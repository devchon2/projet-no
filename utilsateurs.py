def create_user(user_data, users_file):
    """
    Crée un utilisateur en ajoutant les informations passées en paramètre dans le fichier `users_file`.
    """
    with open(users_file, "a") as file:
        file.write(",".join(user_data) + "\n")

def get_user(username, users_file):
    """
    Récupère les informations de l'utilisateur correspondant au nom d'utilisateur `username` dans le fichier `users_file`.
    Retourne un dictionnaire avec les informations de l'utilisateur ou None si l'utilisateur n'existe pas.
    """
    with open(users_file, "r") as file:
        for line in file:
            user_info = line.strip().split(",")
            if user_info[0] == username:
                return {"username": user_info[0], "password": user_info[1]}
    return None