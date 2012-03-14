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


class TestRouter(unittest.TestCase):

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

    def test_create_get_delete(self):
        r, c = self.bridge.create(self.test_tenant_name, self.test_bridge_name)
        bridge_uuid = utils.get_uuid(r)
        self.bridge.get(bridge_uuid)
        self.bridge.delete(bridge_uuid)
        #NOTE: shouldn't mgmt return HTTPNotFounnd?
        self.assertRaises(exc.HTTPInternalServerError, self.bridge.get, bridge_uuid)

    def test_link_create(self):
        #TODO
        pass


if __name__ == '__main__':
    unittest.main()
