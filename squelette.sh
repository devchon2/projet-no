#mkdir -p app data/{input,output} logs static/{css,js} templates tests venv && 
#touch app/{__init__,config,models,scraper,stats,views}.py data/input/sites.txt data/output/stats.csv logs/{access,error}.log static/css/style.css static/js/script.js templates/{base,dashboard}.html tests/__init__.py venv/.gitignore README.md requirements.txt main.py && 
#echo import os install infrastructure

#
# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)
er.py && 
echo import os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)
ts.py && 
echo import os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)
sites web enregistrés dans le fichier sites.txt\n\tType de données retourné : pandas.DataFrame\n\tstats(): renvoie un objet Pandas DataFrame contenant les statistiques calculées à partir des données extraites\n\tType de données retourné : pandas.DataFrame\n\tupdate(): met à jour les données extraites à partir des sites web enregistrés dans le fichier sites.txt et les sauvegarde dans un fichier CSV\n\tType de données retourné : None" > app/views.py && 
echo import os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)
 && 
echo import os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)
py && 
echo import os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)
 data_analyzer.py && 
echo import os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)

echo import os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)

echo import os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)

    cimport os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)

    Timport os

# Liste des modules à importer pour chaque fichier
modules = {
    'scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'stats.py': ['pandas'],
    'views.py': ['pandas', 'flask'],
    'utils.py': ['pandas'],
    'main.py': ['flask'],
    'data_scraper.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'data_parser.py': ['pandas'],
    'data_analyzer.py': ['pandas'],
    'data_visualizer.py': ['pandas', 'matplotlib'],
    'data_updater.py': ['pandas', 'selenium', 'requests', 'json', 'anticaptchaofficial'],
    'dashboard.py': ['pandas', 'dash', 'dash_core_components', 'dash_html_components', 'plotly.graph_objs']
}

# Parcourt chaque fichier et ajoute l'importation des modules en début de fichier
for filename in modules.keys():
    with open(filename, 'r+') as f:
        content = f.read()
        for module in modules[filename]:
            if module not in content:
                f.seek(0, 0)
                f.write("import " + module + "\n" + content)


