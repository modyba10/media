import csv
import   api

import json


def update_subnet_data():


    data = api.acquire_data ("subnets/all/")
    vlans =api.acquire_data ("vlans/all/") 

   
 

    

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


        #A On va redefir les champs pour les rendre comforme à Nautobot


        subnet ["masterSubnet"] =subnet.pop("masterSubnetId")
        subnet["status"] = "active"
        subnet["is_pool"] =True


        #traiter le vlanId

        if subnet["vlanId"] !=0 : 

            for vlan in vlans:

                if vlan["id"] ==subnet["vlanId"]:
                    subnet["vlanId"]= vlan["name"]
                    break
        else:
            subnet["vlanId"] =None

        
      
        subnet ["vlan"] =subnet.pop("vlanId")        


        

        #Ici on va supprimer les champs non utile
      
        list = [
        "mask",
        "sectionId",
        "isFull",
        "vrfId",
        "permissions",
        "custom_fields",
        "pingSubnet",
        "discoverSubnet",
        "resolveDNS",
        "DNSrecursive",
        "DNSrecords",
        "nameserverId",
        "scanAgent",
        "customer_id",
        "isFolder",
        "tag",
        "threshold",
        "location",
        "editDate",
        "lastScan",
        "lastDiscovery",
        "isPool",
        "links", 
        "linked_subnet",
        "firewallAddressObject",
        "allowRequests",
        "showName",
        "device"]


        for item in list:

            del subnet[item]

    
    return json.dumps(data,indent =4)
  


print (update_subnet_data ())



def subnets_to_csv():

    csv_file = "prefixes_or_subnets.csv"

    data_json = update_subnet_data()

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








