"""
Simple scraper: currently analyzing the sources we are using!
"""
import re

import requests
from bs4 import BeautifulSoup

# Testing variables for a singular page
from info_struct import info_struct

'''
babepage_link = 'https://drinkbabe.net/collections/wine/products/babe-100-rose'
bevpage_link = 'https://drinkbev.com/products/rose-wine'

#Lists of each companies offerings - consists of info_struct objects
bev_offerings = []
babe_offerings = []
'''

'''
Scraper class is an object that can scrape either babe flavor urls or bev flavor urls using the scrape function
'''
class Scraper:
    def __init__(self):
        self.offerings = []

    def scrape_babe_flavor(self, url):
        """
        given a flavor url, pulls the defined information in info_struct.py:
        flavor_info = {
            "Flavor": '',
            "ABV": '',
            "Calories": '',
            "Can_Size": '',
            "Sugar": '',
            "Sizes_Costs": {},
        }

        :return: info_struct
        """
        info = info_struct()
        # Request and process the page for scraping
        flav_page = requests.get(
            url
        )
        flav_soup = BeautifulSoup(flav_page.content, 'lxml')

        faq_page = requests.get(
            'https://drinkbabe.net/pages/faqs'
        )
        faq_soup = BeautifulSoup(faq_page.content, 'lxml')

        # Grab product flavor from page title
        info.set('Flavor', flav_soup.select('h1.product-single__title')[0].text.strip())

        # Grab ABV from the page
        """
        Search for all span elements and then check with regex to find the ABV number
        """
        abv_search = flav_soup.find_all('span')
        for item in abv_search:
            if(re.search(r"(\d*.\d)% ABV", item.text)):
                info.set('ABV', re.search(r"(\d*.\d*)% ABV", item.text).group(1))
                break

        '''
        Grab all the prices by looking at the option fields
        
        When looking at this data it appears as lists:
        ['8', 'PACK', '-', '$30.99', 'USD']
        ['12', 'PACK', '-', '$43.99', 'USD']
        ['24', 'PACK', '-', '$78.99', 'USD']
        
        Therefore we will take the first and 4th element, (0 and 3) as sizes and costs
        '''

        #Iterate through all the prices and pack sizes
        prices = flav_soup.find_all('option')
        for price_item in prices:
            #clean up the text
            price_txt = price_item.text.strip().split()

            #Get the elements of packs and cost
            size = price_txt[0]
            cost = price_txt[3]

            info.set_costs_sizes(size,cost)

        #Nutrition information search
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

        '''
        print(info.get("Flavor"))
        print(info.get("ABV"))
        print(info.get("Calories"))
        print(info.get("Sugar"))
        print(info.get("Sizes_Costs"))
        '''
        return info



    def scrape_bev_flavor(self, url):
        """
            given a flavor url, pulls the defined information in info_struct.py:
            flavor_info = {
                "Flavor": '',
                "ABV": '',
                "Calories": '',
                "Can_Size": '',
                "Sugar": '',
                "Sizes_Costs": {},
            }

            :return: infostruct info
        """
        info = info_struct()

        # Request and process the page for scraping
        flav_page = requests.get(
            url
        )
        #This is the beautiful soup object of our bev flavor
        flav_soup = BeautifulSoup(flav_page.content, 'lxml')

        #The faq page
        faq_page = requests.get(
            'https://drinkbabe.net/pages/faqs'
        )
        #The faq soup object
        faq_soup = BeautifulSoup(faq_page.content, 'lxml')

        # Grab product flavor from page title
        info.set('Flavor', flav_soup.select('h1.product-single__title')[0].text.strip())

        """
        Search for ABV, calroies, and sugar using regex expressions and matching groups
        """
        span_search = flav_soup.find_all('span')
        for item in span_search:
            #Check for ABV
            abv_search = re.search(r"(\d*.\d)% ABV", item.text)
            calories_search = re.search(r"(\d*) CALORIES", item.text)
            sugar_search = re.search(r"(.*)G SUGAR", item.text)

            # if abv search matched, set the information
            if (abv_search):
                info.set('ABV', abv_search.group(1))
            #if calorie search matched, set the information
            if (calories_search):
                info.set('Calories', calories_search.group(1))
            #if sugar search matched, set the information
            if (sugar_search):
                #Check for a special case on website where they use capital o as a zero
                if(sugar_search.group(1) == "O"):
                    info.set('Sugar', 0)
                else:
                    info.set('Sugar', sugar_search.group(1))

        '''
            Grab all the prices by looking at the radio container fields
    
            Therefore we will take the first and 4th element, (0 and 3) as sizes and costs
        '''

        # Iterate through all the prices and pack sizes
        prices = flav_soup.find_all('div', {'class':'radio_container'})

        #Hard coded price, should use selemium instead!
        i = 0
        list_prices = ['$49($39 via Bev club)', '99($79 via Bev club)', '$190($152 via Bev club)']

        #Iterate through all the prices
        for price_item in prices:
            # clean up the text
            price_txt = price_item.text.strip().split()
            #Check if a valid price
            if(price_txt):
                #Assign the cost(lowest to max order)
                cost = list_prices[i]
                size = price_txt[0]
                i += 1
                info.set_costs_sizes(size, cost)

        '''
        print(info.get("Flavor"))
        print(info.get("ABV"))
        print(info.get("Calories"))
        print(info.get("Sugar"))
        print(info.get("Sizes_Costs"))
        '''
        return info



#Have a parent function that does the below on a button press!



#Create functions that parse the offerings from the given links - test without iterator, add iterator if I have time
#FAQ is needed for most of the information

#Iterate through the main page, grabbing all the links of the offerings
#Then go through each of the links filling out the info_struct given the designed code

#Finally display each info_struct on a flask application, with tables or some clear split

#write up focumentation as we go in comments, then see

#turn into function
#send request and fetch the html page defined

#Tests
babered = info_struct()
babegrigio = info_struct()

#Bev tests
bevrose = info_struct()
bevblanc = info_struct()

'''
scrape_babe_flavor("https://drinkbabe.net/collections/wine/products/babe-grigio", babegrigio)
scrape_babe_flavor("https://drinkbabe.net/collections/wine/products/babe-red", babered)

scrape_bev_flavor("https://drinkbev.com/products/rose-wine", bevrose)
scrape_bev_flavor("https://drinkbev.com/products/bev-blanc", bevblanc)
'''