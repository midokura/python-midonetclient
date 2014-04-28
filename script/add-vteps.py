#!/usr/bin/env python

from midonetclient.api import MidonetApi
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

args = {
    'base_uri': "http://127.0.0.1:8080/midonet-api",
    'username': 'quantum',
    'password': 'quantum',
    'project_id': 'service',
}

def main():
    my_laptop = 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'
    mc = MidonetApi(**args)

    vtep_management_ip = '119.15.112.22'
    vtep_management_port = '6633'

    # Preparation
    bridge_name = 'DHCPv6BRIDGE NO2'
    bridge_exists = False
    bridges = mc.get_bridges({'tenant_id': my_laptop})
    for b in bridges: 
        if b.get_name() == bridge_name:
            bridge_exists = True
            bridge = b 

    if not bridge_exists: 
        bridge = mc.add_bridge().name(bridge_name).tenant_id(my_laptop).create()

    bridge_id = bridge.get_id()
    print 'Bridge ID for %s: %s' % (bridge_name, bridge_id)

    # Create a new VTEP
    vtep = mc.add_vtep().name('My VTEP').management_ip(vtep_management_ip).management_port(vtep_management_port).create()
    print 'Created a VTEP.'

    # Add a new VTEP binding.
    #vtep_binding = vtep.add_binding().port_name('in1').network_id(bridge_id).create()
    vtep_binding = vtep.add_binding().port_name('in1').vlan_id(124).network_id(bridge_id).create()
    print 'Added a new VTEP binding.'

    #mgmt_ip = vtep_binding.get_management_ip()
    #port_name = vtep_binding.get_port_name()
    #vlan_id = vtep_binding.get_vlan_id()
    #network_id = vtep_binding.get_network_id()
    #print 'mgmt ip=%s, port name=%s, vlan id=%d, network id=%s' % (mgmt_ip, port_name, vlan_id, network_id)

    # Add a new VTEP binding 
    #bindings = mc.get_bridge('SOME-BRIDGE-ID').get_vtep_bindings()


if __name__ == '__main__':
    main()
