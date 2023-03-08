import requests
from bs4 import BeautifulSoup
import pandas as pd

# Liste des sites à analyser
sites = [
    {"url": "https://www.moniteurlive.com/c/225/son--image", "name": "son-image-monlive2"},
    {"url": "https://www.moniteurlive.com/c/226/informatique--bureautique", "name": "info-bureau-monlive2"},
    {"url": "https://www.interencheres.com/materiels-professionnels/materiels-professionnels/", "name": "inter2"},   # Ajouter d'autres sites ici
]

# Analyser chaque site
for site in sites:
    # Obtenir le contenu de la page
    response = requests.get(site["url"])
    html = response.content

    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Trouver tous les éléments HTML avec des classes ou des identifiants
    elements = soup.find_all(attrs={"class": True, "id": True})

    # Liste pour enregistrer les informations
    resultats = []

    # Ajouter les informations pour chaque élément à la liste
    for element in elements:
        # Ajouter toutes les classes de l'élément à la liste
        classes = element.get("class")
        if classes:
            for css_class in classes:
                # Trouver l'élément correspondant à la classe
                classe_element = soup.find(class_=css_class)
                if classe_element:
                    resultats.append({
                        "Classe/ID": css_class,
                        "Contenu HTML": classe_element.encode_contents()
                    })

        # Ajouter l'ID de l'élément à la liste
        element_id = element.get("id")
        if element_id:
            # Trouver l'élément correspondant à l'ID
            id_element = soup.find(id=element_id)
            if id_element:
                resultats.append({
                    "Classe/ID": element_id,
                    "Contenu HTML": id_element.encode_contents()
                })

    # Enregistrer les informations dans une feuille de calcul
    with pd.ExcelWriter("resultats.xlsx", mode="a") as writer:
        df = pd.DataFrame(resultats, columns=["Classe/ID", "Contenu HTML"])
        df.to_excel(writer, sheet_name=site["name"], index=False)
