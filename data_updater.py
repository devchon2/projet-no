import pandas as pd
import os
from datetime import datetime
from data_visualizer import generate_charts, generate_dashboards


def load_data(file_path):
    """
    Charge les données à partir d'un fichier Excel.
    :param file_path: Le chemin du fichier Excel contenant les données.
    :return: Le DataFrame contenant les données.
    """
    # Vérifier que le fichier existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier '{file_path}' est introuvable.")

    # Charger les données à partir du fichier Excel
    df = pd.read_excel(file_path)

    return df


def clean_data(df):
    """
    Nettoie les données en supprimant les colonnes inutiles et les transactions en double.
    :param df: Le DataFrame contenant les données à nettoyer.
    :return: Le DataFrame nettoyé.
    """
    # Supprimer les colonnes inutiles
    df = df.drop(columns=['Transaction ID', 'Date'])

    # Supprimer les transactions en double
    df = df.drop_duplicates()

    return df


def update_data(file_path):
    """
    Charge et nettoie les données, génère des graphiques et des tableaux de bord, puis sauvegarde les résultats.
    :param file_path: Le chemin du fichier Excel contenant les données à mettre à jour.
    :return: None
    """
    # Charger les données
    data = load_data(file_path)

    # Nettoyer les données
    data = clean_data(data)

    # Générer des graphiques
    generate_charts(data)

    # Générer des tableaux de bord interactifs
    app = generate_dashboards(data)

    # Lancer l'application Dash
    app.run_server(debug=True, use_reloader=False)

    # Sauvegarder les résultats
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    data.to_excel(f'data_{timestamp}.xlsx', index=False)
