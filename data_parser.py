from bs4 import BeautifulSoup
import pandas as pd

def parse_data(raw_data):
    soup = BeautifulSoup(raw_data, 'html.parser')
    # code to extract data from html using BeautifulSoup
    # ...
    # return data as a Pandas DataFrame
    data = pd.DataFrame(...)
    return data
