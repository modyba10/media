import api_nautobot as api
import acquire_from_phpipam.subnets as subnets

def add_ip():
    
    api.create_nautobot_resource("prefixes/", subnets.update_subnet_data())