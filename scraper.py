"""
Simple scraper: currently analyzing the sources we are using!
"""

import requests

res = requests.get(
    'https://drinkbabe.net/collections/wine/products/babe-100-rose'
)

txt = res.text
status = res.status_code

print(txt,status)