import pandas as pd
import requests
import json
import time
import subprocess
import sys
import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from utils import check_package, save_data

if check_package('anticaptchaofficial'):
    import anticaptchaofficial
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class SaleItemSpider(scrapy.Spider):
    name = "SaleItemSpider"
    start_urls = []
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/58.0.3029.110 Safari/537.36'
    }
    selectors = []

    def __init__(self, start_urls, selectors, *args, **kwargs):
        super(SaleItemSpider, self).__init__(*args, **kwargs)
        self.start_urls = start_urls
        self.selectors = selectors

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        for selector in self.selectors:
            items = soup.select(selector)
            data = []
            for item in items:
                cols = [ele.text.strip() for ele in item.find_all('td')]
                data.append(cols)
            df = pd.DataFrame(data, columns=['Auction Name', 'Auction ID', 'Start Time', 'End Time', 'Current Bid', 'Location', 'Link'])
            yield df


def scrape_data(url, selectors=None):
    if selectors is None:
        selectors = [".item"]
    driver = webdriver.Chrome()
    if 'google.com/recaptcha/' in url:
        captcha_text = solve_captcha(driver)
        html = get_html(url, captcha_text=captcha_text)
    else:
        html = get_html(url)
    driver.quit()
    save_data(html, 'output.html')
    process = CrawlerProcess()
    process.crawl(SaleItemSpider, start_urls=[url], selectors=selectors)
    process.start()


def get_html(url, captcha_text=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/58.0.3029.110 Safari/537.36',
        'Referer': url
    }
    if captcha_text:
        cookies = requests.get(url).text
        captcha_id = cookies.split(';')[1]
        captcha_answer = requests.get(f'http://api.anti-captcha.com/getTaskResult?taskId={captcha_id}&retry=0').text
        while 'CAPCHA_NOT_READY' in captcha_answer:
            time.sleep(5)
            captcha_answer = requests.get(f'http://api.anti-captcha.com/getTaskResult?taskId={captcha_id}&retry=0').text
        captcha_token = captcha_answer.split(':')[1].replace('"', '').replace('}', '')
        r = requests.get(f'{url}&g-recaptcha-response={captcha_token}', headers=headers)
        return r.text
    else:
        r = requests.get(url, headers=headers)
        return r.text


def solve_captcha(driver):
    task = anticaptchaofficial.ImageToTextTask(image_url=get_image_path(driver))
    captcha_text = task.solve()
    return captcha_text


def get_image_path(driver):
    driver.get('https://www.google.com/recaptcha/api2/demo')
    frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
    driver.switch_to.frame(frame)
    image_element = driver.find_element_by_xpath('//img[contains(@src, "data:image")]')
    image_url = image_element.get_attribute('src')
    return image_url
