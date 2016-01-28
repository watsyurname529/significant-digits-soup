#!/usr/local/bin/python3

#Python code to do data wrangling / formatting from raw data files from the 
#webscraper code.

import re
import locale
import json
import csv

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

list_of_counts_alt = {'Zero': list_of_counts[0], 'One': list_of_counts[1], 'Two': list_of_counts[2], 'Three': list_of_counts[3], 'Four': list_of_counts[4], 
        'Five': list_of_counts[5], 'Six': list_of_counts[6], 'Seven': list_of_counts[7], 'Eight': list_of_counts[8], 'Nine': list_of_counts[9]}

#with open('counts.csv', 'w') as csvfile:
#    fieldnames = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    writer.writeheader()
#    writer.writerow(list_of_counts_alt[0])

#with open('counts.csv', 'w') as csvfile:
#    csvfile.write('Digit, Count\n')
#    for key, value in list_of_counts_alt.items():
#        csv_string = key + ',' + str(value) + '\n'
#        csvfile.write(csv_string)

with open('counts.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Digit','Counts'])
    for key, value in list_of_counts_alt.items():
        writer.writerow([key, value])

print(list_of_counts)
print(list_of_counts_alt)
