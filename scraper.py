"""
Simple scraper: currently analyzing the sources we are using!
"""

import requests
from bs4 import BeautifulSoup

#Testing variables for a singular page
babepage = 'https://drinkbabe.net/collections/wine/products/babe-100-rose'
bevpage = 'https://drinkbev.com/products/rose-wine'

#send request and fetch the html page defined
page = requests.get(
    bevpage
)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text

print(title)
