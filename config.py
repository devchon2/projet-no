import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG', False)

    # Data settings
    # Ajouter une variable DATA_FILE pour stocker le chemin vers le fichier Excel.
    DATA_FILE = "data.xlsx"
    BACKUP_FOLDER = os.environ.get('BACKUP_FOLDER', '/path/to/backup/folder/')
    BACKUP_INTERVAL = os.environ.get('BACKUP_INTERVAL', 24)
    MIN_SLEEP = os.environ.get('MIN_SLEEP', 1)
    MAX_SLEEP = os.environ.get('MAX_SLEEP', 5)

    # Scraper settings
    API_KEY = os.environ.get('API_KEY', 'your_api_key_here')

    # Database settings
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    DB_NAME = os.environ.get('DB_NAME', 'mydatabase')
    DB_USER = os.environ.get('DB_USER', 'mydatabaseuser')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'mypassword')
