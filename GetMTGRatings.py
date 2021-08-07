from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request

req = Request("https://www.coolstuffinc.com/a/aliaintrazi-07222021-afr-standard-set-review-red", headers={"User Agent" : "Mozilla/5.0"})
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')

print(soup.prettify())