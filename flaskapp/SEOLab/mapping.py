import json
from client import RestClient
from secrets import *


class Mapper:
    def __init__(self):
        self.client = RestClient(LOGIN, PASSWORD)

    def save_get_response(self, path):
        directory = path.split('/')
        filepath = ''
        for name in directory:
            filepath += f"{name}_"
        filepath = filepath[:-1] + '.json'

        # get the data
        response = json.dumps(self.client.get(path), indent=4)
        with open(filepath, 'w') as outfile:
            outfile.write(response)
