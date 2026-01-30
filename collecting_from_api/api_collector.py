import requests
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

from utils.config import API_CONFIG

load_dotenv()

class APIDataCollector:
    def __init__(self, api_name: str):
        self.api_name = api_name
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'StudentCollector/1.0'
        })

    def get_base_url(self):
        return API_CONFIG[self.api_name]['base_url']

    def make_request(self, endpoint: str, params: dict):
        url = self.get_base_url() + endpoint
        response = self.session.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def save_to_csv(self, data, filename):
        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f'Данные сохранены в {filename}')

        
class NasaApodCollector(APIDataCollector):
    def __init__(self):
        super().__init__('nasa')

    def get_apod(self, count=5):
        params = {
            'api_key': os.getenv('NASA_API_KEY'),
            'count': count
        }

        data = self.make_request(
            API_CONFIG['nasa']['endpoints']['apod'],
            params
        )

        result = []
        for item in data:
            result.append({
                'date': item.get('date'),
                'title': item.get('title'),
                'explanation': item.get('explanation'),
                'media_type': item.get('media_type'),
                'url': item.get('url')
            })

        return result
