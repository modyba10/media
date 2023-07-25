import   api

import json


def update_subnet_data():


    data = api.acquire_data ("subnets/all/")
 

    i=0

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

    
    for subnet in data :



        

        subnet ["masterSubnet"] =subnet.pop("masterSubnetId")

        #Ici on va supprimer les champs non utile
    
    
    return [data]








