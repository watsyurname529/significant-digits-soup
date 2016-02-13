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

    def read_database(self, filename):
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

    def find_all_digits(self):
        """
        """

        list_of_digits_str = []
        list_of_digits_num = []
        extract_digits = regex.compile(r'[0-9]*(?>[0-9\,\.]?|(?R))*[0-9]+')

        for key, value in self.database.items():
            for entry in value:
                list_of_digits_str.extend(extract_digits.find_all(entry))

        for digit_str in list_of_digits_str:
            list_of_digits_num.append(locale.atof(digit_str))

        return list_of_digits_num

    def find_all_string(self, string):
        """
        """

        list_of_digits_str = []
        list_of_digits_num = []
        extract_digits = regex.compile(r'[0-9]*(?>[0-9\,\.]?|(?R))*[0-9]+')

        for key, value in self.database.items():
            for entry in value:
                if string in entry:
                    list_of_digits_str.extend(extract_digits.find_all(entry))

        for digit_str in list_of_digits_str:
            list_of_digits_num.append(locale.atof(digit_str))

        return list_of_digits_num

    def find_all_regex(self, regex):
        """
        """
        
        list_of_matches = []
        extract_expression = regex.compile(regex)

        for key, value in self.database.items():
            for entry in value:
                list_of_matches.extend(extract_expression.find_all(entry))

        return list_of_matches
