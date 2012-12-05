

from web_resource import WebResource
from application import Application


class MidonetMgmt(object):

    def __init__(self, midonet_uri='http://localhost:8080/midolmanj-mgmt',
                 web_resource=None, logger=None):

        self.midonet_uri = midonet_uri
        self.web_resource = web_resource
        self.app = None

    def get_routers(self, query):
        self._ensure_application()
        return self.app.get_routers(query)

    def get_bridges(self, query):
        self._ensure_application()
        return self.app.get_bridges(query)

    def get_port_groups(self, query):
        self._ensure_application()
        return self.app.get_port_groups(query)

    def get_chains(self, query):
        self._ensure_application()
        return self.app.get_chains(query)

    def get_chain(self, tenant_id, id_):
        self._ensure_application()
        return self.app.get_chain(tenant_id, id_)

    def get_tunnel_zones(self, query={}):
        self._ensure_application()
        return self.app.get_tunnel_zones(query)

    def get_hosts(self, query={}):
        self._ensure_application()
        return self.app.get_hosts(query)

    def get_host(self, id_):
        self._ensure_application()
        return self.app.get_host(id_)

    def get_ad_route(self, id_):
        self._ensure_application()
        return self.app.get_ad_route(id_)

    def get_bgp(self, id_):
        self._ensure_application()
        return self.app.get_bgp(id_)

    def get_bridge(self, id_):
        self._ensure_application()
        return self.app.get_bridge(id_)

    def get_chain(self, id_):
        self._ensure_application()
        return self.app.get_chain(id_)

    def get_host(self, id_):
        self._ensure_application()
        return self.app.get_host(id_)

    def get_port_group(self, id_):
        self._ensure_application()
        return self.app.get_port_group(id_)

    def get_port(self, id_):
        self._ensure_application()
        return self.app.get_port(id_)

    def get_route(self, id_):
        self._ensure_application()
        return self.app.get_route(id_)

    def get_router(self, id_):
        self._ensure_application()
        return self.app.get_router(id_)

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

    def add_gre_tunnel_zone(self):
        self._ensure_application()
        return self.app.add_gre_tunnel_zone()

    def add_capwap_tunnel_zone(self):
        self._ensure_application()
        return self.app.add_capwap_tunnel_zone()

    def _ensure_application(self):
        if (self.app == None):
            self.app = Application(self.web_resource, None,
                                   {'uri': self.midonet_uri})
            self.app.get()


# just for testing
if __name__ == '__main__':

    import uuid
    import time
    import sys

    # add keystone auth
    # from midonet.auth.keystone import KeystoneAuth
    # auth = KeystoneAuth(uri='http://localhost:5000/v2.0',
    #                     username='admin', password='password',
    #                     tenant_id='56b0ed0897c94b23bce00e42edcbb2dc')

    import logging
    FORMAT = '%(asctime)-15s %(name)s %(message)s'
    logging.basicConfig(format=FORMAT)
    LOG = logging.getLogger('nova...midonet.client')
    LOG.setLevel(logging.DEBUG)

    web_resource = WebResource(auth=None, logger=LOG)
    mgmt = MidonetMgmt(web_resource=web_resource, logger=LOG)

#    for z in mgmt.get_tunnel_zones():
#        for h in z.get_hosts():
#            print h

