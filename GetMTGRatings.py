from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import urllib
import json
import re
import selenium
from selenium.webdriver.common.by import By
import sqlalchemy as sqlal
from sqlalchemy.orm import sessionmaker
import Env
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.exc import IntegrityError
import time
from selenium import webdriver

Base = declarative_base()

class Draftsim_Card(Base):
    __tablename__ = 'DraftsimRankings'
    Rank = Column(Integer, primary_key=True)
    Name = Column(String, primary_key=True)
    Set = Column(String, primary_key=True)

class Draftsim_Scraper:
    def __init__(self):
        self.card_rank_dic = {}

    def gather_dic_from_site(self, input_web_address):
        driver = webdriver.Chrome()
        try:
            driver.get(input_web_address)
            # All the card rankings are in the draft_img id
            card_ranks_page = driver.find_elements(By.ID, 'draft_img')
            # Pull the text for all the card rankings
            card_ranks_text = card_ranks_page[0].text
            # Replace the headers putting each card in a tier
            card_ranks_text = card_ranks_text.replace('Tier 1: Incredible Bombs', '')
            card_ranks_text = card_ranks_text.replace('Tier 2: Great First Picks', '')
            card_ranks_text = card_ranks_text.replace('Tier 3: Above Average Cards', '')
            card_ranks_text = card_ranks_text.replace('Tier 4: Solid Playables', '')
            card_ranks_text = card_ranks_text.replace('Tier 5: Sometimes Playable', '')
            card_ranks_text = card_ranks_text.replace('Tier 6: Rarely Playable', '')
            card_ranks_text = card_ranks_text.replace('Tier 7: Basically Unplayable', '')
            # Remove the disclaimer text at the bottom
            card_ranks_text = card_ranks_text.replace(
                'Wizards of the Coast, Magic: The Gathering, and their logos are trademarks of Wizards of the Coast LLC. © 2021 Wizards. All rights reserved. The copyright for Magic: the Gathering and all associated card names and card images is held by Wizards of the Coast. Draftsim.com is unofficial Fan Content permitted under the Fan Content Policy. Not approved/endorsed by Wizards. This site is © Draftsim.com. Our Privacy Policy.',
                '')
            # Each card is split by three new lines
            card_ranks_split = card_ranks_text.split('\n\n\n')
            card_rank_dic = {}

            # Remove any extra new lines
            # Split by the '.' such as 1. Card_Name
            for x in range(len(card_ranks_split)):
                card_ranks_split[x] = card_ranks_split[x].replace('\n', '')
                card_rank_number_and_name = card_ranks_split[x].split('. ')
                self.card_rank_dic[card_rank_number_and_name[0].strip()] = card_rank_number_and_name[1].strip()
        finally:
            driver.quit()

    def add_to_database(self, input_database_session, card_rank, card_name, set_name):
        draftsim_database_card = Draftsim_Card(Rank=card_rank, Name=card_name, Set=set_name)
        input_database_session.add(draftsim_database_card)
        try:
            input_database_session.commit()
        except IntegrityError:
            input_database_session.rollback()

    def get_card_dic(self):
        return self.card_rank_dic


Environment = Env.Environment()
engine = Environment.get_database_engine()
Session = sessionmaker(bind=engine)
database_session = Session()

draftsim = Draftsim_Scraper()
#draftsim.gather_dic_from_site("https://draftsim.com/STX-pick-order.php")
draftsim.gather_dic_from_site("https://draftsim.com/KHM-pick-order.php")

cards = draftsim.get_card_dic()

for card in cards:
    name = cards.get(card)
    draftsim.add_to_database(database_session, card, name, "Kaldheim")

database_session.close()