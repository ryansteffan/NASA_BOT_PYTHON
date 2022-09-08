__name__ = "API"

import os
from NASA_API.JSON_PARSER import json_parser
from NASA_API.YAML_PARSER import yaml_parser

#Imports the classes that are used to parse the data from NASA and the yaml config

class api:
    def __init__(self, conf_location, conf_index):
        self.location = os.path.abspath(conf_location)
        self.index = conf_index 

        #Sets the config location and what item from the config to grab.

    def url_grab(self):
        self.url = yaml_parser(self.location).parse_data(self.index)
        return self.url

        #Returns the the url from the yaml config

    def json_full(self):
        self.full_data = json_parser(self.url_grab()).all()
        return self.full_data

        #Grabs all of the data from url returned via url_grab()

    def json_data(self, item):
        self.data = json_parser(self.url_grab()).parse_data(item)
        return self.data

        #returns the spicific item from the json data

#syntax:    api('conf\config.yaml', 'APOD_URL').json_data('url')

