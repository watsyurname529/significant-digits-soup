#!/usr/bin/env python3

import soup_strainer as ss

strainer = ss.strainer()

strainer.read_database('test.json')
print('Database')
print(strainer.database)

print('\nAll Digits')
print(strainer.find_all_digits())

print('\nPercents')
print(strainer.find_all_string('percent'))

print('\n$')
print(strainer.find_all_string('$'))

print('\nmillion & billion')
list_million_billion = []
list_million_billion.extend(strainer.find_all_string('million'))
list_million_billion.extend(strainer.find_all_string('billion'))
print(list_million_billion)

print('\nNull String')
print(sorted(strainer.find_all_string('')));
