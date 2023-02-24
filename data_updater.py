import pandas as pd
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

from apscheduler.schedulers.blocking import BlockingScheduler
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

from data_scraper import scrape_data
#DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

from data_parser import parse_data
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

from data_visualizer import create_dashboard
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

from utils import save_data_to_file
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 


# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

# Définition de l'URL pour scraper les données
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

DATA_URL = 'https://example.com'
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 


# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

# Définition de l'intervalle de mise à jour automatique (en heures)
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

UPDATE_INTERVAL = 24
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 


# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

# Initialisation des données
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

data = pd.DataFrame()
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 


# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

def update_data():
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

    global data
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

    # Scraper les données
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

    html_data = scrape_data(DATA_URL)
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

    # Parser les données
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

    parsed_data = parse_data(html_data)
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

    # Vérifier si de nouvelles données ont été récupérées
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

    if not parsed_data.empty and not parsed_data.equals(data):
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

        # Mettre à jour les données
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

        data = parsed_data
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

        # Créer un dashboard
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

        create_dashboard(data)
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

        # Sauvegarder les données
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

        save_data_to_file(data, 'data.csv')
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

        print('Data updated successfully')
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

    else:
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

        print('No new data available')
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 


# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

# Planification de la mise à jour automatique
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

scheduler = BlockingScheduler()
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

scheduler.add_job(update_data, 'interval', hours=UPDATE_INTERVAL)
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 


# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

if __name__ == '__main__':
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

    scheduler.start()
# DEBUG J:\Synochro\DEV\Projets perso\projet no\projet-no\data_updater.py: ligne 

