

import vlans_domains as domains
import csv

def json_to_csv():
    csv_file = "data_for_nautobot.csv"
    data_json = domains.update_vlans_domains_data()
    
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

# Exemple d'utilisation

json_to_csv()