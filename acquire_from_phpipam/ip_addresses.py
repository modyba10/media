import csv
import json
import os
import api
import subnets


import api
import json


import   api

import json


def update_subnet_data_for_ip():

    data = api.acquire_data ("subnets/all/")

    for subnet in data:

        subnet["subnet"] += "/" + subnet["mask"]
    
        
        

        # Replace the value of the "masterSubnetId" field
        # with the corresponding subnet if it's different from "0", otherwise, set it to None
        if subnet["masterSubnetId"] != "0":
            for prev_subnet in data:
                if prev_subnet["id"] == subnet["masterSubnetId"]:
                    subnet["masterSubnetId"] = prev_subnet["subnet"]
                    break
        else:

            subnet["masterSubnetId"] = None


    return data




def get_ip_adresses():

    data = api.acquire_data_test("addresses/all/")

    # Appeler la fonction update_subnet_data() pour obtenir la liste des sous-réseaux
    subnets_data = update_subnet_data_for_ip()
    subnets_d = subnets_data
    
    for ip in data:

        

        # Concatenate the "mask" field to the "ip_addresses" field

        subnet_id = ip["subnetId"]

        for subnet in subnets_d:

            if subnet["id"] == subnet_id:

                ip["address"] = f"{ip['ip']}/{subnet['mask']}"

                break

        # Replace the value of the "masterSubnetId" field
        # with the corresponding subnet if it's different from "0", otherwise, set it to None

        # Supprimer le champ "subnetId" car nous avons déjà ajouté le masque CIDR à "address"
        ip.pop("subnetId", None)

        # Supprimer d'autres champs indésirables
        del ip["links"]

        del ip["id"]
        del ip["is_gateway"]
        del ip["mac"]
        del ip["owner"]
        del ip["deviceId"]
        del ip["location"]
        del ip["port"]
        del ip["note"]
        del ip["lastSeen"]
        del ip["excludePing"]
        del ip["PTRignore"]
        del ip["PTR"]
        del ip["firewallAddressObject"]
        del ip["editDate"]
        del ip["customer_id"]
        del ip["tag"]

        # Mettre par défaut toutes les IPs en "active"
        ip["status"] = "active"

        # Remplacer le hostname par dns_name
        ip["dns_name"] = ip.pop("hostname")
    for ip in data:
        del ip["ip"]

    return data

        

        








def ip_to_csv():

    csv_file = "ip_addresses.csv"

    data_json = get_ip_adresses()

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






def update_columns_from_csv():

    ip_to_csv ()

    
    columns_to_remove =  ["custom_HOSTNAME_NICS_ADMIN","custom_HOSTNAME_NICS_STORAGE","custom_FQDN_INTERNAL","custom_fields"]

    input_file = "ip_addresses.csv"

    output_file = "ip_addresses.csv"

    # Vérifier si le fichier d'entrée existe

    if not os.path.isfile(input_file):

        print("Le fichier d'entrée spécifié n'existe pas.")

        return False

    # Lire le fichier CSV et supprimer les colonnes spécifiées

    data = []

    with open(input_file, 'r', newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            for column in columns_to_remove:

                row.pop(column, None)

            data.append(row)

    # Écrire les données dans un nouveau fichier CSV

    with open(output_file, 'w', newline='') as csvfile:

        fieldnames = data[0].keys()  # Récupérer les noms de colonnes à partir du premier dictionnaire

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(data)



