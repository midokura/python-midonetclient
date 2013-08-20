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
from midonetclient import resource_base
from midonetclient import vendor_media_type


class VlanBridgeInteriorPort(resource_base.ResourceBase):

    media_type = vendor_media_type.APPLICATION_PORT_JSON

    def __init__(self, uri, dto, auth):
        super(VlanBridgeInteriorPort, self).__init__(uri, dto, auth)

    def get_id(self):
        return self.dto['id']

    def get_type(self):
        return self.dto['type']

    def get_device_id(self):
        return self.dto['deviceId']

    def get_peer_id(self):
        return self.dto['peerId']

    def get_vlan_id(self):
        return self.dto['vlanId']

    def vlan_id(self, id_):
        self.dto['vlanId'] = id_
    	return self

    def link(self, peer_uuid):
        self.dto['peerId'] = peer_uuid
        headers = {'Content-Type':
                    vendor_media_type.APPLICATION_PORT_LINK_JSON}
        self.auth.do_request(self.dto['link'], 'POST', self.dto,
                             headers=headers)

        self.get()
        return self

    def unlink(self):
        headers = {'Content-Type':
                    vendor_media_type.APPLICATION_PORT_LINK_JSON}
        self.auth.do_request(self.dto['link'], 'DELETE')
        self.get()
        return self
