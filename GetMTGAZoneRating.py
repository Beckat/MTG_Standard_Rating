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


# each setp is .077 up from F to A+
# class=wp-block-columns
# https://mtgazone.com/strixhaven-school-of-mages-stx-limited-tier-list/


Base = declarative_base()

Environment = Env.Environment()
engine = Environment.get_database_engine()
Session = sessionmaker(bind=engine)
database_session = Session()

driver = webdriver.Chrome()
driver.get("https://mtgazone.com/strixhaven-school-of-mages-stx-limited-tier-list/")
card_ranks_page = driver.find_elements(By.CLASS_NAME, 'wp-block-columns')
card_ranks_text = card_ranks_page[0].text

print(card_ranks_text)

driver.quit()
database_session.close()
# Added grade breakdown in database