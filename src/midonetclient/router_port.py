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


from midonetclient import port_type
from midonetclient import vendor_media_type
from midonetclient.bgp import Bgp
from midonetclient.resource_base import ResourceBase


class RouterPort(ResourceBase):

    media_type = vendor_media_type.APPLICATION_PORT_JSON

    def __init__(self, uri, dto, auth):
        super(RouterPort, self).__init__(uri, dto, auth)

    def get_id(self):
        return self.dto['id']

    def get_type(self):
        return self.dto['type']

    def get_device_id(self):
        return self.dto['deviceId']

    def get_inbound_filter_id(self):
        return self.dto['inboundFilterId']

    def get_outbound_filter_id(self):
        return self.dto['outboundFilterId']

    def get_network_address(self):
        return self.dto['networkAddress']

    def get_network_length(self):
        return self.dto['networkLength']

    def get_port_address(self):
        return self.dto['portAddress']

    def get_port_mac(self):
        return self.dto['portMac']

    def get_peer_id(self):
        return self.dto['peerId']

    def port_address(self, port_address):
        self.dto['portAddress'] = port_address
        return self

    def network_address(self, network_address):
        self.dto['networkAddress'] = network_address
        return self

    def network_length(self, network_length):
        self.dto['networkLength'] = network_length
        return self

    # Deprecated
    def local_network_address(self, local_network_address):
        assert self.get_type() == port_type.EXTERIOR_ROUTER
        self.dto['localNetworkAddress'] = local_network_address
        return self

    # Deprecated
    def local_network_length(self, local_network_length):
        assert self.get_type() == port_type.EXTERIOR_ROUTER
        self.dto['localNetworkLength'] = local_network_length
        return self

    def inbound_filter_id(self, id_):
        self.dto['inboundFilterId'] = id_
        return self

    def outbound_filter_id(self, id_):
        self.dto['outboundFilterId'] = id_
        return self

    def type(self, type_):
        self.dto['type'] = type_
        return self

    def get_bgps(self):
        query = {}
        headers = {'Accept':
                       vendor_media_type.APPLICATION_BGP_COLLECTION_JSON}
        return self.get_children(self.dto['bgps'], query, headers, Bgp)

    #TODO
    def get_vpns(self):
        pass

    def add_bgp(self):
        return Bgp(self.dto['bgps'], {}, self.auth)

    #TODO
    def add_vpn(self):
        pass

    def link(self, peer_uuid):
        self.dto['peerId'] = peer_uuid
        headers = {'Content-Type':
                    vendor_media_type.APPLICATION_PORT_LINK_JSON}
        self.auth.do_request(self.dto['link'], 'POST', body=self.dto,
                             headers=headers)
        self.get()
        return self

    def unlink(self):
        headers = {'Content-Type':
                    vendor_media_type.APPLICATION_PORT_LINK_JSON}
        self.auth.do_request(self.dto['link'], 'DELETE')
        self.get()
        return self
