from client import RestClient
from secrets import *


class KeywordsAnalyzer:
    def __init__(self):
        self.client = RestClient(LOGIN, PASSWORD)
        self.open_tasks = set()

    def create_task(self, location, website):
        post_data = dict()
        # simple way to set a task
        post_data[len(post_data)] = dict(
            location_name=location,
            target=website)

        # send the request
        response = self.client.post("/v3/keywords_data/google/keywords_for_site/task_post", post_data)

        # add the task id to the open tasks
        self.open_tasks.update({task['id'] for task in response['tasks']})

        return response

    def get_task_data(self, task_id):
        response = self.client.get(f"/v3/keywords_data/google/keywords_for_site/task_get/{task_id}")

        return response

    def get_all_open_tasks(self):
        temp_set = self.open_tasks

        for task_id in temp_set:
            response = self.get_task_data(task_id)
            if response['status_code'] == 20000:
                # the task id can be removed and added to the completed database (to be created)
                self.open_tasks.remove(task_id)

    def get_tasks_ready(self):
        response = self.client.get("/v3/keywords_data/google/keywords_for_site/tasks_ready")

        return response

    def get_tasks_data(self):
        response = self.client.get("/v3/keywords_data/google/keywords_for_site/tasks_ready")

        # you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
        if response['status_code'] == 20000:
            results = []
            for task in response['tasks']:
                if (task['result'] and (len(task['result']) > 0)):
                    for resultTaskInfo in task['result']:
                        # 2 - using this method you can get results of each completed task
                        # GET /v3/keywords_data/google/search_volume/task_get/$id
                        if(resultTaskInfo['endpoint']):
                            results.append(client.get(resultTaskInfo['endpoint']))


'''
NOTES
- create a current SEO report based on current tags and tokenization (remove useless words)
    - start with the simple organic stuff (google and bing)
        - see: people also search, related searches
    - keywords (GOLDMINE)
        - see: competition (rating 0-1), graph monthly searches over past year
        - required fields: domain, location, language (for optimal accuracy)
- allow for custom keywords testing --> $1 per 10 keywords
- running
    - log completions --> update every hour and send to client
'''
