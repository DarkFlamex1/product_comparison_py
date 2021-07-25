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

    faq_page = requests.get(
        'https://drinkbabe.net/pages/faqs'
    )
    faq_soup = BeautifulSoup(faq_page.content, 'lxml')

    #Grab product flavor from page title
    info.set('Flavor', flav_soup.select('h1.product-single__title')[0].text.strip())

    #Grab ABV from the page
    """
    Search for all span elements and then check with regex to find the ABV number
    We use 0:4 as all the ABV's are at most one decimal point
    """
    abv_search = flav_soup.find_all('span')
    for item in abv_search:
        if(re.search(r"(\d*.\d)% ABV", item.text)):
            info.set('ABV', re.search(r"(\d*.\d)% ABV", item.text).group()[0:4])
            break

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

    nutrition = faq_soup.find_all('div', {'class':"collapsible-content__inner collapsible-content__inner--faq rte"})
    for nutrition_info in nutrition:
        #use regex to search for the calories and carbs
        regexp = info.get('Flavor').split()[1].upper() + " IS (\d*) CALORIES AND (\d.\d*)"
        searchresult = re.search(regexp, nutrition_info.text)
        #if we get a result!
        if(searchresult):
            '''
            Using searchresult.groups shows us the calories in first index and sugar in second
            '''
            info.set("Calories",searchresult.group(1))
            info.set("Sugar", searchresult.group(2))
            break

    print(info.get("Flavor"))
    print(info.get("ABV"))
    print(info.get("Calories"))
    print(info.get("Sugar"))
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

#turn into function
#send request and fetch the html page defined
page = requests.get(
    bevpage_link
)

soup = BeautifulSoup(page.content, 'html.parser')

#Tests
babered = info_struct()
scrape_babe_flavor("https://drinkbabe.net/collections/wine/products/babe-grigio", babered)
