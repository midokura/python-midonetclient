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
        mc = MidonetClient()
        cls.tenant = mc.tenants()
        cls.router = mc.routers()
        cls.bridge = mc.bridges()
        cls.router_port = mc.router_ports()
        cls.bridge_port = mc.bridge_ports()

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


    def test_create_list_get_delete_bridge_port(self):
        r, c = self.bridge.create(self.test_tenant_name, self.test_bridge_name)
        bridge_uuid = utils.get_uuid(r)

        r, c = self.bridge_port.create(self.test_tenant_name, bridge_uuid,
                                       str(uuid.uuid4()), str(uuid.uuid4()),
                                       [str(uuid.uuid4()), str(uuid.uuid4()),
                                        str(uuid.uuid4()), str(uuid.uuid4())])
        port_uuid = utils.get_uuid(r)
        self.bridge_port.list(self.test_tenant_name, bridge_uuid)
        self.bridge_port.get(self.test_tenant_name, bridge_uuid, port_uuid)
        self.bridge_port.delete(self.test_tenant_name, bridge_uuid, port_uuid)


if __name__ == '__main__':
    unittest.main()
