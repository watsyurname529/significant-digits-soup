#!/usr/local/bin/python3

#Python code to do data wrangling / formatting from raw data files from the 
#webscraper code.

import re
import locale
import json

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

json_file = input('Enter a JSON database file: ')
#json_file = '../digits.json'

with open(json_file, 'r') as file:
    database = json.loads(file.read())
    print(database)

list_of_digits_str = []
list_of_digits_num = []
extract_digits = re.compile(r'[0-9]*[\.\,]?[0-9]+')

for key, value in database.items():
    print(key)
    for entry in value:
        list_of_digits_str.extend(extract_digits.findall(entry))

for digit_str in list_of_digits_str:
    list_of_digits_num.append(locale.atof(digit_str))

#print(list_of_digits_str)
#print(list_of_digits_num)

#list_of_counts = {'Zero': 0, 'One': 0, 'Two': 0, 'Three': 0, 'Four': 0, 'Five': 0, 'Six': 0, 'Seven': 0, 'Eight': 0, 'Nine': 0}
list_of_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for num_string in list_of_digits_str:
    for char in num_string:
        if(char.isdigit()):
            digit = int(char)
            list_of_counts[digit] += 1 

            #for i in range(0,9):
            #    if(digit == i):
            #        list_of_counts[i] += 1 
            #        break 
            
            #if(digit == 0):
            #    list_of_counts['Zero'] += 1 
            #if(digit == 1):
            #    list_of_counts['One'] += 1
            #if(digit == 2):
            #    list_of_counts['Two'] += 1
            #if(digit == 3):
            #    list_of_counts['Three'] += 1
            #if(digit == 4):
            #    list_of_counts['Four'] += 1
            #if(digit == 5):
            #    list_of_counts['Five'] += 1
            #if(digit == 6):
            #    list_of_counts['Six'] += 1
            #if(digit == 7):
            #    list_of_counts['Seven'] += 1
            #if(digit == 8):
                #list_of_counts['Eight'] += 1
            #if(digit == 9):
            #    list_of_counts['Nine'] += 1

print(list_of_counts)
