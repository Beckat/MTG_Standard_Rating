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
from sqlalchemy import Column, Integer, String, Date, REAL
from sqlalchemy.exc import IntegrityError
import time
from selenium import webdriver
import  pandas as pd


# each setp is .077 up from F to A+
# class=wp-block-columns
# https://mtgazone.com/strixhaven-school-of-mages-stx-limited-tier-list/


Base = declarative_base()

class Database_Card(Base):
    __tablename__ = 'MTGAZoneRatings'
    Name = Column(String, primary_key=True)
    Set = Column(String, primary_key=True)
    Grade = Column(String)
    WeightedRating = Column(REAL)


# Holds the database connection information
Environment = Env.Environment()
engine = Environment.get_database_engine()
Session = sessionmaker(bind=engine)
database_session = Session()

# Gets the grades F-A+ and their weight 0-1.0
grade_table_df = pd.read_sql_table(
    "GradeSystemWeight",
    con=engine
)


class MTGAZone_Scraper:
    def __init__(self):
        self.card_rank_dic = {}

    def gather_dic_from_site(self, input_web_address):
        driver = webdriver.Chrome()
        try:
            driver.get(input_web_address)
            card_ranks_page = driver.find_elements(By.CLASS_NAME, 'wp-block-columns')
            card_ranks_text = card_ranks_page[0].text
            card_ranks_split = card_ranks_text.split('\n')
            card_rank_dic = {}

            # Remove any extra new lines
            # Split by the '.' such as 1. Card_Name
            for x in range(len(card_ranks_split)):
                card_ranks_split[x] = card_ranks_split[x].replace('\n', '')
                card_rank_number_and_name = card_ranks_split[x].split('. ')
                self.card_rank_dic[card_rank_number_and_name[0].strip()] = card_rank_number_and_name[1].strip()
        finally:
            driver.quit()

    def add_to_database(self, input_database_session, card_grade, card_name, set_name, weighed_rating):
        # Creates the object to be added to the database
        database_card = Database_Card(Grade=card_grade, Name=card_name, Set=set_name,
                                                   WeightedRating=weighed_rating)
        input_database_session.add(database_card)
        try:
            input_database_session.commit()
        # Error if the insert would cause an integrety error in the database such as duplicate primary key value
        except IntegrityError:
            input_database_session.rollback()

    def get_card_dic(self):
        return self.card_rank_dic


trans_df = grade_table_df.set_index("Grade").T

grade_dict = trans_df.to_dict()

# Uses selenium to open the web page to scrape ratings
driver = webdriver.Chrome()
driver.get("https://mtgazone.com/strixhaven-school-of-mages-stx-limited-tier-list/")
card_ranks_page = driver.find_elements(By.CLASS_NAME, 'wp-block-columns')
card_ranks_text = card_ranks_page[0].text
card_ranks_split = card_ranks_text.split('\n')

# Check the last two characters against our ratings A+, A, A-, etc... and if it matches remove the last two characters
# Trim the results and set naem as the remainder and the score as what was there

print(card_ranks_text)

card_grade = ""
card_weight_rank = 0.0
card_name = ""

for card in card_ranks_split:
    # We can't check if the last two characters are a grade if the string is length 1 or 0
    if len(card) > 1:
        card_grade = card[-2:].strip()
        # Check if the stripped last two characters match one of the grades
        if card_grade in grade_dict.keys():
            card_weight_rank = grade_dict[card_grade]["WeightedRating"]
            card_name = card[:(len(card) - 2)].strip()

            # Set the values to add to the database
            database_card = Database_Card(Grade=card_grade, Name=card_name, Set="Strixhaven",
                                                   WeightedRating=card_weight_rank)
            database_session.add(database_card)
            try:
                database_session.commit()
            # Error if the insert would cause an integrety error in the database such as duplicate primary key value
            except IntegrityError:
                database_session.rollback()



driver.quit()
database_session.close()