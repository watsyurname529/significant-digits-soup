#!/usr/local/bin/python3

#Python code to do data wrangling / formatting from raw data files from the 
#webscraper code.

import re
import locale
import json

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

#json_file = input('Enter a JSON database file: ')
json_file = '../digits.json'

with open(json_file, 'r') as file:
    database = json.loads(file.read())
    print(database)

list_of_digits = []
list_of_numbers = []
extract_digits = re.compile(r'[0-9]*[\.\,]?[0-9]+')

for key, value in database.items():
    print(key)
    for entry in value:

        #print(re.findall(r'[0-9]*[\.\,]?[0-9]+', entry))
        list_of_digits.extend(extract_digits.findall(entry))
        #list_of_digits.append(float(s) for s in entry.split() if s.isdigit())
        #print(float(s)) for s in entry.split() if s.isdigit()
        #for s in entry.split(): 
            #if s.isdigit():
                #print(s)
for str in list_of_digits:
    list_of_numbers.append(locale.atof(str))

print(list_of_digits)
print(list_of_numbers)
