import  api_nautobot as api
import  groups_vlans


def add_vlans_groups():

    api.create_nautobot_resource("vlans-groups/", groups_vlans.update_vlans_domains_data())