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


class TestBridge(unittest.TestCase):

    tenent = None
    bridge = None
    test_tenant_name = "TEST_TENANT"
    test_bridge_name = "TEST_BRIDGE"

    @classmethod
    def setUpClass(cls):
        mc = MidonetClient()
        cls.tenant = mc.tenants()
        cls.bridge = mc.bridges()

        try:
            cls.tenant.create(cls.test_tenant_name)
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.tenant.delete(cls.test_tenant_name)

    def test_list(self):
        self.bridge.list(self.test_tenant_name)

    def test_create_get_delete_peer_ports(self):
        r, c = self.bridge.create(self.test_tenant_name, self.test_bridge_name)
        bridge_uuid = utils.get_uuid(r)
        self.bridge.get(self.test_tenant_name, bridge_uuid)
        self.bridge.peer_ports(self.test_tenant_name, bridge_uuid)
        self.bridge.delete(self.test_tenant_name, bridge_uuid)

        self.assertRaises(LookupError, self.bridge.get, self.test_tenant_name, bridge_uuid)

if __name__ == '__main__':
    unittest.main()
