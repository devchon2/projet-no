import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import dash


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import dash

from dash import html,dcc

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def create_dashboard(data):
    """
    Génère un tableau de bord interactif pour visualiser les données de transactions.
    :param data: Le DataFrame contenant les données à visualiser.
    :return: L'objet Dash qui contient le tableau de bord.
    """
    # Générer des graphiques à partir des données
    generate_charts(data)

    # Créer l'application Dash
    app = dash.Dash(__name__)

    # Créer une mise en page simple
    app.layout = html.Div([
        html.H1('Visualisation des données de transactions'),
        dcc.Graph(
            id='montants-histogram',
            figure={
                'data': [{
                    'x': data['Amount'],
                    'type': 'histogram'
                }],
                'layout': {
                    'title': 'Distribution des montants'
                }
            }
        ),
        dcc.Graph(
            id='type-de-carte-bar',
            figure={
                'data': [{
                    'x': data['Card Type'],
                    'type': 'histogram'
                }],
                'layout': {
                    'title': 'Nombre de transactions par type de carte'
                }
            }
        ),
        dcc.Graph(
            id='transactions-par-pays-pie',
            figure=px.pie(data.groupby(['Country'])['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False).head(10), values='Amount', names='Country', title='Répartition des transactions par pays (Top 10)')
        )
    ])

    return app

def generate_charts(data):
    """
    Génère des graphiques à partir des données.
    :param data: Le DataFrame contenant les données à visualiser.
    :return: None
    """
    # Générer un histogramme pour visualiser la distribution des montants
    plt.figure(figsize=(8, 6))
    sns.histplot(data=data, x='Amount', kde=True, bins=20)
    plt.title('Distribution des montants')
    plt.savefig('montants.png', dpi=300)
    plt.close()

    # Générer un graphique à barres pour visualiser le nombre de transactions par type de carte
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='Card Type')
    plt.title('Nombre de transactions par type de carte')
    plt.savefig('type_de_carte.png', dpi=300)
    plt.close()

    # Générer un diagramme circulaire pour visualiser la répartition des transactions par pays
    data_by_country = data.groupby(['Country'])['Amount'].sum().reset_index()
    data_by_country = data_by_country.sort_values(by='Amount', ascending=False).head(10)
    fig = px.pie(data_by_country, values='Amount', names='Country')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(title='Répartition des transactions par pays (Top 10)')
    fig.write_image('transactions_par_pays.png', engine='kaleido')
    plt.close()

def generate_charts(data):
    """
    Génère des graphiques à partir des données.
    :param data: Le DataFrame contenant les données à visualiser.
    :return: None
    """
    # Générer un histogramme pour visualiser la distribution des montants
    plt.figure(figsize=(8, 6))
    sns.histplot(data=data, x='Amount', kde=True, bins=20)
    plt.title('Distribution des montants')
    plt.savefig('montants.png', dpi=300)
    plt.close()

    # Générer un graphique à barres pour visualiser le nombre de transactions par type de carte
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='Card Type')
    plt.title('Nombre de transactions par type de carte')
    plt.savefig('type_de_carte.png', dpi=300)
    plt.close()

    # Générer un diagramme circulaire pour visualiser la répartition des transactions par pays
    data_by_country = data.groupby(['Country'])['Amount'].sum().reset_index()
    data_by_country = data_by_country.sort_values(by='Amount', ascending=False).head(10)
    fig = px.pie(data_by_country, values='Amount', names='Country')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(title='Répartition des transactions par pays (Top 10)')
    fig.write_image('transactions_par_pays.png', engine='kaleido')
    plt.close()


def generate_dashboards(data):
    """
    Génère des tableaux de bord interactifs à partir des données.
    :param data: Le DataFrame contenant les données à visualiser.
    :return: L'objet Dash qui contient les tableaux de bord.
    """
    # Créer l'application Dash
    app = dash.Dash(__name__)

    # Créer une mise en page simple
    app.layout = html.Div([
        html.H1('Visualisation des données de transactions'),
        dcc.Graph(
            id='montants-histogram',
            figure={
                'data': [{
                    'x': data['Amount'],
                    'type': 'histogram'
                }],
                'layout': {
                    'title': 'Distribution des montants'
                }
            }
        ),
        dcc.Graph(
            id='type-de-carte-bar',
            figure={
                'data': [{
                    'x': data['Card Type'],
                    'type': 'histogram'
                }],
                'layout': {
                    'title': 'Nombre de transactions par type de carte'
                }
            }
        ),
        dcc.Graph(
            id='transactions-par-pays-pie',
            figure=px.pie(data.groupby(['Country'])['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False).head(10), values='Amount', names='Country', title='Répartition des transactions par pays (Top 10)')
        )
    ])

    return app
