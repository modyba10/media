import  api_nautobot as api 
import  vlans

def add_vlans():
    
    api.create_nautobot_resource("vlans/", vlans.update_vlans())