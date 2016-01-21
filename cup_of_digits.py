#!/usr/local/bin/python3

#Import the necessary packages
#Also requires lxml implicitly for BS4
from bs4 import BeautifulSoup
import requests
import json
import dateutil.parser as dateutil
from datetime import date, timedelta

#JSON db file
db_file = 'digits.json'

#URL to scrape
url = 'http://fivethirtyeight.com/features/significant-digits-for-thursday-jan-14-2016/'
page = requests.get(url)
print("URL: ", url)

#Initialize and get the soup using lxml
soup = BeautifulSoup(page.content, 'lxml')

#First pass, the significant digits are located in the following tag
cup_of_soup = soup.find('div', class_='entry-content')

#Initialize list for digits and iterate over every 'h2'
#tag in the 'cup_of_soup' object. Each digit is enclosed
#by a set of 'h2' tags
list_of_digits = []
for h2 in cup_of_soup.find_all('h2'):
    list_of_digits.append(h2.get_text()) #Append only the text of the tag to the list

#Print for validation
print(list_of_digits)

article_date = soup.find('meta', property='article:published_time')['content']
print("Article Date: ", article_date)
parsed_date = dateutil.parse(article_date)
print("Date Conversion: ", parsed_date.strftime('%A-%b-%d-%Y').lower())
parsed_date = parsed_date + timedelta(days=1)
print("Date + delta: ", parsed_date.strftime('%A-%b-%d-%Y').lower())
formatted_date = parsed_date.strftime('%A-%b-%d-%Y').lower()

database = {article_date: list_of_digits}

url = 'http://fivethirtyeight.com/features/significant-digits-for-{}'.format(formatted_date)
page = requests.get(url)
print("URL: ", url)

soup  = BeautifulSoup(page.content, 'lxml')
cup_of_soup = soup.find('div', class_='entry-content')
list_of_digits = []
for h2 in cup_of_soup.find_all('h2'):
    list_of_digits.append(h2.get_text())

article_date = soup.find('meta', property='article:published_time')['content']
database.update({article_date: list_of_digits})

with open(db_file, 'w') as file:
    file.write(json.dumps(database, indent=4))
