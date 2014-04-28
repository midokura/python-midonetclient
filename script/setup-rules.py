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
    # mn_uri = 'http://localhost:8081'
    my_laptop = 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'
    # mc = MidonetApi(mn_uri, 'admin', 'password')
    mc = MidonetApi(**args)

    chain = mc.add_chain().name('tomohiko_11th_chain').tenant_id(my_laptop).create()
    print('*** 5th chain id: ' + chain.get_id())
    rule = chain.add_rule()
    rule.type('snat')
    rule.flow_action('accept')
    rule.nw_src_address('172.16.1.1')
    rule.nw_src_length(24)
    rule.nw_dst_address('172.16.1.2')
    rule.nw_dst_length(24)
    rule.out_ports(['3e7c31c5-64d9-4184-a27a-3f985d83a71b'])
    rule.nat_targets([{'addressFrom': '200.11.11.11',
                       'addressTo': '200.11.11.12',
                       'portFrom': 8888,
                       'portTo': 9999}])
    rule.create()
    print('*** rule id: ' + rule.get_id())

if __name__ == '__main__':
    main()
