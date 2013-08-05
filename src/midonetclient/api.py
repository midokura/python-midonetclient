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

import logging

from midonetclient import auth_lib
from midonetclient.application import Application


LOG = logging.getLogger(__name__)


class MidonetApi(object):

    def __init__(self, base_uri, username, password, project_id=None):
        self.base_uri = base_uri.rstrip('/')
        self.project_id = project_id
        self.app = None
        self.auth = auth_lib.Auth(self.base_uri + '/login', username, password,
                                  project_id)

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

    def _ensure_application(self):
        if self.app is None:
            self.app = Application(None, {'uri': self.base_uri}, self.auth)
            self.app.get()


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

    router2 = api.add_router().name('router-2').tenant_id(tenant_id)\
                  .outbound_filter_id(random_uuid).create()

    router1.name('router1-changed').update()

    api.get_router(router1.get_id())

    for r in  api.get_routers({'tenant_id': tenant_id}):
        print '--------', r.get_name()
        print 'id: ', r.get_id()
        print 'inboundFilterId: ', r.get_inbound_filter_id()
        print 'outboundFilterId: ', r.get_outbound_filter_id()

    api.get_router(router1.get_id())

    # Routers/Ports

    # port group1
    pg1 = api.add_port_group().tenant_id(tenant_id).name('pg-1').create()
    pg2 = api.add_port_group().tenant_id(tenant_id).name('pg-2').create()

    rp1 = router1.add_exterior_port()\
                 .port_address('2.2.2.2')\
                 .network_address('2.2.2.0')\
                 .network_length(24).create()

    # Add this port to both port groups
    pgp1 = pg1.add_port_group_port().port_id(rp1.get_id()).create()
    pgp2 = pg2.add_port_group_port().port_id(rp1.get_id()).create()
    print 'rp1 port group ids=%r' % [pgp1.get_port_group_id(),
                                     pgp2.get_port_group_id()]

    rp2 = router1.add_interior_port().port_address('1.1.1.1')\
                 .network_address('1.1.1.0').network_length(24).create()

    rp3 = router1.add_interior_port().port_address('1.1.1.2')\
                 .network_address('1.1.1.0').network_length(24).create()
    rp4 = router1.add_interior_port().port_address('1.1.1.3')\
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

    for ar in  bgp1.get_ad_routes():
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

    for b in  api.get_bridges({'tenant_id': tenant_id}):
        print '--------', b.get_name()
        print 'id: ', b.get_id()
        print 'inboundFilterId: ', b.get_inbound_filter_id()
        print 'outboundFilterId: ', b.get_outbound_filter_id()

    print api.get_bridge(bridge1.get_id())

    # Bridges/Ports
    bp1 = bridge1.add_exterior_port().inbound_filter_id(random_uuid).create()

    # Add this port to both port groups
    pgp1 = pg1.add_port_group_port().port_id(bp1.get_id()).create()
    pgp2 = pg2.add_port_group_port().port_id(bp1.get_id()).create()
    print 'bp1 port group ids=%r' % [pgp1.get_port_group_id(),
                                     pgp2.get_port_group_id()]

    bp2 = bridge1.add_interior_port().create()

    print api.get_port(bp1.get_id())
    bp2.link(rp4.get_id())

    print router1.get_peer_ports({})
    print bridge1.get_peer_ports({})

    for bp in bridge1.get_ports():
        print 'bridge port----'
        print bp.get_id()

    dhcp1 = bridge1.add_dhcp_subnet().default_gateway('10.10.10.1')\
                   .subnet_prefix('10.10.10.0').subnet_length(24).create()

    dhcp2 = bridge1.add_dhcp_subnet().default_gateway('11.11.11.1')\
                    .subnet_prefix('11.11.11.0').subnet_length(24).create()

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

    rule1 = chain1.add_rule().type('accept').create()
    rule2 = chain1.add_rule().type('reject').create()

    nat_targets = [{'addressFrom': '192.168.100.1',
                    'addressTo': '192.168.100.10',
                    'portFrom': 80,
                    'portTo': 80},
                  {'addressFrom': '192.168.100.20',
                    'addressTo': '192.168.100.30',
                    'portFrom': 80,
                    'portTo': 80},
                  ]

    rule3 = chain1.add_rule().type('dnat').nw_dst_address('1.1.1.1')\
                             .nw_dst_length(32)\
                             .flow_action('accept')\
                             .nat_targets(nat_targets)\
                             .create()

    print '=' * 10
    print rule3.get_nat_targets()

    chain1.delete()
    chain2.delete()
