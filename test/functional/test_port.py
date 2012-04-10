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
from midonet import utils


class TestPort(unittest.TestCase):

    tenent = None
    router = None
    test_tenant_name = "TEST_TENANT"
    test_router_name = "TEST_ROUTER"

    @classmethod
    def setUpClass(cls):
        mc = MidonetClient(no_ks=True)
        cls.tenant = mc.tenants()
        cls.router = mc.routers()
#        cls.port = mc.ports()
        cls.router_port = mc.router_ports()

        try:
            cls.tenant.create(cls.test_tenant_name)
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.tenant.delete(cls.test_tenant_name)

    def test_create_list_get_delete_router_port(self):
        r, c = self.router.create(self.test_tenant_name, self.test_router_name)
        router_uuid = utils.get_uuid(r)

        r, c = self.router_port.create(self.test_tenant_name, router_uuid, "192.168.10.0", 24,
                                "192.168.10.2", "1.1.1.1", 32)

        port_uuid = utils.get_uuid(r)

        self.router_port.list(self.test_tenant_name, router_uuid)
        self.router_port.get(self.test_tenant_name, router_uuid, port_uuid)
        self.router_port.delete(self.test_tenant_name, router_uuid, port_uuid)

if __name__ == '__main__':
    unittest.main()
