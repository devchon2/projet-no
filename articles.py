from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
import os


def create_article(article_data, articles_file):
    """
    Crée un article en ajoutant les informations passées en paramètre dans le fichier `articles_file`.
    """
    with open(articles_file, "a") as file:
        file.write(",".join(article_data) + "\n")

def get_articles(articles_file):
    """
    Récupère tous les articles stockés dans le fichier `articles_file`.
    Retourne une liste d'articles, chaque article étant représenté par un dictionnaire contenant son titre et son contenu.
    """
    articles = []
    with open(articles_file, "r") as file:
        for line in file:
            article_info = line.strip().split(",")
            articles.append({"title": article_info[0], "content": article_info[1]})
    return articles

def get_prediction(title, content, model):
    """
    Utilise le modèle de prédiction passé en paramètre pour faire une prédiction sur l'article avec le titre et le contenu passés en paramètre.
    Retourne le label de la prédiction.
    """
    article_text = f"{title} {content}"
    prediction = model.predict([article_text])[0]
    return prediction

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Charger le modèle entraîné
    model = joblib.load(os.path.join("model", "model.joblib"))

    # Charger le vecteuriseur de texte
    vectorizer = joblib.load(os.path.join("model", "vectorizer.joblib"))

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/predict', methods=['POST'])
    def predict():
        # Récupérer les données du formulaire
        data = request.form['data']

        # Prétraitement du texte
        data = data.lower()
        data = [data]
        data = vectorizer.transform(data).toarray()

        # Faire la prédiction
        prediction = model.predict(data)

        # Renvoyer la réponse en format JSON
        return jsonify({'result': int(prediction[0])})

    @app.route('/predict_file', methods=['POST'])
    def predict_file():
        # Récupérer le fichier de données
        data = pd.read_excel(request.files.get('file'))

        # Prétraitement du texte
        data = data['description'].apply(lambda x: x.lower())
        data = vectorizer.transform(data).toarray()

        # Faire la prédiction
        prediction = model.predict(data)

        # Ajouter la colonne de prédictions au DataFrame original
        data['category'] = prediction

        # Convertir le DataFrame en dictionnaire
        data_dict = data.to_dict(orient='records')

        # Renvoyer la réponse en format JSON
        return jsonify({'result': data_dict})

    return app
