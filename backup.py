import os
import pandas as pd
from datetime import datetime
import openpyxl

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



# Définition du dossier de sauvegarde
BACKUP_DIR = '/path/to/backup/folder/'


def backup_data(data):
    """
    Sauvegarde les données dans un fichier Excel dans un dossier de sauvegarde.
    Le nom du fichier est généré en fonction de la date et de l'heure courante.
    """
    # Générer le nom de fichier basé sur la date et l'heure actuelles
    filename = 'data_backup_{}.xlsx'.format(
        datetime.now().strftime('%Y%m%d_%H%M%S'))

    # Créer un DataFrame Pandas à partir des données
    df = pd.DataFrame(data)

    # Sauvegarder les données dans un fichier Excel
    backup_path = os.path.join(BACKUP_DIR, filename)
    writer = pd.ExcelWriter(backup_path, engine='openpyxl')
    try:
        writer.book = openpyxl.load_workbook(backup_path)
        writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
    except FileNotFoundError:
        pass
    df.to_excel(writer, index=False, sheet_name='data')
    writer.save()
