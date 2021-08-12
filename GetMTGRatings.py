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
    __tablename__ = 'Draftsim_Rankings'
    name = Column(String, primary_key=True)
    faceName = Column(String, primary_key=True)
    type = Column(String)

class draftSimScraper:
    def __init__(self, input_web_address, input_set, input_database_session, input_draftsim_card):
        self.web_address = input_web_address
        self.set_name = input_web_address
        self.database_session = input_database_session
        self.draftsim_card = input_draftsim_card

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('https://draftsim.com/STX-pick-order.php');

card_ranks_page = driver.find_elements(By.ID, 'draft_img')
card_ranks_text = card_ranks_page[0].text
card_ranks_text = card_ranks_text.replace('Tier 1: Incredible Bombs', '')
card_ranks_text = card_ranks_text.replace('Tier 2: Great First Picks', '')
card_ranks_text = card_ranks_text.replace('Tier 3: Above Average Cards', '')
card_ranks_text = card_ranks_text.replace('Tier 4: Solid Playables', '')
card_ranks_text = card_ranks_text.replace('Tier 5: Sometimes Playable', '')
card_ranks_text = card_ranks_text.replace('Tier 6: Rarely Playable', '')
card_ranks_text = card_ranks_text.replace('Tier 7: Basically Unplayable', '')
card_ranks_text = card_ranks_text.replace('Wizards of the Coast, Magic: The Gathering, and their logos are trademarks of Wizards of the Coast LLC. © 2021 Wizards. All rights reserved. The copyright for Magic: the Gathering and all associated card names and card images is held by Wizards of the Coast. Draftsim.com is unofficial Fan Content permitted under the Fan Content Policy. Not approved/endorsed by Wizards. This site is © Draftsim.com. Our Privacy Policy.', '')
card_ranks_split = card_ranks_text.split('\n\n\n')
card_rank_dic = {}

for x in range(len(card_ranks_split)):
    card_ranks_split[x] = card_ranks_split[x].replace('\n', '')
    card_rank_number_and_name = card_ranks_split[x].split('. ')
    card_rank_dic[card_rank_number_and_name[0].strip()] = card_rank_number_and_name[1].strip()

driver.quit()

