import api_nautobot as api 
import acquire_from_phpipam.ip_addresses as ip




def add_ip():
    
    api.create_nautobot_resource("ip-addresses/", ip.get_ip_adresses())