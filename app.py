import requests
from newsapi import NewsApiClient
import logging
API_KEY = ''
from datetime import datetime, timedelta


class Pipeline:
    def __init__(self):
        self.author = "Jaskirat Singh Sra"
        self.age = 12
        self.news_client = NewsApiClient(api_key=API_KEY)

    def get_headlines(self):
        start_date = datetime.now() - timedelta(minutes=1)
        end_date = datetime.now()
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')
        articles = self.news_client.get_everything(q='Google',
                                                        from_param=start_date,
                                                        to=end_date,
                                                        language='en',
                                                        sort_by='relevancy',
                                                        page=2)
        print("Total articles %s fetched in this run." % (articles['totalResults']))
        return articles

    def run(self):
        articles = self.get_headlines()


obj = Pipeline()

obj.run()
