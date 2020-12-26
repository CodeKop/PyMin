import requests

class UrlData:
    def __init__(self, name: str, base_url: str, sub_urls: dict):
        self.name = name
        self.base_url = base_url
        self.sub_urls = sub_urls

    def build():
        pass

class Scraper:
    def __init__(self, url_data: UrlData):
        self.url_data = url_data

    def home():
        results_data = {}

        # Firstly, retrieve page from provided website.
        # NOTE: Building this specifically for soap2day, will have to make ti generic.
        

        # First collect  home movies.
        results_data["movies"] = []
        results_data["tvseries"] = []