import pandas as pd
from openpyxl import load_workbook

import subprocess

import boto3
import config
from config import Config


def install_missing_packages():
    """
    Installe automatiquement les paquets manquants ou obsolètes.
    """
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])


def update_data(data):
    """
    Met à jour les données à partir des sites web d'enchères et les sauvegarde dans un fichier Excel.

    Args:
        data (Data): Les données à mettre à jour.
    """
    # Extraire les données des sites web d'enchères
    ebay_data = get_ebay_data()
    amazon_data = get_amazon_data()

    # Fusionner les données
    merged_data = merge_data(amazon_data, ebay_data)

    # Ajouter les nouvelles données au fichier Excel
    for entry in merged_data:
        existing_entry = data.df.loc[data.df['id'] == entry['id']]
        if len(existing_entry) > 0:
            data.df.loc[existing_entry.index[0]] = entry
        else:
            data.df = data.df.append(entry, ignore_index=True)
    data.df.to_excel('data/produits.xlsx', index=False)


def get_amazon_data():
    """
    Récupère les données des produits à partir de l'API Amazon Product Advertising.

    Returns:
        list: Les données des produits.
    """
    api_key = Config.API_KEY_AMAZON
    api_secret = Config.API_SECRET_AMAZON
    api_tag = Config.ASSOCIATE_TAG

    amazon_api = boto3.client('apai', region_name='us-west-2', aws_access_key_id=api_key, aws_secret_access_key=api_secret, aws_associate_tag=api_tag)

   
    keywords = 'laptop'
    search_params = {'Keywords': keywords, 'ResponseGroup': 'ItemAttributes,Offers'}

    # Appeler l'API Amazon Product Advertising pour récupérer les informations de produit
    response = amazon_api.call('ItemSearch', **search_params)

    # Extraire les données de la réponse
    item = response['Items']['Item'][0]
    title = item['ItemAttributes']['Title']
    price = item['OfferSummary']['LowestNewPrice']['FormattedPrice']
    url = item['DetailPageURL']

    # Organiser les données dans un dictionnaire
    data = {'id': 'A' + str(uuid.uuid4()), 'name': title, 'description': '', 'price': price, 'url': url}

    return [data]
    
