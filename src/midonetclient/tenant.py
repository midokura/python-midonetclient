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
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura


from midonetclient import vendor_media_type
from midonetclient.bridge import Bridge
from midonetclient.chain import Chain
from midonetclient.port_group import PortGroup
from midonetclient.resource_base import ResourceBase
from midonetclient.router import Router


class Tenant(ResourceBase):

    media_type = vendor_media_type.APPLICATION_TENANT_JSON

    def __init__(self, uri, dto, auth):
        super(Tenant, self).__init__(uri, dto, auth)

    def get_name(self):
        return self.dto['name']

    def get_id(self):
        return self.dto['id']

    def id(self, id):
        self.dto['id'] = id
        return self

    def name(self, name):
        self.dto['name'] = name
        return self

    def get_bridges(self, query=None):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_BRIDGE_COLLECTION_V2_JSON}
        return self.get_children(self.dto['bridges'], query, headers, Bridge)

    def get_chains(self, query=None):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_CHAIN_COLLECTION_JSON}
        return self.get_children(self.dto['chains'], query, headers, Chain)

    def get_port_groups(self, query=None):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_PORTGROUP_COLLECTION_JSON}
        return self.get_children(self.dto['portGroups'], query, headers,
                                 PortGroup)

    def get_routers(self, query=None):
        headers = {'Accept':
                   vendor_media_type.APPLICATION_ROUTER_COLLECTION_V2_JSON}
        return self.get_children(self.dto['routers'], query, headers, Router)
