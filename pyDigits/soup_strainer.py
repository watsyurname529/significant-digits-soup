#!/usr/bin/env python3

import regex
import json
import locale

class strainer:

    def __init__(self):
        """Constructor to initialize variables for filename
        and internal database.

        Set's locale for atof function to US; The atof function
        will then ignore all commas in a number-string and use
        a period for the decimal place.
        """
        self.filename = ''
        self.database = {}
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    def read_database_file(self, filename):
        """Given a filename, read that file using the JSON
        module into the internal database variable.

        Return  0 for success
        Return -1 for failure
        """
        try:
            with open(filename, 'r') as db:
                self.filename = filename
                self.database.update(json.load(db))
                return 0
        except IOError:
            print('{} not found.'.format(filename))
            return -1

    def find_numbers(self):
        """In each significant digit entry (or header) it extracts all
        numbers with the built in regex and returns them as a list. The numbers
        are returned as strings. Returns an empty list if no matches
        are found.
        """

        #list_of_digits_str = []
        #list_of_digits_num = []
        #extract_digits = regex.compile(r'[0-9]*(?>[0-9\,\.]?|(?R))*[0-9]+')

        #for key, value in self.database.items():
        #    for entry in value:
        #        list_of_digits_str.extend(extract_digits.findall(entry))

        #for digit_str in list_of_digits_str:
        #    list_of_digits_num.append(locale.atof(digit_str))

        #return list_of_digits_num
        return self.find_numbers_string('');

    def find_numbers_string(self, string):
        """In each significant digit entry (or header) it searches for
        the given string. If the string is found, it extracts the numbers
        in that entry (header) with the built in regex and returns them as a list.
        The numbers are returned as strings. Returns an empty list if
        no matches are found.
        """

        list_of_digits_str = []
        #list_of_digits_num = []
        extract_digits = regex.compile(r'[0-9]*(?>[0-9\,\.]?|(?R))*[0-9]+')

        for key, value in self.database.items():
            for entry in value:
                if string in entry: # and string is not None:
                    list_of_digits_str.extend(extract_digits.findall(entry))

        #for digit_str in list_of_digits_str:
        #    list_of_digits_num.append(locale.atof(digit_str))

        return list_of_digits_str

    def find_regex(self, regex):
        """In each significant digit entry (or header) it searches for all
        matches to the given regex and returns them as a list of strings.
        """

        list_of_matches = []
        extract_expression = regex.compile(regex)

        for key, value in self.database.items():
            for entry in value:
                list_of_matches.extend(extract_expression.find_all(entry))

        return list_of_matches

    def string_to_numbers(self, list_str):

        list_num = []
        for string in list_str:
            list_num.append(locale.atof(string))

        return list_num
