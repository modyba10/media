import groups_vlans as groups
import ip_addresses as ip
import subnets
import vlans

#defini true les données que tu veux POST
config = {

    "group" :False,
    "vlans":False,
    "subnets" :False,
    "ip":False

}
if config["group"] :

    print ("Téléchargement du csv des groupes")

    groups.vlans_domains_to_csv()

    print ("Téléchargement du csv des groupes réeussi")




if config["vlans"]:

    print ("Téléchargement du csv des vlans")
  
    vlans.vlans_to_csv()

    print ("Téléchargement du csv  des vlans réeussi")



if config ["subnets"] :

     print ("Téléchargement du csv des subnets des vlans")

     subnets.subnets_to_csv()

     print ("Téléchargement du csv  des subnets réeussi")





if config["ip"] :
      
      print ("Téléchargement du csv des adresses ip ")

      ip.update_columns_from_csv()

      print ("Téléchargement du csv  des adresses ip réeussi")





    