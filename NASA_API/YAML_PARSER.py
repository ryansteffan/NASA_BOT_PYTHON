__name__ = "YAML_PARSER"

import yaml

class yaml_parser:
    def __init__(self, location):
        self.yaml_location = location

        #Sets the config location

    def parse_data(self, index, item=0):
        with open(self.yaml_location, 'r') as file:
            self.out = yaml.safe_load(file)
            self.condition = []
            if type(self.out[index]) == type(self.condition):
                self.item_list = self.out[index]
                return self.item_list[item]
            else:
                return self.out[index]

        #Pareses the yaml. Checks if the index is a list and then either returns the part of the index specified or the index as a whole if not a list.

