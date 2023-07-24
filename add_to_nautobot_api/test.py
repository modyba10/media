import requests

def get_vlans():
    token = "0123456789abcdef0123456789abcdef01234567"
    base_url = "http://nautobot.qa.tvvideoms.com/api/ipam/"
    url = base_url + "vlans/"  # URL pour récupérer la liste des VLANs

    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return  response.json()
        
    else:
        print(f"Échec de la requête pour récupérer les VLANs. Code de réponse : {response.status_code}")
        print(response.text)  # Affiche le message d'erreur retourné par l'API en cas d'échec

# Appel de la fonction pour récupérer les VLANs
data = get_vlans()
print (data)
