# from currentsapi import CurrentsAPI
import requests
from dotenv import load_dotenv
import os

load_dotenv()


def fetch_latest_news(api_key, keyword=None, language='en', limit=10):
    if keyword:
        url = 'https://api.currentsapi.services/v1/search'
        params = {
            'apiKey': api_key,
            'language': language,
            'limit': limit,
            'keywords':
            keyword  # Exact match of words in the title or description
        }
    else:
        url = 'https://api.currentsapi.services/v1/latest-news'
        params = {'apiKey': api_key, 'language': language, 'limit': limit}
    print(f"Making request to {url} with params {params}")
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['news']
    else:
        print(f"Failed to fetch news: {response.status_code}, {response.text}")
        return None
