import  api
import csv

def update_vlans_domains_data():

    data = api.acquire_data ("l2domains/")
    for element in data:
         
         if element["description"] is None :
              element["description"] = "None"


         # A partir d'ici on va supprimer les champs qu'il faut, c'est à dire les champs inutile 

         del element["custom_fields"]
         del element["sections"]
         del element ["links"]
         del element ["id"]
         
         #A On va redefir les champs pour les rendre comforme à Nautobot


    return data


"""
def vlans_domains_to_csv():
    csv_file = "data_for_nautobot.csv"
    data_json = update_vlans_domains_data()
    
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
            writer.writerow(entry) """


