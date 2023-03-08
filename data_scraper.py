import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from fake_useragent import UserAgent
from random import randint

def get_auction_data():
    # Read urls from sites.txt file
    with open('./data/input/sites.txt', 'r') as f:
        urls = f.readlines()
    # Remove newline characters
    urls = [url.strip() for url in urls]

    # Initialize list to store data for all auctions
    auction_data = []

    # Set up undetected Chromedriver
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    # Set up proxies
    proxies = {
        'http': '162.243.118.179:3128',
        
    }

    # Loop through urls and scrape data
    for url in urls:
        data = scrape_data(url, proxies)
        auction_data.append(data)
        sleep(randint(3, 10)) # Add random delay between requests to avoid detection

    # Close Chromedriver
    driver.quit()

    return auction_data


def scrape_data(url, proxies):
    # Set up headers with random user-agent
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    # Set up session with random cookies
    session = requests.Session()
    session.cookies.update({'cookie1': 'value1', 'cookie2': 'value2'})

    # Get HTML content of page with proxies, headers and cookies
    r = session.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Scrape data from page
    name = soup.find('.item p').text
    status = soup.find('div', {'class': 'status'}).text
    lot_titles = [title.text for title in soup.find_all('div', {'class': 'title'})]
    lot_descriptions = [description.text for description in soup.find_all('div', {'class': 'description'})]
    lot_images = [image['src'] for image in soup.find_all('img', {'class': 'lot-image'})]

    # Store data in dictionary
    data= {
        'url': url,
        'name': name,
        'status': status,
        'lot_titles': lot_titles,
        'lot_descriptions': lot_descriptions,
        'lot_images': lot_images
    }
    return data
