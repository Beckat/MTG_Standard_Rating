from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import urllib
import json
import re
import selenium

import time

from selenium import webdriver


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()

#page = requests.get("https://draftsim.com/STX-pick-order.php")
#soup = BeautifulSoup(page.text, 'html.parser')

#print(soup.prettify())

#data_list  = soup.find_all("script")
#data = data_list[142]
#p = re.compile('construct_pick_order.js = (.*?);')
#m = p.match(str(data))
#stocks = json.loads(m.groups()[0])

