import api_nautobot as api
import acquire_from_phpipam.vlans as vlans

def add_ip():
    
    api.create_nautobot_resource("vlans/", vlans.update_vlans())