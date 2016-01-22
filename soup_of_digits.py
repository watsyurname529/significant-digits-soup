#!/usr/local/bin/python3

#Import necessary modules
#BeautifulSoup implicitly requires the lxml package
from datetime import date, timedelta
from bs4 import BeautifulSoup
import dateutil.parser as dateutil
import requests
import json

def format_date_string( current_date ):
    date_string = current_date.strftime('%A-%b-%-d-%Y').lower()
    month = current_date.month
    if(month == 3):
        date_string = date_string.replace('mar', 'march')
    elif(month == 4):
        date_string = date_string.replace('apr', 'april')
    elif(month == 6):
        date_string = date_string.replace('jun', 'june')
    elif(month == 7):
        date_string = date_string.replace('jul', 'july')
    elif(month == 9):
        date_string = date_string.replace('sep', 'sept')
    return date_string


#Setup dates for the scraper
start_date = date(2014, 12, 16) #Significant Digits Start Date: 2014-12-16
end_date = date.today() #date(2015, 2, 1)
current_date = start_date

#Setup database and json file
database = {}
json_file = 'digits.json'

#Main loop. For each day between the start and end date, try to load the webpage and
#extract the numbers.
while(current_date <= end_date):

    #Ignore Saturdays and Sundays when the article is not published
    if(current_date.isoweekday() < 6):
        #date_string = current_date.strftime('%A-%b-%-d-%Y').lower()
        date_string = format_date_string(current_date)
        url = 'http://fivethirtyeight.com/datalab/significant-digits-for-{}/'.format(date_string)
        page = requests.get(url)

        #The url changed at some point in time, check for both if one fails
        if(page.status_code != requests.codes.ok):
            url = 'http://fivethirtyeight.com/features/significant-digits-for-{}/'.format(date_string)
            page = requests.get(url)

        #If the page loads correctly, parse the page
        if(page.status_code == requests.codes.ok):

            #Initialize parser with lxml
            soup = BeautifulSoup(page.content, 'lxml')
            article_date = soup.find('meta', property='article:published_time')['content']
            
            #Check if the article date matches the date we asked for
            if(current_date == dateutil.parse(article_date).date()):
            
                #Find the block of significant digits
                cup_of_soup = soup.find('div', class_='entry-content')

                #Extract the digits themselves without the html tags
                list_of_digits = []
                for h2 in cup_of_soup.find_all('h2'):
                    list_of_digits.append(h2.get_text())

                #print(url)
                print(current_date)
                #print(dateutil.parse(article_date))
                #print(list_of_digits)

                #Store in the database with the article date as the key
                database.update({current_date.isoformat(): list_of_digits})
        else:
            print('Invalid URL: ', url)

    #Advance the date object by one day
    current_date = current_date + timedelta(days=1)

#Save database in a json file
with open(json_file, 'w') as file:
    file.write(json.dumps(database, indent=4))
