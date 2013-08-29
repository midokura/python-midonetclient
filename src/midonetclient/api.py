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
# @author: Artem Dmytrenko <art@midokura.com>, Midokura

import logging
from socket import error as socket_error

from midonetclient import auth_lib
from midonetclient.application import Application
from midonetclient import midoapi_exceptions


LOG = logging.getLogger(__name__)


def _net_addr(addr):
    """Get network address prefix and length from a given address."""
    nw_addr, nw_len = addr.split('/')
    nw_len = int(nw_len)
    return nw_addr, nw_len


class MidonetApi(object):

    def __init__(self, base_uri, username, password, project_id=None):
        self.base_uri = base_uri.rstrip('/')
        self.project_id = project_id
        self.app = None
        self.auth = auth_lib.Auth(self.base_uri + '/login', username, password,
                                  project_id)

    def get_tenants(self, query = {}):
        self._ensure_application()
        return self.app.get_tenants(query)

    def delete_router(self, id_):
        self._ensure_application()
        return self.app.delete_router(id_)

    def get_routers(self, query):
        self._ensure_application()
        return self.app.get_routers(query)

    def delete_bridge(self, id_):
        self._ensure_application()
        return self.app.delete_bridge(id_)

    def get_bridges(self, query):
        self._ensure_application()
        return self.app.get_bridges(query)

    def delete_port_group(self, id_):
        self._ensure_application()
        return self.app.delete_port_group(id_)

    def get_port_groups(self, query):
        self._ensure_application()
        return self.app.get_port_groups(query)

    def get_chains(self, query):
        self._ensure_application()
        return self.app.get_chains(query)

    def delete_chain(self, id_):
        self._ensure_application()
        return self.app.delete_chain(id_)

    def get_chain(self, id_):
        self._ensure_application()
        return self.app.get_chain(id_)

    def get_tunnel_zones(self, query=None):
        if query is None:
            query = {}
        self._ensure_application()
        return self.app.get_tunnel_zones(query)

    def get_tunnel_zone(self, id_):
        self._ensure_application()
        return self.app.get_tunnel_zone(id_)

    def get_hosts(self, query=None):
        if query is None:
            query = {}
        self._ensure_application()
        return self.app.get_hosts(query)
    
    def add_host_interface_port(self, host, port_id, interface_name):
        return host.add_host_interface_port().port_id(vport_id) \
            .interface_name(host_dev_name).create()

    def get_write_version(self):
        self._ensure_application()
        return self.app.get_write_version()

    def get_system_state(self):
        self._ensure_application()
        return self.app.get_system_state()

    def get_host_versions(self, query=None):
        self._ensure_application()
        return self.app.get_host_versions(query)

    def get_host(self, id_):
        self._ensure_application()
        return self.app.get_host(id_)

    def delete_ad_route(self, id_):
        self._ensure_application()
        return self.app.delete_ad_route(id_)

    def get_ad_route(self, id_):
        self._ensure_application()
        return self.app.get_ad_route(id_)

    def delete_bgp(self, id_):
        self._ensure_application()
        return self.app.delete_bgp(id_)

    def get_bgp(self, id_):
        self._ensure_application()
        return self.app.get_bgp(id_)

    def get_bridge(self, id_):
        self._ensure_application()
        return self.app.get_bridge(id_)

    def get_port_group(self, id_):
        self._ensure_application()
        return self.app.get_port_group(id_)

    def delete_port(self, id_):
        self._ensure_application()
        return self.app.delete_port(id_)

    def get_port(self, id_):
        self._ensure_application()
        return self.app.get_port(id_)

    def delete_route(self, id_):
        self._ensure_application()
        return self.app.delete_route(id_)

    def get_route(self, id_):
        self._ensure_application()
        return self.app.get_route(id_)

    def get_router(self, id_):
        self._ensure_application()
        return self.app.get_router(id_)

    def delete_rule(self, id_):
        self._ensure_application()
        return self.app.delete_rule(id_)

    def get_rule(self, id_):
        self._ensure_application()
        return self.app.get_rule(id_)

    def get_tenant(self, id_):
        self._ensure_application()
        return self.app.get_tenant(id_)

    def add_router(self):
        self._ensure_application()
        return self.app.add_router()

    def add_bridge(self):
        self._ensure_application()
        return self.app.add_bridge()

    def add_port_group(self):
        self._ensure_application()
        return self.app.add_port_group()

    def add_chain(self):
        self._ensure_application()
        return self.app.add_chain()

    def add_tunnel_zone(self):
        self._ensure_application()
        return self.app.add_tunnel_zone()

    def add_gre_tunnel_zone(self):
        self._ensure_application()
        return self.app.add_gre_tunnel_zone()

    def add_capwap_tunnel_zone(self):
        self._ensure_application()
        return self.app.add_capwap_tunnel_zone()

    # Trace condition operations
    def add_trace_condition(self):
        self._ensure_application()
        return self.app.add_trace_condition()

    def get_trace_conditions(self, query=None):
        self._ensure_application()
        return self.app.get_trace_conditions(query)

    def get_trace_condition(self, id_):
        self._ensure_application()
        return self.app.get_trace_condition(id_)

    def delete_trace_condition(self, id_):
        self._ensure_application()
        return self.app.delete_trace_condition(id_)

    def get_trace_ids(self, query=None):
        self._ensure_application()
        return self.app.get_trace_ids(query)

    def get_trace_messages(self, id_):
        self._ensure_application()
        return self.app.get_trace_messages(id_)

    def delete_trace_messages(self, id_):
        self._ensure_application()
        return self.app.delete_trace_messages(id_)

    def add_bridge_port(self, bridge):
        return bridge.add_port().create()

    def add_router_port(self, router, port_address=None,
                        network_address=None, network_length=None):
        port = router.add_port()
        return port.port_address(port_address).network_address(
            network_address).network_length(network_length).create()

    def link(self, port, peer_id):
        port.link(peer_id)

    def unlink(self, port):
        if port.get_peer_id():
            peer_id = port.get_peer_id()
            port.unlink()
            self.delete_port(peer_id)

    def add_router_route(self, router, type='Normal',
                         src_network_addr=None, src_network_length=None,
                         dst_network_addr=None, dst_network_length=None,
                         next_hop_port=None, next_hop_gateway=None,
                         weight=100):
        """Add a route to a router."""
        route = router.add_route().type(type)
        route = route.src_network_addr(src_network_addr).src_network_length(
            src_network_length).dst_network_addr(
                dst_network_addr).dst_network_length(dst_network_length)
        route = route.next_hop_port(next_hop_port).next_hop_gateway(
            next_hop_gateway).weight(weight)

        return route.create()

    def get_router_routes(self, router_id):
        """Get a list of routes for a given router."""
        router = self.get_router(router_id)
        if router is None:
            raise ValueError("Invalid router_id passed in %s" % router_id)
        return router.get_routes()

    def add_chain_rule(self, chain, action='accept', **kwargs):
        """Add a rule to a chain."""
        # Set default values
        prop_defaults = {
            "nw_src_address": None,
            "nw_src_length": None,
            "inv_nw_src": False,
            "tp_src": None,
            "inv_tp_src": None,
            "nw_dst_address": None,
            "nw_dst_length": None,
            "inv_nw_dst_addr": False,
            "tp_dst": None,
            "inv_tp_dst": None,
            "dl_src": None,
            "inv_dl_src": False,
            "dl_dst": None,
            "inv_dl_dst": False,
            "nw_proto": None,
            "inv_nw_proto": False,
            "dl_type": None,
            "inv_dl_type": False,
            "jump_chain_id": None,
            "jump_chain_name": None,
          "match_forward_flow": False,
            "match_return_flow": False,
            "position": None,
            "properties": None
        }

        # Initialize the rule with passed-in or default values
        vals = {}
        for (prop, default) in prop_defaults.iteritems():
            vals[prop] = kwargs.get(prop, default)

        rule = chain.add_rule().type(action)
        rule = rule.nw_src_address(vals.get("nw_src_address"))
        rule = rule.nw_src_length(vals.get("nw_src_length"))
        rule = rule.inv_nw_src(vals.get("inv_nw_src"))
        rule = rule.nw_dst_address(vals.get("nw_dst_address"))
        rule = rule.nw_dst_length(vals.get("nw_dst_length"))
        rule = rule.inv_nw_dst(vals.get("inv_nw_dst"))
        rule = rule.tp_src(vals.get("tp_src"))
        rule = rule.inv_tp_src(vals.get("inv_tp_src"))
        rule = rule.tp_dst(vals.get("tp_dst"))
        rule = rule.inv_tp_dst(vals.get("inv_tp_dst"))
        rule = rule.dl_src(vals.get("dl_src"))
        rule = rule.inv_dl_src(vals.get("inv_dl_src"))
        rule = rule.dl_dst(vals.get("dl_dst"))
        rule = rule.inv_dl_dst(vals.get("inv_dl_dst"))
        rule = rule.nw_proto(vals.get("nw_proto"))
        rule = rule.inv_nw_proto(vals.get("inv_nw_proto"))
        rule = rule.dl_type(vals.get("dl_type"))
        rule = rule.inv_dl_type(vals.get("inv_dl_type"))
        rule = rule.jump_chain_id(vals.get("jump_chain_id"))
        rule = rule.jump_chain_name(vals.get("jump_chain_name"))
        rule = rule.match_forward_flow(vals.get("match_forward_flow"))
        rule = rule.match_return_flow(vals.get("match_return_flow"))
        rule = rule.position(vals.get("position"))
        rule = rule.properties(vals.get("properties"))

        return rule.create()

    def _ensure_application(self):
        if self.app is None:
            self.app = Application(None, {'uri': self.base_uri}, self.auth)
            try:
                self.app.get()
            except midoapi_exceptions.MidoApiConnectionRefused:
                self.app = None
                raise


