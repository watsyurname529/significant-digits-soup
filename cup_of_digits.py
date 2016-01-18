#!/usr/local/bin/python3

#Import the necessary packages
#Also requires lxml implicitly for BS4
from bs4 import BeautifulSoup
import requests

#URL to scrape
url = 'http://fivethirtyeight.com/features/significant-digits-for-friday-jan-15-2016/'
page = requests.get(url)

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
