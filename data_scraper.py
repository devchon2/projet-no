from selenium import webdriver
from time import sleep

from scraper import get_html
from data_parser import parse_data

from scraper import get_html
from bs4 import BeautifulSoup


def get_auction_data():
    # lire les urls à partir du fichier sites.url
    with open('sites.url', 'r') as f:
        urls = f.readlines()
    urls = [url.strip() for url in urls]  # supprimer les caractères de saut de ligne

    # initialiser la liste pour stocker les données de toutes les enchères
    auction_data = []

    # boucle sur les urls et scraper les données
    for url in urls:
        data = get_html(url)
        # extraire les données de l'enchère à partir du html
        # ajouter les données à la liste d'enchères
        auction_data.append(data)
    
    return auction_data


def scrape_data(url):
    # Set up Selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # Wait for page to load
    sleep(5)
    
    # Get page source
    html = driver.page_source
    
    # Close Selenium webdriver
    driver.quit()
    
    # Parse data
    parsed_data = parse_data(html)
    
    return parsed_data