#    hosts =  mgmt.get_hosts()
#    print hosts[0]
#    random_uuid = str(uuid.uuid4())
#    hosts[0].add_host_interface_port().interface_name('ika').port_id(random_uuid).create()

    # Tunnel zones
    tz1 = mgmt.add_gre_tunnel_zone().name('tunnel_vision').create()
    tz1.name("going' through my head").update()
    tz1.get_hosts()
    tz1.delete()

    tz2 = mgmt.add_capwap_tunnel_zone().name('tunnel_vision2').create()
    tz2.name("going' through my head2").update()
    tz2.get_hosts()
    tz2.delete()

    # Routers
    mgmt.get_routers({'tenant_id':'non-existent'})
    print mgmt.get_routers({'tenant_id':'tenant-1'})

    random_uuid = str(uuid.uuid4())
    router1  = mgmt.add_router().name('router-1').tenant_id(
        'tenant-1').inbound_filter_id(random_uuid).create()

    mgmt.get_routers({'tenant_id':'non-existent'})
    mgmt.get_router(router1.get_id())

    router2  = mgmt.add_router().name('router-2').tenant_id(
        'tenant-1').outbound_filter_id(random_uuid).create()

    router1.name('router1-changed').update()

    mgmt.get_router(router1.get_id())

    for r in  mgmt.get_routers({'tenant_id': 'tenant-1'}):
        print '--------', r.get_name()
        print 'id: ', r.get_id()
        print 'inboundFilterId: ', r.get_inbound_filter_id()
        print 'outboundFilterId: ', r.get_outbound_filter_id()


    mgmt.get_router(router1.get_id())

    # Routers/Ports

    rp1 = router1.add_materialized_port().port_address(
        '2.2.2.2').network_address(
        '2.2.2.0').network_length(24).local_network_address(
            '169.254.1.1').local_network_length(24).create()

    rp2 = router1.add_logical_port().port_address(
        '1.1.1.1').network_address(
        '1.1.1.0').network_length(24).create()

    rp3 = router1.add_logical_port().port_address(
        '1.1.1.2').network_address(
        '1.1.1.0').network_length(24).create()
    rp4 = router1.add_logical_port().port_address(
        '1.1.1.3').network_address(
        '1.1.1.0').network_length(24).create()
    print mgmt.get_port(rp1.get_id())

    # Router/Routes

    print '-------- router/routes'
    router1.add_route().type('Normal').src_network_addr(
        '0.0.0.0').src_network_length(0).dst_network_addr(
        '100.100.100.1').dst_network_length(32).weight(
            1000).next_hop_port(rp4.get_id()).next_hop_gateway('10.0.0.1').create()

    print router1.get_routes()



    rp2.link(rp3.get_id())


    bgp1 = rp1.add_bgp().local_as(1234).peer_as(5678).peer_addr(
        '3.3.3.3').create()


    ar1 = bgp1.add_ad_route().nw_prefix('4.4.4.0').nw_prefix_length(
        24).create()
    ar2 = bgp1.add_ad_route().nw_prefix('5.5.5.0').nw_prefix_length(
        24).create()

    for ar in  bgp1.get_ad_routes():
        print 'advertised route--------'
        print '\t', ar.get_id()
        print '\t', ar.get_nw_prefix()
        print '\t', ar.get_prefix_length()


    print rp1.get_bgps()


    # Bridges
    bridge1 = mgmt.add_bridge().name('bridge-1').tenant_id(
        'tenant-1').create()
    bridge1.name('bridge1-changed').update()

    bridge2 = mgmt.add_bridge().name('bridge-2').tenant_id(
        'tenant-1').inbound_filter_id(random_uuid).create()

    for b in  mgmt.get_bridges({'tenant_id':'tenant-1'}):
        print '--------', b.get_name()
        print 'id: ', b.get_id()
        print 'inboundFilterId: ', b.get_inbound_filter_id()
        print 'outboundFilterId: ', b.get_outbound_filter_id()


    print mgmt.get_bridge(bridge1.get_id())

    # Bridges/Ports
    bp1 = bridge1.add_materialized_port().inbound_filter_id(
        random_uuid).create()
    bp2 = bridge1.add_logical_port().create()

    print mgmt.get_port(bp1.get_id())
    bp2.link(rp4.get_id())


    print router1.get_peer_ports({})
    print bridge1.get_peer_ports({})

    for bp in bridge1.get_ports():
        print 'bridge port----'
        print bp.get_id()

    dhcp1 = bridge1.add_dhcp_subnet().default_gateway(
        '10.10.10.1').subnet_prefix(
        '10.10.10.0').subnet_length(24).create()

    dhcp2 = bridge1.add_dhcp_subnet().default_gateway(
        '11.11.11.1').subnet_prefix(
        '11.11.11.0').subnet_length(24).create()


    dhcp1.add_dhcp_host().name('host-1').ip_addr(
        '10.10.10.2').mac_addr('00:00:00:aa:bb:cc').create()
    dhcp1.add_dhcp_host().name('host-2').ip_addr(
        '10.10.10.3').mac_addr('00:00:00:aa:bb:dd').create()

    assert 2 == len(dhcp1.get_dhcp_hosts())



    for ds in bridge1.get_dhcp_subnets():
        print 'dhcp subnet', ds

    bridge1.get_dhcp_subnet('11.11.11.0_24')


    # tear down routers and bridges


    bp2.unlink()    # if I don't unlink, deletion of router blows up
    rp2.unlink()
    #time.sleep(30)

    router1.delete()
    router2.delete()
    bridge1.delete()
    bridge2.delete()

    # PortGroups
    pg1 = mgmt.add_port_group().tenant_id('tenant-1').name('pg-1').create()
    pg2 = mgmt.add_port_group().tenant_id('tenant-1').name('pg-2').create()

    pgs = mgmt.get_port_groups({'tenant_id': 'tenant-1'})
    for pg in pgs:
        print pg.get_name()
        print pg.get_id()
    pg1.delete()
    pg2.delete()


    # Chains
    chain1 = mgmt.add_chain().tenant_id('tenant-1').name('chain-1').create()
    chain2 = mgmt.add_chain().tenant_id('tenant-1').name('chain-2').create()

    for c in mgmt.get_chains({'tenant_id': 'tenant-1'}):
        print '------- chain: ', c.get_name()
        print c.get_id()

    rule1 = chain1.add_rule().type('accept').create()
    rule2 = chain1.add_rule().type('reject').create()

    nat_targets= [{ 'addressFrom': '192.168.100.1',
                    'addressTo': '192.168.100.10',
                    'portFrom': 80,
                    'portTo': 80},
                  { 'addressFrom': '192.168.100.20',
                    'addressTo': '192.168.100.30',
                    'portFrom': 80,
                    'portTo': 80},
                  ]

    rule3 = chain1.add_rule().type('dnat').nw_dst_address(
        '1.1.1.1').nw_dst_length(32).flow_action(
        'accept').nat_targets(nat_targets).create()

    print '=' * 10
    print rule3.get_nat_targets()

    #time.sleep(20)

    chain1.delete()
    chain2.delete()
