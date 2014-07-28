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

    def delete_network(self, net_id):
        LOG.info("delete_network %r", net_id)
        self.client.delete(self.network_url(net_id))

    def get_network(self, net_id, fields=None):
        LOG.info("get_network %r", net_id)
        return self.client.get(self.network_url(net_id), media_type.NETWORK)

    def get_networks(self, filters=None, fields=None,
                     sorts=None, limit=None, marker=None,
                     page_reverse=False):
        LOG.info("get_networks")
        return self.client.get(self.networks_url(), media_type.NETWORKS)

    def update_network(self, net_id, network):
        LOG.info("update_network %r", network)
        return self.client.put(self.network_url(net_id), media_type.NETWORK,
                               network)

    def create_subnet(self, subnet):
        LOG.info("create_subnet %r", subnet)
        return self.client.post(self.subnets_url(), media_type.SUBNET,
                                body=subnet)

    def create_subnet_bulk(self, subnets):
        LOG.info("create_subnet_bulk entered")
        return self.client.post(self.subnets_url(), media_type.SUBNETS,
                                body=subnets)

    def delete_subnet(self, sub_id):
        LOG.info("delete_subnet %r", sub_id)
        self.client.delete(self.subnet_url(sub_id))

    def get_subnet(self, sub_id):
        LOG.info("get_subnet %r", sub_id)
        return self.client.get(self.subnet_url(sub_id), media_type.SUBNET)

    def get_subnets(self):
        LOG.info("get_subnets")
        return self.client.get(self.subnets_url(), media_type.SUBNETS)

    def update_subnet(self, sub_id, subnet):
        LOG.info("update_subnet %r", subnet)
        return self.client.put(self.subnet_url(sub_id), media_type.SUBNET,
                               subnet)

    def create_port(self, port):
        LOG.info("create_port %r", port)
        return self.client.post(self.ports_url(), media_type.PORT, body=port)

    def create_port_bulk(self, ports):
        LOG.info("create_port_bulk entered")
        return self.client.post(self.ports_url(), media_type.PORTS, body=ports)

    def delete_port(self, port_id):
        LOG.info("delete_port %r", port_id)
        self.client.delete(self.port_url(port_id))

    def get_port(self, port_id):
        LOG.info("get_port %r", port_id)
        return self.client.get(self.port_url(port_id), media_type.PORT)

    def get_ports(self):
        LOG.info("get_ports")
        return self.client.get(self.ports_url(), media_type.PORTS)

    def update_port(self, port_id, port):
        LOG.info("update_port %r", port)
        return self.client.put(self.port_url(port_id), media_type.PORT, port)


class L3ClientMixin(url_provider.L3UrlProviderMixin):
    """L3 operation mixin

    Mixin that defines all the Neutron L3 operations in MidoNet API.
    """

    def create_router(self, router):
        LOG.info("create_router %r", router)
        return self.client.post(self.routers_url(), media_type.ROUTER,
                                body=router)

    def delete_router(self, router_id):
        LOG.info("delete_router %r", router_id)
        self.client.delete(self.router_url(router_id))

    def get_router(self, router_id, fields=None):
        LOG.info("get_router %r", router_id)
        return self.client.get(self.router_url(router_id), media_type.ROUTER)

    def get_routers(self, filters=None, fields=None,
                    sorts=None, limit=None, marker=None,
                    page_reverse=False):
        LOG.info("get_routers")
        return self.client.get(self.routers_url(), media_type.ROUTERS)

    def update_router(self, router_id, router):
        LOG.info("update_router %r", router)
        return self.client.put(self.router_url(router_id), media_type.ROUTER,
                               router)

    def add_router_interface(self, router_id, interface_info):
        LOG.info("add_router_interface %r %r", (router_id, interface_info))
        return self.client.put(self.add_router_interface_url(router_id),
                               media_type.ROUTER_INTERFACE, interface_info)

    def remove_router_interface(self, router_id, interface_info):
        LOG.info("remove_router_interface %r %r", (router_id, interface_info))
        return self.client.put(self.remove_router_interface_url(router_id),
                               media_type.ROUTER_INTERFACE, interface_info)

    def create_floating_ip(self, floating_ip):
        LOG.info("create_floating_ip %r", floating_ip)
        return self.client.post(self.floating_ips_url(),
                                media_type.FLOATING_IP, body=floating_ip)

    def delete_floating_ip(self, id):
        LOG.info("delete_floating_ip %r", id)
        self.client.delete(self.floating_ip_url(id))

    def get_floating_ip(self, id):
        LOG.info("get_floating_ip %r", id)
        return self.client.get(self.floating_ip_url(id),
                               media_type.FLOATING_IP)

    def get_floating_ips(self):
        LOG.info("get_floating_ips")
        return self.client.get(self.floating_ips_url(),
                               media_type.FLOATING_IPS)

    def update_floating_ip(self, id, floating_ip):
        LOG.info("update_floating_ip %r", floating_ip)
        return self.client.put(self.floating_ip_url(id),
                               media_type.FLOATING_IP, floating_ip)


