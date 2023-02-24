import os
import sys
import time
import config
import random
import data_parser
import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd
from python_anticaptcha import AnticaptchaClient, ImageToTextTask


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path='chromedriver')

# Anti-captcha settings
api_key = 'your-key-here'
client = AnticaptchaClient(api_key)
solver = ImageToTextTask(client)

import requests
