from flask import Flask, render_template
from config import Config

from models import Data
from views import home, data, stats, update
from utils import install_missing_packages
from data_scraper import get_auction_data
from data_analyzer import process_data
from data_visualizer import generate_charts, generate_dashboards
from data_updater import update_data
from backup import backup_data
from utils import add_entry_to_excel, delete_entry_from_excel, get_entry_by_id
from forms import AddForm, DeleteForm
import pandas as pd
from flask import render_template, request, redirect, url_for
from app import app

import logging

# Configuration du logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Exemple d'utilisation
logging.debug('Un message de debug')
logging.info('Un message d\'info')
logging.warning('Un message d\'avertissement')
logging.error('Un message d\'erreur')
logging.critical('Un message critique')

data_file_path = Config.DATA_FILE

app = Flask(__name__)
app.config.from_pyfile('config.py')


def load_data_from_excel():
    df = pd.read_excel(app.config['DATA_FILE'])
    return df.to_dict(orient='records')


@app.route('/')
def index():
    return home()


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm(request.form)
    if request.method == 'POST' and form.validate():
        data = {
            'id': form.id.data,
            'name': form.name.data,
            'description': form.description.data,
            'image': form.image.data
        }
        add_entry_to_excel(data, app.config['DATA_FILE'])
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteForm(request.form)
    form.entries.choices = [(entry['id'], entry['name']) for entry in load_data_from_excel()]
    if request.method == 'POST' and form.validate():
        entry_id = form.entries.data
        delete_entry_from_excel(entry_id, app.config['DATA_FILE'])
        return redirect(url_for('index'))
    return render_template('delete.html', form=form)


@app.route('/entry/<int:entry_id>')
def entry(entry_id):
    entry = get_entry_by_id(entry_id, app.config['DATA_FILE'])
    return render_template('entry.html', entry=entry)


@app.route('/data')
def get_data():
    return data()


@app.route('/stats')
def get_stats():
    return stats(data)


@app.route('/update')
def update_data_route():
    message = update_data(data)
    return render_template('update.html', message=message)


if __name__ == '__main__':
    # Mettre à jour les données automatiquement tous les jours
    update_data(data, daily=True)

    # Installer automatiquement les paquets manquants ou obsolètes
    install_missing_packages()

    # Extraire les données des sites web d'enchères
    auction_data = get_auction_data()

    # Traiter les données extraites
    processed_data = process_data(auction_data)

    # Générer les graphiques et les tableaux de bord pour la visualisation des données" :

if __name__ == '__main__':
    # Mettre à jour les données automatiquement tous les jours
    update_data(Data(app.config['DATA_FILE_PATH'])) 
    # Installer automatiquement les paquets manquants ou obsolètes
    install_missing_packages()
    # Extraire les données des sites web d'enchères
    auction_data = get_auction_data()
    # Traiter les données extraites
    processed_data = process_data(auction_data)
    # Générer les graphiques et les tableaux de bord pour la visualisation des données
    generate_charts(processed_data)
    generate_dashboards(processed_data)
    # Sauvegarder les données dans un fichier Excel
    backup_data(processed_data, data_file_path)
    # Démarrer l'application Flask
    app.run()