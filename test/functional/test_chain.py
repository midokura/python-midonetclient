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
    router = None
    test_tenant_name = "TEST_TENANT"
    test_router_name = "TEST_ROUTER"

    @classmethod
    def setUpClass(cls):
        mc = MidonetClient()
        cls.tenant = mc.tenants()
        cls.router = mc.routers()
        cls.chain = mc.chains()

        try:
            cls.tenant.create(cls.test_tenant_name)
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.tenant.delete(cls.test_tenant_name)

    def test_create_get_delete(self):
        resp, content = self.router.create(self.test_tenant_name, self.test_router_name)
        router_uuid = utils.get_uuid(resp['location'])

        r, c = self.chain.create(router_uuid, 'TEST_CHAIN')


        chain_uuid = utils.get_uuid(r['location'])

        self.chain.list(router_uuid)
        self.chain.get(chain_uuid)
        self.chain.delete(chain_uuid)


        



if __name__ == '__main__':
    unittest.main()
