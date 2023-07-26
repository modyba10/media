import add_to_nautobot_api.groups_vlans_nautobots as groups
import add_to_nautobot_api.ip_nautobots as ip
import add_to_nautobot_api.subnets_nautobots as subnets
import add_to_nautobot_api.vlans_nautobots as vlans


config = {

    "group" : False,
    "vlans":False,
    "subnets" :False,
    "ip":False

}
    
    #Running

if config["group"] :

    print ("Téléversement des groupes de vlans actuels de phpipam vs Nautobot")

    groups.add_vlans_groups()




if config["vlans"]:

    print ("Téléversement des vlans de phpipam vers Nautobot")
  
    vlans.add_vlans()



if config ["subnets"] :

    print ("Téléversment des address de subnets e phpipam vers Nautobot")

    subnets.add_subnets()




if config["ip"] :
      
      print ("Téléversement des ip de phpipam vers Nautobot")

      ip.add_ip()

