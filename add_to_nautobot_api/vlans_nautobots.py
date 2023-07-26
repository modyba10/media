import api_nautobot as api
import acquire_from_phpipam.vlans as vlans

def add_vlans():
    
    api.create_nautobot_resource("vlans/", vlans.update_vlans())