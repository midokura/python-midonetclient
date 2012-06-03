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

    def test_create_get_update_delete_peer_ports(self):
        r, c = self.router.create(self.test_tenant_name, self.test_router_name,
                           inbound_filter_id=str(uuid.uuid4()),
                           outbound_filter_id=str(uuid.uuid4()))
        router_uuid = utils.get_uuid(r)
        self.router.get(self.test_tenant_name, router_uuid)
        self.router.update(self.test_tenant_name, router_uuid,'new-name',
                           inbound_filter_id=str(uuid.uuid4()),
                           outbound_filter_id=str(uuid.uuid4()))
        self.router.peer_ports(self.test_tenant_name, router_uuid)
        self.router.delete(self.test_tenant_name, router_uuid)
        self.assertRaises(LookupError, self.router.get, self.test_tenant_name,
                          router_uuid)

if __name__ == '__main__':
    unittest.main()
