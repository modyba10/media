import  api 
import json

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

        # A partir d'ici on va supprimer les champs qu'il faut, c'est à dire les champs inutile 
         

         #A On va redefir les champs pour les rendre comforme à Nautobot


    return data



