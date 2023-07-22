import   api

import json


def update_subnet_data():
    data = api.acquire_data ("subnets/all/")
    
   
    
    for subnet in data:
        # Concatenate the "mask" field to the "subnet" field
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

        # A partir d'ici on va supprimer les champs qu'il faut, c'est à dire les champs inutile 

        del subnet["mask"]

        #A On va redefir les champs pour les rendre comforme à Nautobot

        

        subnet ["masterSubnet"] =subnet.pop("masterSubnetId")
    
    
    return data