# just for testing
if __name__ == '__main__':

    import uuid
    import time
    import sys

    if len(sys.argv) < 4:
        print >> sys.stderr, "Functional testing with MN API"
        print >> sys.stderr, "Usage: " + sys.argv[0] \
            + " <URI> <username> <password> [project_id]"
        sys.exit(-1)

    uri = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    if len(sys.argv) > 4:
        project_id = sys.argv[4]
    else:
        project_id = None

    tenant_id = str(uuid.uuid4())
    FORMAT = '%(asctime)-15s %(name)s %(message)s'
    logging.basicConfig(format=FORMAT)
    LOG.setLevel(logging.DEBUG)

    api = MidonetApi(uri, username, password, project_id=project_id)

    # Tunnel zones
    tz1 = api.add_gre_tunnel_zone().name('tunnel_vision').create()
    tz1.name("going' through my head").update()
    tz1.get_hosts()
    tz1.delete()

    tz2 = api.add_capwap_tunnel_zone().name('tunnel_vision2').create()
    tz2.name("going' through my head2").update()
    tz2.get_hosts()
    tz2.delete()

    # Routers
    api.get_routers({'tenant_id': 'non-existent'})
    print api.get_routers({'tenant_id': tenant_id})

    random_uuid = str(uuid.uuid4())
    router1 = api.add_router().name('router-1').tenant_id(
        tenant_id).inbound_filter_id(random_uuid).create(headers={})
    api.get_routers({'tenant_id': 'non-existent'})
    api.get_router(router1.get_id())

    router2 = api.add_router().name('router-2').tenant_id(
        tenant_id).outbound_filter_id(random_uuid).create()

    router1.name('router1-changed').update()

    api.get_router(router1.get_id())

    for r in api.get_routers({'tenant_id': tenant_id}):
        print '--------', r.get_name()
        print 'id: ', r.get_id()
        print 'inboundFilterId: ', r.get_inbound_filter_id()
        print 'outboundFilterId: ', r.get_outbound_filter_id()

    api.get_router(router1.get_id())

    print '-------- Tenants ------'
    tenants = api.get_tenants(query={})
    for t in tenants:
        print 'id: ',  t.get_id()
        print 'name: ', t.get_name()

        print '----- Tenant by ID ------'
        t = api.get_tenant(t.get_id())
        print 'id: ',  t.get_id()
        print 'name: ', t.get_name()

    # Tenant routers
    print '-------- Tenant Routers ------'
    for t in tenants:
        for r in t.get_routers():
            print 'id: ',  r.get_id()

    # Routers/Ports

    # port group1
    pg1 = api.add_port_group().tenant_id(tenant_id).name('pg-1').create()
    pg2 = api.add_port_group().tenant_id(tenant_id).name('pg-2').create()

    # Tenant port groups
    print '-------- Tenant port groups ------'
    for t in tenants:
        for p in t.get_port_groups():
            print 'id: ',  p.get_id()

    rp1 = router1.add_port()\
                 .port_address('2.2.2.2')\
                 .network_address('2.2.2.0')\
                 .network_length(24).create()

    # Add this port to both port groups
    pgp1 = pg1.add_port_group_port().port_id(rp1.get_id()).create()
    pgp2 = pg2.add_port_group_port().port_id(rp1.get_id()).create()
    print 'rp1 port group ids=%r' % [pgp1.get_port_group_id(),
                                     pgp2.get_port_group_id()]

    rp2 = router1.add_port().port_address('1.1.1.1')\
                 .network_address('1.1.1.0').network_length(24).create()

    rp3 = router1.add_port().port_address('1.1.1.2')\
                 .network_address('1.1.1.0').network_length(24).create()
    rp4 = router1.add_port().port_address('1.1.1.3')\
                 .network_address('1.1.1.0').network_length(24).create()
    print api.get_port(rp1.get_id())

    # Router/Routes

    print '-------- router/routes'
    router1.add_route().type('Normal').src_network_addr('0.0.0.0')\
                       .src_network_length(0)\
                       .dst_network_addr('100.100.100.1')\
                       .dst_network_length(32)\
                       .weight(1000)\
                       .next_hop_port(rp4.get_id())\
                       .next_hop_gateway('10.0.0.1').create()

    print router1.get_routes()

    rp2.link(rp3.get_id())

    bgp1 = rp1.add_bgp().local_as(1234).peer_as(5678)\
              .peer_addr('3.3.3.3').create()

    ar1 = bgp1.add_ad_route().nw_prefix('4.4.4.0')\
                             .nw_prefix_length(24)\
                             .create()
    ar2 = bgp1.add_ad_route().nw_prefix('5.5.5.0')\
                             .nw_prefix_length(24)\
                             .create()

    for ar in bgp1.get_ad_routes():
        print 'advertised route--------'
        print '\t', ar.get_id()
        print '\t', ar.get_nw_prefix()
        print '\t', ar.get_prefix_length()

    print rp1.get_bgps()

    # Bridges
    bridge1 = api.add_bridge().name('bridge-1').tenant_id(tenant_id).create()
    bridge1.name('bridge1-changed').update()

    bridge2 = api.add_bridge().name('bridge-2').tenant_id(
        tenant_id).inbound_filter_id(random_uuid).create()

    for b in api.get_bridges({'tenant_id': tenant_id}):
        print '--------', b.get_name()
        print 'id: ', b.get_id()
        print 'inboundFilterId: ', b.get_inbound_filter_id()
        print 'outboundFilterId: ', b.get_outbound_filter_id()

    print api.get_bridge(bridge1.get_id())

    # Tenant bridges
    print '-------- Tenant Bridges ------'
    for t in tenants:
        for b in t.get_bridges():
            print 'id: ',  b.get_id()

    # Bridges/Ports
    bp1 = bridge1.add_port().inbound_filter_id(random_uuid).create()

    # Add this port to both port groups
    pgp1 = pg1.add_port_group_port().port_id(bp1.get_id()).create()
    pgp2 = pg2.add_port_group_port().port_id(bp1.get_id()).create()
    print 'bp1 port group ids=%r' % [pgp1.get_port_group_id(),
                                     pgp2.get_port_group_id()]

    bp2 = bridge1.add_port().create()

    print api.get_port(bp1.get_id())
    bp2.link(rp4.get_id())

    print router1.get_peer_ports({})
    print bridge1.get_peer_ports({})

    for bp in bridge1.get_ports():
        print 'bridge port----'
        print bp.get_id()

    dhcp1 = bridge1.add_dhcp_subnet().default_gateway('10.10.10.1')\
                   .subnet_prefix('10.10.10.0').subnet_length(24).create()

    dhcp2 = bridge1.add_dhcp_subnet().default_gateway(
        '11.11.11.1').subnet_prefix('11.11.11.0').subnet_length(24).create()

    dhcp1.add_dhcp_host().name('host-1').ip_addr('10.10.10.2')\
                         .mac_addr('00:00:00:aa:bb:cc').create()
    dhcp1.add_dhcp_host().name('host-2').ip_addr('10.10.10.3')\
                         .mac_addr('00:00:00:aa:bb:dd').create()

    assert 2 == len(dhcp1.get_dhcp_hosts())

    for ds in bridge1.get_dhcp_subnets():
        print 'dhcp subnet', ds

    bridge1.get_dhcp_subnet('11.11.11.0_24')

    # list port groups and remove them.
    pgs = api.get_port_groups({'tenant_id': tenant_id})
    for pg in pgs:
        print pg.get_name()
        print pg.get_id()

    # Add a port(bp2) to pg2
    pgp1 = pg2.add_port_group_port().port_id(bp2.get_id()).create()

    membership = pg2.get_ports()
    size = len(membership)
    print 'pg2(id=%r) membership=%r, size=%d' % (pg2.get_id(), membership,
                                                 size)
    pgp1.delete()
    membership = pg2.get_ports()
    size_after_delete_pgp1 = len(membership)
    print 'pg2(id=%r) membership=%r, size=%d' % (pg2.get_id(),
                                                 membership,
                                                 size_after_delete_pgp1)
    assert size == size_after_delete_pgp1 + 1

    pg1.delete()
    # Try deleting by ID
    api.delete_port(pg2.get_id())

    # tear down routers and bridges
    bp2.unlink()    # if I don't unlink, deletion of router blows up
    rp2.unlink()

    router1.delete()
    router2.delete()
    bridge1.delete()
    bridge2.delete()

    # Chains
    chain1 = api.add_chain().tenant_id(tenant_id).name('chain-1').create()
    chain2 = api.add_chain().tenant_id(tenant_id).name('chain-2').create()

    for c in api.get_chains({'tenant_id': tenant_id}):
        print '------- chain: ', c.get_name()
        print c.get_id()

    # Tenant chains
    print '-------- Tenant Chains -----'
    for t in tenants:
        for c in t.get_chains():
            print 'id: ',  c.get_id()

    rule1 = chain1.add_rule().type('accept').create()
    rule2 = chain1.add_rule().type('reject').create()

    nat_targets = [{'addressFrom': '192.168.100.1',
                    'addressTo': '192.168.100.10',
                    'portFrom': 80,
                    'portTo': 80},
                   {'addressFrom': '192.168.100.20',
                    'addressTo': '192.168.100.30',
                    'portFrom': 80,
                    'portTo': 80}]

    rule3 = chain1.add_rule().type('dnat').nw_dst_address('1.1.1.1')\
                             .nw_dst_length(32)\
                             .flow_action('accept')\
                             .nat_targets(nat_targets)\
                             .create()

    print '=' * 10
    print rule3.get_nat_targets()

    chain1.delete()
    chain2.delete()

    # Trace conditions
    tCond1 = api.add_trace_condition().nw_src_address('5.5.5.5').create()
    tCond2 = api.add_trace_condition().dl_type('1536').nw_proto('1').create()

    tConds = api.get_trace_conditions()
    for tCond in tConds:
        print 'trace condition ----'
        print tCond.get_id()

    tCond1.delete()
    tCond2.delete()
