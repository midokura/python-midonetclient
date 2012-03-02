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


class TestRule(unittest.TestCase):

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
        cls.rule = mc.rules()

        try:
            cls.tenant.create(cls.test_tenant_name)
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.tenant.delete(cls.test_tenant_name)

    def test_create_get_delete(self):
        r, c = self.router.create(self.test_tenant_name, self.test_router_name)
        router_uuid = utils.get_uuid(r)

        r, c = self.chain.list(router_uuid)

        chain_uuid_0 = c[0]['id']
        chain_uuid_1 = c[1]['id']

        r0, c = self.rule.create_dnat_rule(chain_uuid_0, '123.10.10.3', '192.168.10.3')
        r1, c = self.rule.create_snat_rule(chain_uuid_1, '123.10.10.3', '192.168.10.3')

        self.rule.list(chain_uuid_0)
        self.rule.list(chain_uuid_1)

        rule_0 = utils.get_uuid(r0)
        rule_1 = utils.get_uuid(r1)

        for r in (rule_0, rule_1):
            self.rule.get(r)
            self.rule.delete(r)


if __name__ == '__main__':
    unittest.main()
