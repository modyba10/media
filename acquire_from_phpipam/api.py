import requests
import json

def acquire_data(path):
    # URL de l'API
    base_url = "https://phpipam.inf.tvvideoms.com/api/ansible/"
    headers = {'token': 'JWzsEm8LBnAm1K4DJ3lCvw9SXjU0iY_d'}

    try:
        # Envoi de la requête à l'API avec le bon chemin
        response = requests.get(base_url + path, headers=headers)

        # Vérification du code de statut de la réponse
        if response.status_code == 200:
            data = response.json()
            data = data["data"]

            # Return indented JSON string
            return data

        else:
            print("La requête a retourné un code d'erreur :", response.status_code)
            return None

    except requests.RequestException as e:
        print("Une erreur de requête s'est produite :", e)
        return None
    
