import pandas as pd

class Data:
    """
    Classe pour stocker et traiter les données des enchères.
    """

    def __init__(self, data_file='data.csv'):
        """
        Initialise un objet Data à partir d'un fichier CSV.

        Args:
            data_file (str): Le nom du fichier contenant les données.
        """
        self.data_file = data_file
        self.df = pd.read_csv(data_file)

    def get_data(self):
        """
        Retourne les données stockées dans l'objet.

        Returns:
            pandas.DataFrame: Les données stockées dans l'objet.
        """
        return self.df

    def update_data(self, new_data):
        """
        Met à jour les données stockées dans l'objet avec de nouvelles données.

        Args:
            new_data (pandas.DataFrame): Les nouvelles données à ajouter.
        """
        self.df = pd.concat([self.df, new_data])
        self.df.to_csv(self.data_file, index=False)

    def filter_data(self, filters):
        """
        Filtre les données stockées dans l'objet selon les filtres spécifiés.

        Args:
            filters (dict): Un dictionnaire de filtres à appliquer aux données.

        Returns:
            pandas.DataFrame: Les données filtrées.
        """
        filtered_data = self.df
        for column, value in filters.items():
            filtered_data = filtered_data.loc[filtered_data[column] == value]
        return filtered_data

    def sort_data(self, column, ascending=True):
        """
        Trie les données stockées dans l'objet selon une colonne spécifiée.

        Args:
            column (str): Le nom de la colonne à utiliser pour le tri.
            ascending (bool): True si le tri doit être effectué dans l'ordre croissant, False sinon.

        Returns:
            pandas.DataFrame: Les données triées.
        """
        sorted_data = self.df.sort_values(column, ascending=ascending)
        return sorted_data

    def get_stats(self, column):
        """
        Retourne les statistiques descriptives pour une colonne spécifiée.

        Args:
            column (str): Le nom de la colonne pour laquelle calculer les statistiques.

        Returns:
            pandas.Series: Les statistiques descriptives pour la colonne spécifiée.
        """
        stats = self.df[column].describe()
        return stats
