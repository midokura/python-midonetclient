# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2014 Midokura Europe SARL, All Rights Reserved.
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

import logging
from midonetclient import httpclient
from midonetclient.neutron import media_type
from midonetclient.neutron import url_provider

LOG = logging.getLogger(__name__)


class NetworkClientMixin(url_provider.NetworkUrlProviderMixin):
    """Network operation mixin

    Mixin that defines all the Neutron network operations in MidoNet API.
    """

    def create_network(self, network):
        LOG.info("create_network %r", network)
        return self.client.post(self.networks_url(), media_type.NETWORK,
                                body=network)

    def create_network_bulk(self, networks):
        LOG.info("create_network_bulk entered")
        return self.client.post(self.networks_url(), media_type.NETWORKS,
                                body=networks)

    def delete_network(self, id):
        LOG.info("delete_network %r", id)
        self.client.delete(self.network_url(id))

    def get_network(self, id, fields=None):
        LOG.info("get_network %r", id)
        return self.client.get(self.network_url(id), media_type.NETWORK)

    def get_networks(self, filters=None, fields=None,
                     sorts=None, limit=None, marker=None,
                     page_reverse=False):
        LOG.info("get_networks")
        return self.client.get(self.networks_url(), media_type.NETWORKS)

    def update_network(self, id, network):
        LOG.info("update_network %r", network)
        return self.client.put(self.network_url(id), media_type.NETWORK,
                               network)

    def create_subnet(self, subnet):
        LOG.info("create_subnet %r", subnet)
        return self.client.post(self.subnets_url(), media_type.SUBNET,
                                body=subnet)

    def create_subnet_bulk(self, subnets):
        LOG.info("create_subnet_bulk entered")
        return self.client.post(self.subnets_url(), media_type.SUBNETS,
                                body=subnets)

    def delete_subnet(self, id):
        LOG.info("delete_subnet %r", id)
        self.client.delete(self.subnet_url(id))

    def get_subnet(self, id):
        LOG.info("get_subnet %r", id)
        return self.client.get(self.subnet_url(id), media_type.SUBNET)

    def get_subnets(self):
        LOG.info("get_subnets")
        return self.client.get(self.subnets_url(), media_type.SUBNETS)

    def update_subnet(self, id, subnet):
        LOG.info("update_subnet %r", subnet)
        return self.client.put(self.subnet_url(id), media_type.SUBNET, subnet)

    def create_port(self, port):
        LOG.info("create_port %r", port)
        return self.client.post(self.ports_url(), media_type.PORT, body=port)

    def create_port_bulk(self, ports):
        LOG.info("create_port_bulk entered")
        return self.client.post(self.ports_url(), media_type.PORTS, body=ports)

    def delete_port(self, id):
        LOG.info("delete_port %r", id)
        self.client.delete(self.port_url(id))

    def get_port(self, id):
        LOG.info("get_port %r", id)
        return self.client.get(self.port_url(id), media_type.PORT)

    def get_ports(self):
        LOG.info("get_ports")
        return self.client.get(self.ports_url(), media_type.PORTS)

    def update_port(self, id, port):
        LOG.info("update_port %r", port)
        return self.client.put(self.port_url(id), media_type.PORT, port)


class MidonetClient(NetworkClientMixin):
    """Main MidoNet client class

    The main class for MidoNet client.  Instantiate this class to make API
    calls to MidoNet API.
    """

    def __init__(self, base_uri, username, password, project_id=None):
        self.base_uri = base_uri
        self.client = httpclient.HttpClient(base_uri, username, password,
                                            project_id=project_id)
        super(MidonetClient, self).__init__()
