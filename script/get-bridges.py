#!/usr/bin/env python

from midonetclient.api import MidonetApi
import logging
import sys
import time

logging.basicConfig(level=logging.DEBUG)

args = {
    'base_uri': "http://127.0.0.1:8080/midonet-api",
    'username': 'quantum',
    'password': 'quantum',
    'project_id': 'service',
}

def main():
    # mn_uri = 'http://localhost:8081'
    my_laptop = 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'
    # mc = MidonetApi(mn_uri, 'admin', 'password')
    mc = MidonetApi(**args)

    mc.get_bridges({'tenant_id': 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'})

    print('Sleep for 2 secs.')
    time.sleep(3)
    #mc.get_bridges({'tenant_id': my_laptop})
    mc.get_port_groups({'tenant_id': 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'})

if __name__ == '__main__':
    main()
