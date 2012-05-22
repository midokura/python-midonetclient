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


class TestChain(unittest.TestCase):

    tenent = None
    router = None
    test_tenant_name = "TEST_TENANT"
    test_router_name = "TEST_ROUTER"

    @classmethod
    def setUpClass(cls):
        mc = MidonetClient()
        cls.tenant = mc.tenants()
        cls.chain = mc.chains()

        try:
            cls.tenant.create(cls.test_tenant_name)
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.tenant.delete(cls.test_tenant_name)

    def test_create_get_delete(self):
        r, c = self.chain.create(self.test_tenant_name, 'TEST_CHAIN')
        chain_uuid = utils.get_uuid(r)

        self.chain.list(self.test_tenant_name)
        self.chain.get(self.test_tenant_name, chain_uuid)
        self.chain.delete(self.test_tenant_name, chain_uuid)


if __name__ == '__main__':
    unittest.main()
