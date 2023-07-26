import api
import csv

import json

def update_vlans():
    data_domains = api.acquire_data("l2domains/")
    data = api.acquire_data("vlans/all")

    for vlan in data:
        vlan["status"] = "active"

        for domain in data_domains:
            if vlan["domainId"] == domain["id"]:
                vlan["domainId"] = domain["name"]
                break

        
        # Concatenate the "name" field with the "id" field and replace the "name" field
        vlan["name"] = f"{vlan['name']}-{vlan['number']}"

        # A partir d'ici on va supprimer les champs qu'il faut, c'est à dire les champs inutile 
        del vlan["links"]
        del vlan["custom_fields"]
        del vlan["customer_id"]
        del vlan["editDate"]
        del vlan["number"]
        

        # A On va redefir les champs pour les rendre comforme à Nautobot
        vlan["group"] = vlan.pop("domainId")
        vlan["vid"] = vlan.pop("id")

        

    return data





"""json.dumps(data, indent=4)    Utile pour bien voir les données Json"""

    






def vlans_to_csv():
    csv_file = "vlans_for_nautobot.csv"
    data_json = update_vlans()
    # Vérification des données JSON
    if not isinstance(data_json, list) or not all(isinstance(item, dict) for item in data_json):
        raise ValueError("Le paramètre 'data_json' doit être une liste de dictionnaires.")

    # Vérification des noms de colonnes
    headers = set()
    for entry in data_json:
        headers.update(entry.keys())

    # Écrire les données JSON dans le fichier CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for entry in data_json:
            writer.writerow(entry)

vlans_to_csv()



