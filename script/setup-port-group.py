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

    port_group = mc.add_port_group().name('tomohiko-port-group').tenant_id(my_laptop).create()
    port_group.add_port_group_port().port_id('3e7c31c5-64d9-4184-a27a-3f985d83a71b').create()

if __name__ == '__main__':
    main()
