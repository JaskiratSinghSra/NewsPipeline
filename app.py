import requests
from newsapi import NewsApiClient
API_KEY = ''


class Pipeline:
    def __init__(self):
        self.author = "jaskirat"
        self.age = 12
        self.news_client = NewsApiClient(api_key=API_KEY)

    def get_headlines(self):
        top_headlines = self.news_client.get_top_headlines(q='bitcoin',
                                                           category='business',
                                                           language='en',
                                                           country='us')
        titles = []
        for headline in top_headlines['articles']:
            titles.append(headline['title'])

        return top_headlines

    def run(self):
        articles = self.get_headlines()


obj = Pipeline()

obj.run()
