import api_nautobot as api
import acquire_from_phpipam.groups_vlans as groups


def add_vlans_groups():

    api.create_nautobot_resource("vlans-groups/", groups.update_vlans_domains_data())