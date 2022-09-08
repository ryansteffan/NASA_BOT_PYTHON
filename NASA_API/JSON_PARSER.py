__name__ = "JSON_PARSER"

import requests

class json_parser:
    def __init__(self, url):
        self.request = requests.get(url)
        self.json = self.request.json()

        #Gets the json data from the provided url.

    def all(self):
        return self.json

        #returns the json data in full

    def parse_data(self, dic_item):
        item = self.json[dic_item]
        return item

        #Returns a given item from the full json data 