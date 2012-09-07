# Copyright 2012 Midokura Japan KK

import os
import sys
import unittest
import uuid
from webob import exc

TOPDIR = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                   os.pardir,
                                   os.pardir,
                                   os.pardir))
sys.path.insert(0, TOPDIR)

from midonet.client import MidonetClient
from midonet import utils


class TestPort(unittest.TestCase):

    tenent = None
    router = None
    test_tenant_name = "TEST_TENANT"
    test_router_name = "TEST_ROUTER"
    test_bridge_name = "TEST_BRIDGE"

    @classmethod
    def setUpClass(cls):
        cls.mc = MidonetClient()
        cls.router = cls.mc.routers()
        cls.bridge = cls.mc.bridges()
        cls.router_port = cls.mc.router_ports()
        cls.bridge_port = cls.mc.bridge_ports()


        r, c = cls.router.create(cls.test_tenant_name, cls.test_router_name)
        cls.router_uuid = utils.get_uuid(r)

        r, c = cls.bridge.create(cls.test_tenant_name, cls.test_bridge_name)
        cls.bridge_uuid = utils.get_uuid(r)


    @classmethod
    def tearDownClass(cls):
        cls.bridge.delete(cls.test_tenant_name, cls.bridge_uuid)
        cls.router.delete(cls.test_tenant_name, cls.router_uuid)

    def test_create_list_get_update_delete_materialized_router_port(self):

        r, c = self.router_port.create(self.test_tenant_name, self.router_uuid,
                                       "MaterializedRouter",
                                       "192.168.10.0", 24,
                                       "192.168.10.2", "1.1.1.1", 32)

        port_uuid = utils.get_uuid(r)
        self.router_port.list(self.test_tenant_name, self.router_uuid)
        res, rp = self.router_port.get(self.test_tenant_name,
                                       self.router_uuid, port_uuid)


        res, content = self.router_port.bgp_create(self.test_tenant_name,
                                                   self.router_uuid, port_uuid,
                                                   65104, 23637, "1.1.1.1")
        res, bgp = self.mc.get(res['location'])

        res, bgps = self.router_port.bgp_list(self.test_tenant_name,
                                                   self.router_uuid, port_uuid)

        # add route
        res, content = self.router_port.bgp_ad_route(self.test_tenant_name,
                                                     self.router_uuid,
                                                     port_uuid,
                                                     bgp['id'],
                                                     '14.128.23.0', 27)

        res, ad_route = self.mc.get(res['location'])


        res, ad_routes = self.router_port.bgp_ad_route_list(
                self.test_tenant_name,
                self.router_uuid,
                port_uuid,
                bgp['id'])

        print ad_routes

        res, ad_route = self.router_port.bgp_ad_route_get(
                self.test_tenant_name,
                self.router_uuid,
                port_uuid,
                bgp['id'],
                ad_route['id'])
        print ad_route

        res, ad_routes = self.router_port.bgp_ad_route_delete(
                self.test_tenant_name,
                self.router_uuid,
                port_uuid,
                bgp['id'],
                ad_route['id'])

        res, ad_routes = self.router_port.bgp_ad_route_list(
                self.test_tenant_name,
                self.router_uuid,
                port_uuid,
                bgp['id'])

        res, bgp = self.router_port.bgp_get(self.test_tenant_name,
                                             self.router_uuid, port_uuid,
                                             bgp['id'])


        res, content = self.router_port.bgp_delete(self.test_tenant_name,
                                             self.router_uuid, port_uuid,
                                             bgp['id'])

        res, bgps = self.router_port.bgp_list(self.test_tenant_name,
                                                   self.router_uuid, port_uuid)
        rp['vifId'] = str(uuid.uuid4())
        res, content = self.router_port.update(self.test_tenant_name,
                                        self.router_uuid, port_uuid, rp)
        rp['vifId'] = None
        res, rp = self.router_port.update(self.test_tenant_name,
                                        self.router_uuid, port_uuid, rp)
        self.router_port.delete(self.test_tenant_name, self.router_uuid,
                                port_uuid)


    def test_create_list_get_delete_logical_router_port(self):
        r, c = self.router_port.create(self.test_tenant_name, self.router_uuid,
                                       "LogicalRouter",
                                       "192.168.10.0", 24,
                                       "192.168.10.2", "1.1.1.1", 32)

        port_uuid = utils.get_uuid(r)
        self.router_port.list(self.test_tenant_name, self.router_uuid)
        res, rp = self.router_port.get(self.test_tenant_name,
                                       self.router_uuid, port_uuid)
        self.router_port.delete(self.test_tenant_name, self.router_uuid,
                                port_uuid)


    def test_create_list_get_delete_materialized_bridge_port(self):
        r, c = self.bridge_port.create(self.test_tenant_name, self.bridge_uuid,
                                       'MaterializedBridge',
                                       str(uuid.uuid4()), str(uuid.uuid4()), None)
                                       #[str(uuid.uuid4()), str(uuid.uuid4())])

        port_uuid = utils.get_uuid(r)
        self.bridge_port.list(self.test_tenant_name, self.bridge_uuid)
        res, bp = self.bridge_port.get(self.test_tenant_name,
                                        self.bridge_uuid, port_uuid)

        bp['vifId'] = str(uuid.uuid4())
        res, content = self.bridge_port.update(self.test_tenant_name,
                                        self.bridge_uuid, port_uuid, bp)


        res, bp = self.bridge_port.get(self.test_tenant_name,
                                       self.bridge_uuid, port_uuid)

        bp['vifId'] = None
        res, content = self.bridge_port.update(self.test_tenant_name,
                                               self.bridge_uuid, port_uuid, bp)
        res, bp = self.bridge_port.get(self.test_tenant_name,
                                       self.bridge_uuid, port_uuid)
        self.bridge_port.delete(self.test_tenant_name, self.bridge_uuid,
                                port_uuid)

    def test_create_list_get_delete_logical_bridge_port(self):

        r, c = self.bridge_port.create(self.test_tenant_name, self.bridge_uuid,
                                       'LogicalBridge',
                                       str(uuid.uuid4()), str(uuid.uuid4()),
                                       None)
                                       #[str(uuid.uuid4()), str(uuid.uuid4())])

        port_uuid = utils.get_uuid(r)
        self.bridge_port.list(self.test_tenant_name, self.bridge_uuid)
        self.bridge_port.get(self.test_tenant_name, self.bridge_uuid, port_uuid)
        self.bridge_port.delete(self.test_tenant_name, self.bridge_uuid,
                                port_uuid)

    def _test_link_unlink(self):


        # logical bridge port 1
        r, c = self.bridge_port.create(self.test_tenant_name, self.bridge_uuid,
                                       'LogicalBridge',
                                       str(uuid.uuid4()), str(uuid.uuid4()), None)
                                       #[str(uuid.uuid4()), str(uuid.uuid4())])
        r, bp_1 = self.mc.get(r['location'])

        # logical bridge port 2
        r, c = self.bridge_port.create(self.test_tenant_name, self.bridge_uuid,
                                       'LogicalBridge',
                                       str(uuid.uuid4()), str(uuid.uuid4()), None)
                                       #[str(uuid.uuid4()), str(uuid.uuid4())])
        r, bp_2 = self.mc.get(r['location'])

        # logical router port 1
        r, c = self.router_port.create(self.test_tenant_name, self.router_uuid,
                                       "LogicalRouter",
                                       "192.168.10.0", 24,
                                       "192.168.10.2", "1.1.1.1", 32)
        r, rp_1 = self.mc.get(r['location'])

        # logical router port 2
        r, c = self.router_port.create(self.test_tenant_name, self.router_uuid,
                                       "LogicalRouter",
                                       "192.168.10.0", 24,
                                       "192.168.10.2", "1.1.1.1", 32)
        r, rp_2 = self.mc.get(r['location'])

        # link/unlink from rp_1 to rp_2
        r, c = self.router_port.link(self.test_tenant_name, self.router_uuid,
                                     rp_1['id'], rp_2['id'])
        r, router = self.router.get(self.test_tenant_name, self.router_uuid)
        r, pp = self.router.peer_ports(self.test_tenant_name, self.router_uuid)
        r, c = self.router_port.unlink(self.test_tenant_name, self.router_uuid,
                                     rp_1['id'])

        # link/unlink from bp_1 to rp_1
        r, c = self.bridge_port.link(self.test_tenant_name, self.bridge_uuid,
                                     bp_1['id'], rp_2['id'])
        r, pp = self.bridge.peer_ports(self.test_tenant_name, self.bridge_uuid)
        r, c = self.bridge_port.unlink(self.test_tenant_name, self.bridge_uuid,
                                     bp_1['id'])

        # link/unlink from rp_1 to bp_1
        r, c = self.router_port.link(self.test_tenant_name, self.router_uuid,
                                     rp_1['id'], bp_1['id'])
        r, c = self.router_port.unlink(self.test_tenant_name, self.router_uuid,
                                     rp_1['id'])

if __name__ == '__main__':
    unittest.main()
