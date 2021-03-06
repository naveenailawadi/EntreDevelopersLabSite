from http.client import HTTPSConnection
from base64 import b64encode
from json import loads, dumps


class RestClient:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.domain = "api.dataforseo.com"

    def request(self, path, method, data=None):
        connection = HTTPSConnection(self.domain)
        try:
            base64_bytes = b64encode(
                ("%s:%s" % (self.username, self.password)).encode("ascii")
            ).decode("ascii")
            headers = {'Authorization': 'Basic %s' % base64_bytes, 'Content-Encoding': 'gzip'}
            connection.request(method, path, headers=headers, body=data)
            response = connection.getresponse()
            return loads(response.read().decode())
        finally:
            connection.close()

    def get(self, path):
        return self.request(path, 'GET')

    def post(self, path, data):
        if isinstance(data, str):
            data_str = data
        else:
            data_str = dumps(data)
        return self.request(path, 'POST', data_str)


'''
NOTES
- keyword suggestions could be the most powerful (data for seo labs)
- use the homepage template with checkboxes --> send a cookie to the backend when rerouting to purchase page
'''
