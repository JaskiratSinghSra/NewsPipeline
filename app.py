import requests
from newsapi import NewsApiClient
import logging
from time import sleep
import os
import sys

API_KEY = '8e762f6fc7634b1a8268c27ea76a3a7f'
from datetime import datetime, timedelta, timezone
FORMAT = '[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s %(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class Pipeline:
    def __init__(self):
        self.author = "Jaskirat Singh Sra"
        self.age = 12
        self.news_client = NewsApiClient(api_key=API_KEY)

    def get_articles(self):
        start_date = datetime.now() - timedelta(minutes=15)
        end_date = datetime.now()
        start_date = start_date.replace(tzinfo=timezone.utc).timestamp()
        end_date = end_date.replace(tzinfo=timezone.utc).timestamp()
        logging.info("Fetching articles from News API")
        articles = self.news_client.get_everything(q='Google',
                                                   from_param=start_date,
                                                   to=end_date,
                                                   language='en',
                                                   sort_by='relevancy',
                                                   page=2)
        logging.info("Total articles %s fetched in this run." % (articles['totalResults']))
        return articles

    def run(self):
        while True:
            articles = self.get_articles()
            sleep(60)


if __name__ == '__main__':
    controller = Pipeline()
    controller.run()
