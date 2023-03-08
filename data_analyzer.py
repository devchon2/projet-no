import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
from config import DATA_FILE
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from data_parser import parse_data


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def process_data(raw_data):
    # Parse the raw data into a DataFrame
    df = parse_data(raw_data)
    
    # Convert the estimate column to a float
    if 'lot_estimate' in df.columns and isinstance(df['lot_estimate'], str):
        df['lot_estimate'] = df['lot_estimate'].str.replace(',', '').str.extract(r'(\d+\.?\d*)', expand=False).astype(float)
    else:
        print("'lot_estimate' column not found in data or not of type 'str'")
    
    # Return the processed DataFrame
    return df



def train_model(X, y):
    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner le modèle de régression logistique
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)

    # Prédire les étiquettes pour les données de test
    y_pred = lr_model.predict(X_test)

    # Calculer la précision du modèle
    accuracy = accuracy_score(y_test, y_pred)

    return lr_model, accuracy


def classify_auction_data(file_path):
    # Prétraiter les données
    X, y = process_data(file_path)

    # Entraîner le modèle
    lr_model, accuracy = train_model(X, y)

    # Renvoyer le modèle entraîné et sa précision
    return lr_model, accuracy



def generate_statistics(X, y):
    # Générer des statistiques sur les données
    num_instances, num_features = X.shape
    num_benign = np.sum(y == 0)
    num_malignant = np.sum(y == 1)

    print(f"Nombre total d\'instances : {num_instances}")
    print(f'Nombre total de fonctionnalités : {num_features}')
    print(f'Nombre de cas bénins : {num_benign}')
    print(f'Nombre de cas malins : {num_malignant}')


def generate_visualizations(X, y):
    # Générer des graphiques pour visualiser les données
    num_instances, num_features = X.shape
    num_benign = np.sum(y == 0)
    num_malignant = np.sum(y == 1)

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].pie([num_benign, num_malignant], labels=['Bénin', 'Malin'], autopct='%1.1f%%', startangle=90)
    axs[0].axis('equal')
    axs[0].set_title('Répartition des cas bénins et malins')

    axs[1].scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap=plt.cm.coolwarm)
    axs[1].set_xlabel('Radius Mean')
    axs[1].set_ylabel('Texture Mean')
    axs[1].set_title('Répartition des cas bénins et malins selon les fonctionnalités Radius Mean et Texture Mean')

    plt.show()
