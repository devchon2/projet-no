import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def process_data(file_path):
    # Lire les données à partir du fichier CSV
    data = pd.read_csv(file_path)

    # Supprimer les colonnes inutiles
    data = data.drop(['id', 'Unnamed: 32'], axis=1)

    # Remplacer les valeurs manquantes par la moyenne de la colonne
    data = data.fillna(data.mean())

    # Convertir la colonne de classification en valeurs numériques
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

    # Séparer les données de classification des autres données
    y = data['diagnosis']
    X = data.drop('diagnosis', axis=1)

    # Normaliser les données en utilisant la moyenne et l'écart-type
    X = (X - X.mean()) / X.std()

    return X, y


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
