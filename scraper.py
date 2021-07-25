"""
Simple scraper: currently analyzing the sources we are using!
"""
import re

import requests
from bs4 import BeautifulSoup

#Testing variables for a singular page
babepage = 'https://drinkbabe.net/collections/wine/products/babe-100-rose'
bevpage = 'https://drinkbev.com/products/rose-wine'

#Dictionary storing all the scraped information
bevinfo = {
    "Flavor"     : '',
    "ABV"        : '',
    "Calories"   : '',
    "Can_Size"   : '',
    "Gluten_Free": '',
    "Carbs"      : '',
    "Sugar"      : '',
    "Sizes"      : [],
    "Costs"      : [],
}

#All the features we will be comparing are stored in these dictionaries
babeinfo = {
    "Flavor"     : '',
    "ABV"        : '',
    "Calories"   : '',
    "Can_Size"   : '',
    "Gluten_Free": '',
    "Carbs"      : '',
    "Sugar"      : '',
    "Sizes"      : [],
    "Costs"      : [],
}

"""
Parse given text for abv information
"""
def parse_abv(pg_txt, soup):
    #print(soup.find_all(attrs={'class': 'flavour-content'}))
    #Works with bev | could be a faster way(iterating through above code and then finding regex?)
    alcContent = soup.find_all(string=re.compile(r"(....)% ABV"))
    print(alcContent)



#send request and fetch the html page defined
page = requests.get(
    bevpage
)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text

parse_abv(page, soup)


