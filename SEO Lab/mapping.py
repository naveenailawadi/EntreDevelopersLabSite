import json
from client import RestClient
from secrets import *

CLIENT = RestClient(LOGIN, PASSWORD)


def save_response(path):
    directory = path.split('/')
    filepath = ''
    for name in directory[2:]:
        filepath += f"{name}_"
    filepath = filepath[:-1] + '.json'

    # get the data
    response = json.dumps(CLIENT.get(path), indent=4)
    with open(filepath, 'w') as outfile:
        outfile.write(response)
