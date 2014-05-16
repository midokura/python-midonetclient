# Copyright (c) 2014 Midokura Europe SARL, All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from midonetclient.resource_base import ResourceBase
from midonetclient import vendor_media_type

class VtepBinding(ResourceBase):

    media_type = vendor_media_type.APPLICATION_VTEP_BINDING_JSON

    def __init__(self, uri, dto, auth):
        super(VtepBinding, self).__init__(uri, dto, auth)

    def get_management_ip(self):
        return self.dto['mgmtIP']

    def get_port_name(self):
        return self.dto['portName']

    def get_vlan_id(self):
        return self.dto['vlanId']

    def get_network_id(self):
        return self.dto['networkId']

    def port_name(self, port_name):
        self.dto['portName'] = port_name
        return self

    def vlan_id(self, vlan_id):
        self.dto['vlanId'] = vlan_id
        return self

    def network_id(self, network_id):
        self.dto['networkId'] = network_id
        return self

    def create(self, headers=None):
        """Does REST POST at some uri followed by REST GET at new location"""
        headers = headers or dict()
        self._ensure_content_type(headers)

        self.auth.do_request(self.uri, 'POST', body=self.dto, headers=headers)
        # TODO(tomohiko) This method override is a temporary workaround for
        # unimplemented MidoNet API VTEP binding GET. Remove this once the GET
        # is implemented.
        return self
