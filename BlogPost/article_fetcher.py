import requests


class ArticleFetcher:
    def __init__(self):
        pass

    def get_devto_articles(self):
        url = "https://dev.to/api/articles?tag=programming"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return []

    def aggregate_articles(self):
        articles = self.get_devto_articles()


        return articles
