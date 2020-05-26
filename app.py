import requests
from newsapi import NewsApiClient
import logging
from time import sleep
import os
import sys

API_KEY = ''
from datetime import datetime, timedelta, timezone


class Pipeline:
    def __init__(self):
        self.author = "Jaskirat Singh Sra"
        self.age = 12
        self.news_client = NewsApiClient(api_key=API_KEY)

    def get_headlines(self):
        start_date = datetime.now() - timedelta(minutes=15)
        end_date = datetime.now()
        start_date = start_date.replace(tzinfo=timezone.utc).timestamp()
        end_date = end_date.replace(tzinfo=timezone.utc).timestamp()
        print("Fetching articles from News API")
        articles = self.news_client.get_everything(q='Google',
                                                   from_param=start_date,
                                                   to=end_date,
                                                   language='en',
                                                   sort_by='relevancy',
                                                   page=2)
        print("Total articles %s fetched in this run." % (articles['totalResults']))
        return articles

    def run(self):
        while True:
            articles = self.get_headlines()
            sleep(60)


if __name__ == '__main__':
    controller = Pipeline()
    controller.run()
