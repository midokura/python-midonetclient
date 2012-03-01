# Copyright 2012 Midokura Japan KK

import os
import sys
import unittest
from webob import exc

TOPDIR = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                   os.pardir,
                                   os.pardir,
                                   os.pardir))
sys.path.insert(0, TOPDIR)

from midonet.client import MidonetClient
from midonet.routes import Route
from midonet.routers import Router
from midonet.tenants import Tenant
from midonet import utils 


class TestRoute(unittest.TestCase):

    tenent = None
    router = None
    route = None
    test_tenant_name = "TEST_TENANT"
    test_router_name = "TEST_ROUTER"

    @classmethod
    def setUpClass(cls):
        mc = MidonetClient()
        cls.tenant = mc.tenants()
        cls.router = mc.routers()
        cls.route = mc.routes()
        cls.router_port = mc.router_ports()

        try:
            cls.tenant.create(cls.test_tenant_name)
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.tenant.delete(cls.test_tenant_name)

    def test_create_list_get_delete_router_port(self):
        resp, content = self.router.create(self.test_tenant_name, self.test_router_name)
        router_uuid = utils.get_uuid(resp['location'])

        resp, content = self.router_port.create(router_uuid, "192.168.10.0", 24,
                                "192.168.10.2", "1.1.1.1", 32)

        port_uuid = utils.get_uuid(resp['location'])

        resp, content = self.route.create(router_uuid, "Normal", "0.0.0.0", 0,
                                          "9.9.9.9", 24, 100, port_uuid)

        route_uuid = utils.get_uuid(resp['location'])

        self.route.list(router_uuid)
        self.route.get(route_uuid)
        self.route.delete(route_uuid)


if __name__ == '__main__':
    unittest.main()
