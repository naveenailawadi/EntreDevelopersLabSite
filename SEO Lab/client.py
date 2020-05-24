from http.client import HTTPSConnection
from base64 import b64encode
from json import loads
from json import dumps


class RestClient:

    def __init__(self, username, password, sandbox):
        self.username = username
        self.password = password

        if sandbox:
            self.domain = "sandbox.dataforseo.com"
        else:
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
- create a current SEO report based on current tags and tokenization (remove useless words)
    - start with the simple organic stuff (google and bing)
        - see: people also search, related searches
    - keywords (GOLDMINE)
        - see: competition (rating 0-1), graph monthly searches over past year
        - required fields: domain, location, language (for optimal accuracy)
'''
