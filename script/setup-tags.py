#!/usr/bin/env python

from midonetclient.api import MidonetApi
import sys

def main():
    mn_uri = 'http://localhost:8080/midonet-api'
    my_laptop = 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'
    mc = MidonetApi(mn_uri, 'admin', 'password')

    bridge = mc.add_bridge().name('DHCPv6BRIDGE').tenant_id(my_laptop).create()
    port_left = bridge.add_exterior_port().create()
    port_right = bridge.add_exterior_port().create()
    tag = bridge.add_tag().tag("tomohiko_tag1").create()
    tag = bridge.add_tag().tag("tomohiko_tag2").create()

    ## Test deleting a bridge.
    bridge_delete = mc.add_bridge().name('BRIDGE_DELETE_TEST').tenant_id(my_laptop).create()
    tag = bridge_delete.add_tag().tag("bridge_delete_tag1").create()
    tag = bridge_delete.add_tag().tag("bridge_delete_tag2").create()
    bridge_delete.delete()

    tags = bridge.get_tags()
    for tag in tags:
      print("%s\n", tag.get_tag())

    ## # Set up interface/vport binding
    ## host = mc.get_host(my_laptop)
    ## interface_left = host.add_host_interface_port().port_id(port_left.get_id()).interface_name('leftdp')
    ## interface_left.create()
    ## interface_right = host.add_host_interface_port().port_id(port_right.get_id()).interface_name('rightdp')
    ## interface_right.create()

if __name__ == '__main__':
    main()
