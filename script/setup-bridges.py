#!/usr/bin/env python

from midonetclient.api import MidonetApi
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

args = {
    'base_uri': "http://localhost:8080/midonet-api",
    'username': 'quantum',
    'password': 'quantum',
    'project_id': 'service',
}

def main():
    my_laptop = 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'
    mc = MidonetApi(**args)

    bridge = mc.add_bridge().name('DHCPv6BRIDGE').tenant_id(my_laptop).create()
    port_left = bridge.add_exterior_port().create()
    port_right = bridge.add_exterior_port().create()

if __name__ == '__main__':
    main()
