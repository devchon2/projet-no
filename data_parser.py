import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
from data_scraper import scrape_data, get_auction_data
from bs4 import BeautifulSoup
from data_visualizer import create_dashboard
from utils import save_data
import logging
from config import DATA_FILE
from scraper import get_html

# Initialisation des données
data = pd.DataFrame()

# Définition de l'URL pour scraper les données
# Lire l'URL à scraper à partir du fichier sites.txt
with open('data\input\sites.txt', 'r') as file:
    DATA_URL = file.readline().strip()

# Définition de l'intervalle de mise à jour automatique (en heures)
UPDATE_INTERVAL = 24

# Configuration des journaux
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('data_updater.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(file_handler)

from bs4 import BeautifulSoup
import pandas as pd

def parse_data(raw_data):
    # Extraire les données du contenu HTML
    print(raw_data)
    soup = BeautifulSoup(raw_data, 'html.parser', from_encoding='utf-8')
    
    # Trouver tous les conteneurs de lot
    lot_containers = soup.select('div.itemLot')
    
    # Liste pour stocker les données de chaque lot
    data = []
    
    # Parcourir chaque conteneur de lot
    for container in lot_containers:
        # Récupérer les informations pour chaque lot
        lot_number = container.select_one('div.text-h6').text.strip()
        lot_description = container.select_one('div.description.text-body-2').text.strip()
        lot_estimate = container.select_one('div.estimates').text.strip()
        lot_images = [img['src'] for img in container.select('div.sale-item__img')]
        
        # Ajouter les informations de chaque lot à la liste de données
        data.append({
            'lot_number': lot_number,
            'lot_description': lot_description,
            'lot_estimate': lot_estimate,
            'lot_images': lot_images
        })
    
    # Convertir la liste de dictionnaires en un DataFrame
    df = pd.DataFrame(data)
    
    # Retourner le DataFrame
    return df




def update_data():
    from scraper import get_html

    # Get auction data from scraper
    auction_data = get_auction_data()

    # Loop through auction data and scrape individual auction pages
    for d in auction_data:
        # Get HTML for auction page
        html_data = get_html(d['url'])

        # Skip to next iteration if html_data is None
        if html_data is None:
            logging.warning(f"No HTML data for {d['url']}")
            continue

        # Parse HTML data for auction
        parsed_data = parse_data(html_data)

        # Check if parsed_data is None before updating data
        if parsed_data is not None:
            # Update auction data with parsed data
            data.update(parsed_data)
        else:
            logging.warning(f"No parsed data for {d['url']}")

    # Output data to console
    print(data)


# Planification de la mise à jour automatique
scheduler = BlockingScheduler()
scheduler.add_job(update_data, 'interval', hours=UPDATE_INTERVAL)

if __name__ == '__main__':
    logging.info('Starting the data updater...')
    scheduler.start()