class SecurityGroupClientMixin(url_provider.SecurityGroupUrlProviderMixin):
    """Security group operation mixin

    Mixin that defines all the Neutron Sg operations in MidoNet API.
    """

    def create_security_group(self, security_group):
        LOG.info("create_security_group %r", security_group)
        return self.client.post(self.security_groups_url(),
                                media_type.SECURITY_GROUP,
                                body=security_group)

    def create_security_group_bulk(self, security_groups):
        LOG.info("create_security_group_bulk entered")
        return self.client.post(self.security_groups_url(),
                                media_type.SECURITY_GROUPS,
                                body=security_groups)

    def delete_security_group(self, sg_id):
        LOG.info("delete_security_group %r", sg_id)
        self.client.delete(self.security_group_url(sg_id))

    def get_security_group(self, sg_id):
        LOG.info("get_security_group %r", sg_id)
        return self.client.get(self.security_group_url(sg_id),
                               media_type.SECURITY_GROUP)

    def get_security_groups(self):
        LOG.info("get_security_groups")
        return self.client.get(self.security_groups_url(),
                               media_type.SECURITY_GROUPS)

    def update_security_group(self, sg_id, security_group):
        LOG.info("update_security_group %r", security_group)
        return self.client.put(self.security_group_url(sg_id),
                               media_type.SECURITY_GROUP, security_group)

    def create_security_group_rule(self, security_group_rule):
        LOG.info("create_security_group_rule %r", security_group_rule)
        return self.client.post(self.security_group_rules_url(),
                                media_type.SG_RULE,
                                body=security_group_rule)

    def create_security_group_rule_bulk(self, security_group_rules):
        LOG.info("create_security_group_rule_bulk entered")
        return self.client.post(self.security_group_rules_url(),
                                media_type.SG_RULES,
                                body=security_group_rules)

    def delete_security_group_rule(self, rule_id):
        LOG.info("delete_security_group_rule %r", rule_id)
        self.client.delete(self.security_group_rule_url(rule_id))

    def get_security_group_rule(self, rule_id):
        LOG.info("get_security_group_rule %r", rule_id)
        return self.client.get(self.security_group_rule_url(rule_id),
                               media_type.SG_RULE)


class LoadBalancerClientMixin(url_provider.LoadBalancerUrlProviderMixin):
    """LoadBalancer operation mixin

    Mixin that defines all the Neutron Load Balancer operations in MidoNet API.
    """

    def create_vip(self, vip):
        LOG.info("create_vip %r", vip)
        return self.client.post(self.vips_url(), media_type.VIP, body=vip)

    def delete_vip(self, id):
        LOG.info("delete_vip %r", id)
        self.client.delete(self.vip_url(id))

    def update_vip(self, vip_id, vip):
        LOG.info("update_vip %r", vip)
        return self.client.put(self.vip_url(vip_id), media_type.VIP, vip)

    def create_pool(self, pool):
        LOG.info("create_pool %r", pool)
        return self.client.post(self.pools_url(), media_type.POOL, body=pool)

    def delete_pool(self, id):
        LOG.info("delete_pool %r", id)
        self.client.delete(self.pool_url(id))

    def update_pool(self, pool_id, pool):
        LOG.info("update_pool %r", pool)
        return self.client.put(self.pool_url(pool_id), media_type.POOL, pool)

    def create_member(self, member):
        LOG.info("create_member %r", member)
        return self.client.post(self.members_url(), media_type.MEMBER,
                                body=member)

    def delete_member(self, id):
        LOG.info("delete_member %r", id)
        self.client.delete(self.member_url(id))

    def update_member(self, member_id, member):
        LOG.info("update_member %r", member)
        return self.client.put(self.member_url(member_id), media_type.MEMBER,
                               member)

    def create_health_monitor(self, health_monitor):
        LOG.info("create_health_monitor %r", health_monitor)
        return self.client.post(self.health_monitors_url(),
                                media_type.HEALTH_MONITOR,
                                body=health_monitor)

    def delete_health_monitor(self, id):
        LOG.info("delete_health_monitor %r", id)
        self.client.delete(self.health_monitor_url(id))

    def update_health_monitor(self, health_monitor_id, health_monitor):
        LOG.info("update_health_monitor %r", health_monitor)
        return self.client.put(self.health_monitor_url(health_monitor_id),
                               media_type.HEALTH_MONITOR,
                               health_monitor)

    def create_pool_health_monitor(self, health_monitor, pool_id):
        LOG.info("create_pool_health_monitor %r, %r", health_monitor, pool_id)
        return self.client.post(self.members_url(),
                                media_type.POOL_HEALTH_MONITOR,
                                body=member)

    def delete_pool_health_monitor(self, health_monitor_id, pool_id):
        LOG.info("create_pool_health_monitor %r, %r", health_monitor_id,
                 pool_id)
        self.client.delete(self.member_url(id))


class MidonetClient(NetworkClientMixin, L3ClientMixin,
                    SecurityGroupClientMixin, LoadBalancerClientMixin):
    """Main MidoNet client class

    The main class for MidoNet client.  Instantiate this class to make API
    calls to MidoNet API.
    """

    def __init__(self, base_uri, username, password, project_id=None):
        self.base_uri = base_uri
        self.client = httpclient.HttpClient(base_uri, username, password,
                                            project_id=project_id)
        super(MidonetClient, self).__init__()
