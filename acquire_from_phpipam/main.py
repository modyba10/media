import groups_vlans_nautobots as groups
import ip_nautobots as ip
import subnets_nautobots as subnets
import vlans_nautobots as vlans

#defini true les données que tu veux POST
config = {

    "group" : False,
    "vlans":False,
    "subnets" :False,
    "ip":True

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

