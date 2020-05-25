from client import RestClient
from secrets import *


class KeywordsAnalyzer:
    def __init__(self, sandbox=False):
        self.client = RestClient(LOGIN, PASSWORD, sandbox=sandbox)

    def create_task(self, location, website):
        post_data = dict()
        # simple way to set a task
        post_data[len(post_data)] = dict(
            location_name=location,
            target=website)

        # send the request
        response = self.client.post("/v3/keywords_data/google/keywords_for_site/task_post", post_data)

        return response

    def get_tasks_ready(self):
        response = self.client.get("/v3/keywords_data/google/keywords_for_site/tasks_ready")

        return response

    def create_task_live(self, location, website):
        post_data = dict()
        # simple way to set a task
        post_data[len(post_data)] = dict(
            location_name=location,
            target=website)

        # send the request
        response = self.client.post("/v3/keywords_data/google/keywords_for_site/task_post/live", post_data)

        return response


'''
NOTES
- create a current SEO report based on current tags and tokenization (remove useless words)
    - start with the simple organic stuff (google and bing)
        - see: people also search, related searches
    - keywords (GOLDMINE)
        - see: competition (rating 0-1), graph monthly searches over past year
        - required fields: domain, location, language (for optimal accuracy)
'''
