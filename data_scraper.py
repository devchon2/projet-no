from selenium import webdriver
from time import sleep

from scraper import get_html
from data_parser import parse_data

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
