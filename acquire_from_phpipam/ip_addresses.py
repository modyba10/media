import api
import subnets

def get_ip_adresses (subnet) :

    data = api.acquire_data("addresses/all/")
    for element in data:
        print("Nothing")
        

        # A partir d'ici on va supprimer les champs qu'il faut, c'est à dire les champs inutile 
         

         #A On va redefir les champs pour les rendre comforme à Nautobot


    return data