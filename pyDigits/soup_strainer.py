#!/usr/bin/env python3

import regex
import json
import locale

class strainer:

    def __init__(self):
        """Constructor to initialize variables for filename
        and internal database.
        """
        self.filename = ''
        self.database = {}

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

    def find_all_regex(self, regex):
        """
        """

    def find_all_string(self, string):
        """
        """
