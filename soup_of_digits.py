#!/usr/local/bin/python3

from datetime import date, timedelta
from bs4 import BeautifulSoup
import dateutil.parser as dateutil
import requests
import json

start_date = date(2016, 1, 8)
end_date = date(2016, 1, 15)

current_date = start_date

while(current_date <= end_date):

    if(current_date.isoweekday() < 6):
        string_date = current_date.strftime('%A-%b-%d-%Y').lower()
        url = 'http://fivethirtyeight.com/features/significant-digits-for-{}/'.format(string_date)
        page = requests.get(url)

        if(page.status_code == requests.codes.ok):

            soup = BeautifulSoup(page.content, 'lxml')
            article_date = soup.find('meta', property='article:published_time')['content']
            
            if(current_date == dateutil.parse(article_date).date()):
            
                cup_of_soup = soup.find('div', class_='entry-content')

                list_of_digits = []
                for h2 in cup_of_soup.find_all('h2'):
                    list_of_digits.append(h2.get_text())

                print(url)
                print(current_date)
                print(list_of_digits)

    current_date = current_date + timedelta(days=1)
