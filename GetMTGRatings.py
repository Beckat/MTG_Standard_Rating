from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import urllib
import json
import re
import selenium
from selenium.webdriver.common.by import By

import time

from selenium import webdriver


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('https://draftsim.com/STX-pick-order.php');

card_ranks = driver.find_elements(By.ID, 'draft_img')

driver.quit()

