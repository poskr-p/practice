import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import os

class AutoRuParser:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def parse_cars(self, url):
        self.driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        cars = soup.find_all('div', {'data-testid': 'listing-item'})

        result = []

        for car in cars:
            try:
                title = car.find('h3').text.strip()
                price = car.find('span', {'data-testid': 'price'}).text.strip()

                result.append({
                    'title': title,
                    'price': price
                })
            except:
                continue

        return result

    def close(self):
        self.driver.quit()
