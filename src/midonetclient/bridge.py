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
# @author: Tomoe Sugihara <tomoe@midokura.com>, Midokura
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura

from resource_base import ResourceBase
from bridge_port import BridgePort
from router_port import RouterPort
from dhcp_subnet import DhcpSubnet

import port_type
import vendor_media_type


class Bridge(ResourceBase):

    media_type = vendor_media_type.APPLICATION_BRIDGE_JSON

    def __init__(self, uri, dto, auth):
        super(Bridge, self).__init__(uri, dto, auth)

    def get_name(self):
        return self.dto['name']

    def get_id(self):
        return self.dto['id']

    def get_tenant_id(self):
        return self.dto['tenantId']

    def get_inbound_filter_id(self):
        return self.dto['inboundFilterId']

    def get_outbound_filter_id(self):
        return self.dto['outboundFilterId']

    def name(self, name):
        self.dto['name'] = name
        return self

    def tenant_id(self, tenant_id):
        self.dto['tenantId'] = tenant_id
        return self

    def inbound_filter_id(self, id_):
        self.dto['inboundFilterId'] = id_
        return self

    def outbound_filter_id(self, id_):
        self.dto['outboundFilterId'] = id_
        return self

    def get_ports(self, query=None):
        if query == None:
            query = {}
        headers = {'Accept':
                       vendor_media_type.APPLICATION_PORT_COLLECTION_JSON}
        return self.get_children(self.dto['ports'], query, headers, BridgePort)

    def get_peer_ports(self, query=None):
        if query == None:
            query = {}
        headers = {'Accept':
                       vendor_media_type.APPLICATION_PORT_COLLECTION_JSON}
        res, peer_ports = self.auth.do_request(self.dto['peerPorts'], 'GET',
                                               headers=headers, query=query)

        res = []
        for pp in peer_ports:
            if pp['type'] == port_type.INTERIOR_ROUTER:
                res.append(RouterPort(self.dto['ports'], pp, self.auth))
            elif pp['type'] == port_type.INTERIOR_BRIDGE:
                res.append(BridgePort(self.dto['ports'], pp, self.auth))
        return res

    def get_dhcp_subnets(self):
        query = {}
        headers = {
            'Accept':
                vendor_media_type.APPLICATION_DHCP_SUBNET_COLLECTION_JSON
            }
        return self.get_children(self.dto['dhcpSubnets'], query, headers,
                                 DhcpSubnet)

    def get_dhcp_subnet(self, subnet_str):
        """
        given the subnet_str (x.x.x.x_y, address_length), returns DhcpSubnet
        resource that has subnet prefix and length found in the subnet_str.
        """
        prefix, length = subnet_str.split('_')
        for ds in self.get_dhcp_subnets():
            if ds.get_subnet_prefix() == prefix and \
                    ds.get_subnet_length() == int(length):
                return ds
        raise LookupError('subnet=%r not found' % subnet_str)

    def add_interior_port(self):
        return BridgePort(self.dto['ports'],
                          {'type': port_type.INTERIOR_BRIDGE}, self.auth)

    def add_exterior_port(self):
        return BridgePort(self.dto['ports'],
                          {'type': port_type.EXTERIOR_BRIDGE}, self.auth)

    def add_dhcp_subnet(self):
        return DhcpSubnet(self.dto['dhcpSubnets'], {}, self.auth)
