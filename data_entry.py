#!/usr/local/bin/python3

import json

quit = False
database = {}
json_file = input('Enter JSON DB: ')

if(json_file != ""):
    with open(json_file, 'r') as file:
        file_db = json.loads(file.read())
    database.update(file_db)
else:
    quit = True
    print('Exiting program.')

while(quit == False):
    choice = input('New JSON Entry (Y/N): ')

    if(choice == 'Y'):
        list = []
        key = input('Article Date as YYYY-MM-DD: ')
        while(True):
            digit = input('Enter digits: ')
            if(digit != ""):
                list.append(digit)
            else:
                break
        database.update({key: list})

    elif(choice == 'N'):
        quit = True
        print('Exiting program.')
    
    else:
        print(choice, 'Not valid option.')

if(json_file != ""):
    with open(json_file, 'w') as file:
        file.write(json.dumps(database, indent=4))
    print('Database saved.')
