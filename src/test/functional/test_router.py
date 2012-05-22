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


class TestRouter(unittest.TestCase):

    tenent = None
    router = None
    test_tenant_name = "TEST_TENANT"
    test_router_name = "TEST_ROUTER"

    @classmethod
    def setUpClass(cls):
        mc = MidonetClient()
        cls.tenant = mc.tenants()
        cls.router = mc.routers()
        cls.bridge = mc.bridges()

        try:
            cls.tenant.create(cls.test_tenant_name)
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.tenant.delete(cls.test_tenant_name)

    def test_list(self):
        self.router.list(self.test_tenant_name)

    def test_create_get_update_delete(self):
        r, c = self.router.create(self.test_tenant_name, self.test_router_name)
        router_uuid = utils.get_uuid(r)
        self.router.get(self.test_tenant_name, router_uuid)

        self.router.update(self.test_tenant_name, router_uuid,'new-name',
                           inboundFilter=str(uuid.uuid4()),
                           outboundFilter=str(uuid.uuid4()))

        self.router.delete(self.test_tenant_name, router_uuid)
        self.assertRaises(LookupError, self.router.get, self.test_tenant_name, router_uuid)

    def test_link_router_create_list_get_delete(self):
        r1, junk = self.router.create(self.test_tenant_name, "router1")
        r2, junk = self.router.create(self.test_tenant_name, "router2")
        r1_uuid = utils.get_uuid(r1)
        r2_uuid = utils.get_uuid(r2)

        self.router.link_router_create(self.test_tenant_name, r1_uuid, "10.0.0.0", 30,
                                "10.0.0.1", "10.0.0.2", r2_uuid)
        self.router.link_router_list(self.test_tenant_name, r1_uuid)
        self.router.link_router_get(self.test_tenant_name, r1_uuid, r2_uuid)
        self.router.link_router_delete(self.test_tenant_name, r1_uuid, r2_uuid)


    def test_link_bridge_create_list_get_delete(self):
        r, junk = self.router.create(self.test_tenant_name, "router11")
        b, junk = self.bridge.create(self.test_tenant_name, "bridge11")
        r_uuid = utils.get_uuid(r)
        b_uuid = utils.get_uuid(b)

        self.router.link_bridge_create(self.test_tenant_name, r_uuid, "10.0.0.0", 24,
                                "10.0.0.1", b_uuid)
        self.router.link_bridge_list(self.test_tenant_name, r_uuid)
        self.router.link_bridge_get(self.test_tenant_name, r_uuid, b_uuid)
        self.router.link_bridge_delete(self.test_tenant_name, r_uuid, b_uuid)


if __name__ == '__main__':
    unittest.main()
