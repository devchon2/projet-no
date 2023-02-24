def create_user(user_data, users_file):
    """
    Crée un utilisateur en ajoutant les informations passées en paramètre dans le fichier `users_file`.
    """
    with open(users_file, "a") as file:
        file.write(",".join(user_data) + "\n")
