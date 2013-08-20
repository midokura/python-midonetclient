# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Midokura PTE LTD.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# @author: Rossella Sblendido <rossella@midokura.com>, Midokura


from midonetclient import port_type
from midonetclient import vendor_media_type
from midonetclient.resource_base import ResourceBase
from midonetclient.vlan_bridge_trunk_port import VlanBridgeTrunkPort
from midonetclient.vlan_bridge_interior_port import VlanBridgeInteriorPort


class VlanBridge(ResourceBase):

    media_type = vendor_media_type.APPLICATION_VLAN_BRIDGE_JSON

    def __init__(self, uri, dto, auth):
        super(VlanBridge, self).__init__(uri, dto, auth)

    def get_name(self):
        return self.dto['name']

    def get_id(self):
        return self.dto['id']

    def get_tenant_id(self):
        return self.dto['tenantId']

    def name(self, name):
        self.dto['name'] = name
        return self

    def tenant_id(self, tenant_id):
        self.dto['tenantId'] = tenant_id
        return self

    def get_trunk_ports(self, query=None):
        if query == None:
            query = {}
        headers = {'Accept':
                       vendor_media_type.APPLICATION_PORT_COLLECTION_JSON}
        return self.get_children(self.dto['trunkPorts'], query, headers, VlanBridgeTrunkPort)

    def get_interior_ports(self, query=None):
        if query == None:
            query = {}
        headers = {'Accept':
                       vendor_media_type.APPLICATION_PORT_COLLECTION_JSON}
        return self.get_children(self.dto['interiorPorts'], query, headers, VlanBridgeInteriorPort)


    def get_peer_ports(self, query=None):
        if query == None:
            query = {}
        headers = {'Accept':
                       vendor_media_type.APPLICATION_PORT_COLLECTION_JSON}
        res, peer_ports = self.auth.do_request(self.dto['interiorPorts'], 'GET',
                                               headers=headers, query=query)

        res = []
        for pp in peer_ports:
             res.append(VlanBridgeInteriorPort(self.dto['interiorPorts'], pp, self.auth))
        return res

    def add_interior_port(self):
        return VlanBridgeInteriorPort(self.dto['interiorPorts'],
                          {'type': port_type.INTERIOR_VLAN_BRIDGE}, self.auth)

    def add_trunk_port(self):
        return VlanBridgeTrunkPort(self.dto['trunkPorts'],
                          {'type': port_type.TRUNK_VLAN_BRIDGE}, self.auth)

