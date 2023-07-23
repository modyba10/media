import requests

def create_nautobot_resource(url_suffix, data):

    token = "0123456789abcdef0123456789abcdef01234567"
    base_url = "http://nautobot.qa.tvvideoms.com/api/ipam/"
    url = base_url + url_suffix

    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Ressource créée avec succès. URL de la ressource : {response.json()['url']}")
    else:
        print(f"Échec de la création de la ressource. Code de réponse : {response.status_code}")
        print(response.text)  # Affiche le message d'erreur retourné par l'API en cas d'échec
