import  api_nautobot as api
import subnets

def add_subnets():
    
    api.create_nautobot_resource("prefixes/", subnets.update_subnet_data())