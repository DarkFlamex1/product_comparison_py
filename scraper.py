"""
Simple scraper: currently analyzing the sources we are using!
"""
import re

import requests
from bs4 import BeautifulSoup

#Testing variables for a singular page
from info_struct import info_struct

babepage_link = 'https://drinkbabe.net/collections/wine/products/babe-100-rose'
bevpage_link = 'https://drinkbev.com/products/rose-wine'

#Lists of each companies offerings - consists of info_struct objects
bev_offerings = []
babe_offerings = []

def scrape_babe_flavor(url, info):
    """
    given a flavor url, pulls the information for it
    :return:
    """

    #Request and process the page for scraping
    flav_page = requests.get(
        url
    )
    flav_soup = BeautifulSoup(flav_page.content, 'lxml')

    #Grab product flavor from page title
    info.set('Flavor', flav_soup.select('h1.product-single__title')[0].text.strip())

    #Grab ABV from the page
    #print(flav_soup.find_all(string=re.compile(r"(....)% ABV")))

    #Grab sizes offered look for class=variant-input, data-index=option1 ...
    sizes_offered = flav_soup.find_all(attrs={"class":"variant-input"})
    for item in sizes_offered:
        print(item.attrs['data-value'])

    '''
    Grab all the prices by looking at the option fields
    
    When looking at this data it appears as lists:
    ['8', 'PACK', '-', '$30.99', 'USD']
    ['12', 'PACK', '-', '$43.99', 'USD']
    ['24', 'PACK', '-', '$78.99', 'USD']
    
    Therefore we will take the first and 4th element, (0 and 3) as sizes and costs
    '''

    prices = flav_soup.find_all('option')
    for price_item in prices:
        #clean up the text
        price_txt = price_item.text.strip().split()

        #Get the elements of packs and cost
        size = price_txt[0]
        cost = price_txt[3]

        info.set_costs_sizes(size,cost)


    print(info.get("Sizes_Costs"))
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

parse_abv(page, soup)

#Tests
babered = info_struct()
scrape_babe_flavor("https://drinkbabe.net/collections/wine/products/babe-red", babered)
