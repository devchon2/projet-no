import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
from data_scraper import scrape_data
from data_parser import parse_data
from data_visualizer import create_dashboard
from utils import save_data_to_file
from apscheduler.schedulers.blocking import BlockingScheduler
from data_scraper import scrape_data
from data_parser import parse_data
from data_visualizer import create_dashboard
from utils import save_data_to_file

# Définition de l'URL pour scraper les données
# Lire l'URL à scraper à partir du fichier sites.txt
with open('data\input\sites.txt', 'r') as file:
    DATA_URL = file.readline().strip()

# Définition de l'intervalle de mise à jour automatique (en heures)
UPDATE_INTERVAL = 24
# Définition de l'intervalle de mise à jour automatique (en heures)
UPDATE_INTERVAL = 24

# Initialisation des données
data = pd.DataFrame()
# Initialisation des données
data = pd.DataFrame()

def update_data():
    global data
    # Scraper les données
    html_data = scrape_data(DATA_URL)
    # Parser les données
    parsed_data = parse_data(html_data)
    # Vérifier si de nouvelles données ont été récupérées
    if not parsed_data.empty and not parsed_data.equals(data):
        # Mettre à jour les données
        data = parsed_data
        # Créer un dashboard
        create_dashboard(data)
        # Sauvegarder les données
        save_data_to_file(data, 'data.csv')
        print('Data updated successfully')
    else:
        print('No new data available')
def update_data():
    global data
    # Scraper les données
    html_data = scrape_data(DATA_URL)
    # Parser les données
    parsed_data = parse_data(html_data)
    # Vérifier si de nouvelles données ont été récupérées
    if not parsed_data.empty and not parsed_data.equals(data):
        # Mettre à jour les données
        data = parsed_data
        # Créer un dashboard
        create_dashboard(data)
        # Sauvegarder les données
        save_data_to_file(data, 'data.csv')
        print('Data updated successfully')
    else:
        print('No new data available')

# Planification de la mise à jour automatique
scheduler = BlockingScheduler()
scheduler.add_job(update_data, 'interval', hours=UPDATE_INTERVAL)
# Planification de la mise à jour automatique
scheduler = BlockingScheduler()
scheduler.add_job(update_data, 'interval', hours=UPDATE_INTERVAL)

if __name__ == '__main__':
    scheduler.start()
if __name__ == '__main__':
    scheduler.start()
