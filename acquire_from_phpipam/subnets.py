import csv
import json
import api





def update_vlans_test():
    data_domains = api.acquire_data("l2domains/")
    data = api.acquire_data("vlans/all")

    for vlan in data:
        vlan["name"] = f"{vlan['name']}-{vlan['number']}"
        found_match = False  # Variable pour vérifier si une correspondance a été trouvée pour ce VLAN
        for domain in data_domains:
            if vlan["domainId"] == domain["id"]:
                vlan["domainId"] = domain["name"]
                found_match = True
                break

        # Si aucune correspondance n'a été trouvée, attribuer une valeur par défaut
        if not found_match:
            vlan["domainId"] = None

    return data





def update_subnet_data():
    data = api.acquire_data("subnets/all/")
    vlans = update_vlans_test()

    for subnet in data:

        
        subnet["subnet"] += "/" + subnet["mask"]

        # Replace the value of the "masterSubnetId" field
        # with the corresponding subnet if it's different from "0", otherwise, set it to None
        """
        if subnet["masterSubnetId"] != "0":
            for prev_subnet in data:
                if prev_subnet["id"] == subnet["masterSubnetId"]:
                    subnet["masterSubnetId"] = prev_subnet["subnet"]
                    break
        else:
            subnet["masterSubnetId"] = None
        """

        # Redefine the fields to make them compliant with Nautobot
        subnet["masterSubnet"] = subnet.pop("masterSubnetId")
        subnet["status"] = "active"
        subnet["is_pool"] = True

        # Process the vlanId
        if subnet["vlanId"] != 0:

            for vlan in vlans:
                
                if vlan["id"] == subnet["vlanId"]:

                    subnet["vlan_group"] = vlan["domainId"]

                    subnet["vlanId"] = vlan["name"]

                    break

        else:

            subnet["vlanId"] = None


        subnet["vlan"] = subnet.pop("vlanId")


        subnet["prefix"] = subnet.pop("subnet")

        # Remove unnecessary fields
        keys_to_keep = ["vlan_group","status", "is_pool", "vlan", "prefix","description"]

        subnet_keys = list(subnet.keys())

        for key in subnet_keys:

            if key not in keys_to_keep:

                del subnet[key]

    return data

def delete_0 () : 

    data = update_subnet_data()

    for subnet in data :

        if subnet["vlan"] == "0" :

            subnet["vlan"] = ""

    return data






def subnets_to_csv():
    csv_file = "prefixes_or_subnets.csv"
    data_json = delete_0()

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
subnets_to_csv()




