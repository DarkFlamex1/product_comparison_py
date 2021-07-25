"""
Simple scraper: currently analyzing the sources we are using!
"""
import re

import requests
from bs4 import BeautifulSoup

#Testing variables for a singular page
babepage_link = 'https://drinkbabe.net/collections/wine/products/babe-100-rose'
bevpage_link = 'https://drinkbev.com/products/rose-wine'

#Lists of each companies offerings - consists of info_struct objects
bev_offerings = []
babe_offerings = []

""""
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
}"""

"""
Parse given text for abv information
"""

#Have a parent function that does the below on a button press!



#Create functions that parse the offerings from the given links - test without iterator, add iterator if I have time
#FAQ is needed for most of the information

#Iterate through the main page, grabbing all the links of the offerings
#Then go through each of the links filling out the info_struct given the designed code

#Finally display each info_struct on a flask application, with tables or some clear split

#write up focumentation as we go in comments, then see




def parse_abv(pg_txt, soup):
    #print(soup.find_all(attrs={'class': 'flavour-content'}))
    #Works with bev | could be a faster way(iterating through above code and then finding regex?)
    alcContent = soup.find_all(string=re.compile(r"(....)% ABV"))
    print(alcContent)


#turn into function
#send request and fetch the html page defined
page = requests.get(
    bevpage_link
)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text

parse_abv(page, soup)


