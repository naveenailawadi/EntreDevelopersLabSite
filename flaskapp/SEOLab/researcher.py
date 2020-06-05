from flask import url_for
from flaskapp.SEOLab.client import RestClient
from flaskapp.SEOLab.secrets import *
from datetime import datetime as dt
import json
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np


# create a class that hosts the necessary data
class Report:
    def __init__(self, report_id, endpoint):
        # create a
        today = dt.now()
        self.client = RestClient(LOGIN, PASSWORD)

        # eventually get this from a database
        self.date = f"{today.month}/{today.day}/{today.year} ({today.hour}:{today.minute})"
        self.id = report_id

        # create a folder for the report

        # handle for a blank current directory
        self.current_directory = os.getcwd()
        self.in_wsgi = False
        if len(self.current_directory) < 3:
            self.current_directory = '/var/www/EntreDevelopersLabSite'
            self.in_wsgi = True

        self.directory = f"{self.current_directory}/flaskapp{url_for('static', filename='SEOLabReports')}/{self.id}"

        try:
            os.mkdir(self.directory)
            self.new_additions = True
        except FileExistsError:
            self.new_additions = False

        # set the variables in the response
        exec(f"self.{endpoint}()")

    # create a method just for testing

    def test(self):
        # make the response an object to call it later (when creating data forms)
        test_data = f"{self.current_directory}/flaskapp/SEOLab/Responses/_v3_keywords_data_google_keywords_for_site_task_get_apple.json"

        self.response = json.loads(open(test_data).read())

        # make useful variables for making graphs
        keyword_max = 25

        # allow the user to set the number of keywords
        results = self.response['tasks'][0]['result'][:keyword_max]
        self.keywords = [entry['keyword'] for entry in results]
        self.search_volumes = [entry['search_volume'] for entry in results]
        self.cpcs = [entry['cpc'] for entry in results]
        self.competition_ratings = [entry['competition'] * 100 for entry in results]
        self.firepower_ratings = [entry['search_volume'] / entry['competition'] for entry in results]

        # create a dictionary of records
        self.monthly_search_data = {record['keyword']: record['monthly_searches'] for record in results}

        self.location = self.response['tasks'][0]['data']['location_name']
        self.url = self.response['tasks'][0]['data']['target']

    def create_task(self, location, website):
        post_data = dict()
        # simple way to set a task
        post_data[len(post_data)] = dict(
            location_name=location,
            target=website)

        # send the request
        response = self.client.post("/v3/keywords_data/google/keywords_for_site/task_post", post_data)

        return response

    # create a class that creates reports for all the keywords upon a search
    def get_task_keywords_data(self):
        # make the response an object to call it later (when creating data forms)
        self.response = self.client.get(f"/v3/keywords_data/google/keywords_for_site/task_get/{self.id}")
        self.location = self.response['tasks'][0]['data']['location_name']
        self.url = self.response['tasks'][0]['data']['target']

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

    # make functions to add particular charts depending on the report requested
    def create_horizontal_bar_chart(self, values, labels, title, ylabel, xlabel):
        file = f"{title}.png"
        if self.new_additions:
            sns.set(style="whitegrid", font_scale=1.5)
            sns.set_color_codes("pastel")

            # Initialize the matplotlib figure
            plt.rcParams['figure.figsize'] = (len(self.keywords), 10)
            plt.ylim(200)

            plt.title(title)
            plt.ylabel(ylabel)
            plt.xlabel(xlabel)
            sns.barplot(x=labels, y=values)

            # save the file to the folder created for the report
            plot_url = f"{self.directory}/{file}"

            plt.savefig(plot_url)
            plt.close()

        return url_for('static', filename=f"SEOLabReports/{self.id}/{file}")

    def create_line_graph(self, trend_list, label, title, ylabel, xlabel):
        file = f"{title}.png"
        print(trend_list)
        if True:  # self.new_additions:
            sns.set(style="whitegrid", font_scale=1.5)
            sns.set_color_codes("pastel")

            # Initialize the matplotlib figure
            plt.rcParams['figure.figsize'] = (len(self.keywords), 10)

            plt.title(title)
            plt.ylabel(ylabel)
            plt.xlabel(xlabel)
            sns.lineplot(data=trend_list, label=label)

            # save the file to the folder created for the report
            plot_url = f"{self.directory}/{file}"

            plt.savefig(plot_url)
            plt.close()

        return url_for('static', filename=f"SEOLabReports/{self.id}/{file}")

    # create a function that returns a list from the
    def extract_trend(self, key, keyword_records):
        trend_list = [record[key] for record in keyword_records]
        return np.flip(np.array(trend_list))


'''
NOTES
- allow for custom keywords testing --> $1 per 10 keywords
- running
    - log completions --> update every hour and send to client
    - going to need a way to filter the most important keywords --> allow user to filter data
    - create a pingback endpoint
- keywords configuration (get custom domain recommendations)
    - store ids in a database --> can be used later to recreate SEO pulls (email this ID as confirmation)
        - can add this to a user account if necessary (but probably overkill)
        - will need date and time that the report was created
        - will need to record sales for this in this database --> can track revenue over time
    - can add some metrics about other ads and expected costs with the /v3/keywords_data/google/ad_traffic_by_keywords endpoint
- get category domain recommendations
    - will give out competitors and advise future positioning based on any particular catgory
- current analysis (gives competitors, keywords, categories, referring to-from)
    - https://docs.dataforseo.com/v3/traffic_analytics/similarweb/task_get/?python
    - have custom competitor sorting (make it look pretty)
- current category research reports
    = allow input for category and location --> compile data for competitors
'''
