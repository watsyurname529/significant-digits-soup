#!/usr/bin/env python3

import soup_strainer
ss = soup_strainer.strainer()

json_file = input('Enter a JSON database file: ')
if(ss.read_database_file(json_file) == -1):
    print('Terminating execution.')
    quit()

list_of_numbers = ss.find_numbers()

#Frequency of Digits selection
list_of_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for number in list_of_numbers:
    for char in number:
        if(char.isdigit()):
            list_of_counts[int(char)] += 1

list_of_counts = {'Zero': list_of_counts[0], 'One': list_of_counts[1], 'Two': list_of_counts[2], 'Three': list_of_counts[3], 'Four': list_of_counts[4],
        'Five': list_of_counts[5], 'Six': list_of_counts[6], 'Seven': list_of_counts[7], 'Eight': list_of_counts[8], 'Nine': list_of_counts[9]}
list_of_numbers = ss.string_to_numbers(list_of_numbers)

#Frequency of Percent selection
list_of_percents = ss.find_numbers_string('percent')
list_of_percents = ss.string_to_numbers(list_of_percents)

#Frequency of $ selection
list_of_dollars = ss.find_numbers_string('$')
list_of_dollars = ss.string_to_numbers(list_of_dollars)

with open('counts.csv', 'w') as csvfile:
   csvfile.write('Digit,Counts\n')
   for key, value in list_of_counts.items():
       #csv_string = key + ',' + str(value) + '\n'
       csv_string = '{},{}\n'.format(key,value)
       csvfile.write(csv_string)

with open('numbers.csv', 'w') as csvfile:
    csvfile.write('Number\n')
    for number in list_of_numbers:
        csv_string = '{}\n'.format(number)
        csvfile.write(csv_string)

with open('percent.csv', 'w') as csvfile:
    csvfile.write('Percent\n')
    for percent in list_of_percents:
        #csv_string = percent + '\n'
        csv_string = '{}\n'.format(percent)
        csvfile.write(csv_string)

# with open('dollars.csv', 'w') as csvfile:
#     csvfile.write('Dollars\n')
#     for dollars in list_of_dollars:
#         #csv_string = percent + '\n'
#         csv_string = '{}\n'.format(dollars)
#         csvfile.write(csv_string)
