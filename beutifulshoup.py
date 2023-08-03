from bs4 import BeautifulSoup

import requests
r = requests.get('https://stockx.com/')
 
# check status code for response received
# success code - 200
print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
menu = soup.findAll('div', class_="css-rw1muy-CategoriesContainer")

print(menu)