import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
from data_scraper import scrape_data,get_auction_data
from data_parser import parse_data
from data_visualizer import create_dashboard
from utils import save_data
import logging
from config import DATA_FILE
from scraper import get_html
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Définition de l'URL pour scraper les données
# Lire l'URL à scraper à partir du fichier sites.txt
with open('data\input\sites.txt', 'r') as file:
    DATA_URL = file.readline().strip()

# Définition de l'intervalle de mise à jour automatique (en heures)
UPDATE_INTERVAL = 24

# Initialisation des données
data = pd.DataFrame()

def update_data():
    # Get auction data from scraper
    auction_data = get_auction_data()

    # Loop through auction data and scrape individual auction pages
    for data in auction_data:
        # Get HTML for auction page
        html_data = get_html(data['url'])

        # Skip to next iteration if html_data is None
        if html_data is None:
            print("Pas de donnée!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            continue

        # Parse HTML data for auction
        parsed_data = parse_data(html_data)
        print(parsed_data)
        # Update auction data with parsed data
        data.update(parsed_data)

        # Output data to console
        print(data)



# Planification de la mise à jour automatique
scheduler = BlockingScheduler()
scheduler.add_job(update_data, 'interval', hours=UPDATE_INTERVAL)

if __name__ == '__main__':
    logging.info('Starting the data updater...')
    scheduler.start()
