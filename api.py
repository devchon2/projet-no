import boto3
import config
from config import Config 
#from ebaysdk import Connection as Finding


def search_product_info():
     # Charger les adresses des sites témoins depuis le fichier
    with open("data/input/sites-temoins.txt") as f:
        site_urls = [line.strip() for line in f.readlines()]

    # Afficher les adresses des sites témoins
    print("Sites témoins :")
    for site_url in site_urls:
        print(site_url)
    """
    API_KEY_AMAZON = Config.API_KEY_AMAZON
    API_SECRET_AMAZON = Config.API_SECRET_AMAZON
    API_COLLAB_TAG = Config.ASSOCIATE_TAG
    API_KEY_EBAY = Config.API_KEY_EBAY

    # Créer une connexion à l'API Amazon Product Advertising
    amazon_api = boto3.client('apai', region_name='us-west-2', aws_access_key_id=API_KEY_AMAZON, aws_secret_access_key=API_SECRET_AMAZON, aws_associate_tag=ASSOCIATE_TAG)

    # Définir les paramètres de recherche
    keywords = 'laptop'
    search_params = {'Keywords': keywords, 'ResponseGroup': 'ItemAttributes,Offers'}

    # Appeler l'API Amazon Product Advertising pour récupérer les informations de produit
    response = amazon_api.call('ItemSearch', **search_params)

    # Extraire les données de la réponse
    item = response['Items']['Item'][0]
    title = item['ItemAttributes']['Title']
    price = item['OfferSummary']['LowestNewPrice']['FormattedPrice']
    url = item['DetailPageURL']

    # Afficher les données
    print(f'Title: {title}, Price: {price}, URL: {url}')
    
    # Définir la clé API eBay
    api_key = API_KEY_EBAY

    # Créer une connexion à l'API eBay
    ebay_api = Finding(appid=API_KEY_EBAY, config_file=None)

    # Définir les paramètres de recherche
    keywords = 'laptop'
    search_params = {'keywords': keywords, 'outputSelector': 'SellerInfo'}

    # Appeler l'API eBay pour récupérer les informations d'enchère
    response = ebay_api.execute('findItemsByKeywords', search_params)

    # Extraire les données de la réponse
    item = response.reply.searchResult.item[0]
    title = item.title
    price = item.sellingStatus.currentPrice.value
    seller = item.sellerInfo.sellerUserName

    # Afficher les données
    print(f'Title: {title}, Price: {price}, Seller: {seller}')
    """