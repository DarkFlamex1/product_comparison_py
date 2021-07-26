# product_comparison_py
product comparison task

## Live Preview:
https://enigmatic-waters-39562.herokuapp.com/

## Structure of Application:
app.py contains the main logic built of two secondary files.
-> scraper.py
-> info_struct.py

### Scraper Class
This is a scraper that utilized beautiful soup 4 and multiple regex functions in order to find the specified elements we are looking for in each wine flavor.
- Two member functions, one for babe and one for bev which take in a url and return a info_struct as defined in info_struct.py
- Can be instantiated and used to call its member functions(see app.py)

### info_struct class
This class is the representation and helper methods of all the information we are scraping from all the products.
```python
self.flavor_info = {
            "Flavor": '',
            "ABV": '',
            "Calories": '',
            "Can_Size": '',
            "Sugar": '',
            "Sizes_Costs": {},
        }
```

### Flask Application
In app.py we have a basic flask application that renders all collected information into tables for easy comparisons.

## Walkthrough
When we first enter the app on the live preview we have a comparison button waiting on the page. Once clicked, this button will instantiate the scraper object and begin calling the scraper on two bev products and two babe products. The goal is to grab all the information in info_struct.py and then convert into pandas dataframes which become basic html tables for easy viewing. If this was going to be a full program, the python code would actually iterate through all the product offerings(with simple loops) and call the scraper on each product to create a full list of product offerings. Later this data can be turned into a csv, or any excel format.
