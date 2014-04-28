#!/usr/bin/env python

from midonetclient.api import MidonetApi
import sys

def main():
    mn_uri = 'http://localhost:8081'
    my_laptop = 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'
    mc = MidonetApi(mn_uri, 'admin', 'password')

    bridge = mc.add_bridge().name('DHCPv6BRIDGE NO2').tenant_id(my_laptop).create()
    port_left = bridge.add_exterior_port().create()
    port_right = bridge.add_exterior_port().create()
    tag = bridge.add_tag().tag("tomohiko_tag1").create()
    tag = bridge.add_tag().tag("tomohiko_tag3").create()

    bridge = mc.add_bridge().name('DHCPv6BRIDGE NO3').tenant_id(my_laptop).create()
    port_left = bridge.add_exterior_port().create()
    port_right = bridge.add_exterior_port().create()
    tag = bridge.add_tag().tag("tomohiko_tag1").create()
    tag = bridge.add_tag().tag("tomohiko_tag2").create()

if __name__ == '__main__':
    main()
