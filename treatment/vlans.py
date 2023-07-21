import  api

import json
import vlans_domains as dm

def update_vlans():

    data_domains=  api.acquire_data("l2domains/")

    data =  api.acquire_data("vlans/all")

    
    for vlan in data:
        vlan ["status"] = "active"

        for domain in data_domains:
             
             if vlan["domainId"] == domain["id"]:
                    
                    vlan["domainId"] = domain["name"]

                    break
             

        # A partir d'ici on va supprimer les champs qu'il faut, c'est à dire les champs inutile 
        del vlan ["links"]
        del vlan["custom_fields"]
        del vlan ["customer_id"]
        del vlan["editDate"]
        del vlan ["number"]
        


        #A On va redefir les champs pour les rendre comforme à Nautobot


        vlan["group"] =vlan.pop ("domainId")
        vlan["vid"] =vlan.pop ("id")
       





    return data

