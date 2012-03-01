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
from midonet.routers import Router
from midonet.tenants import Tenant
from midonet.ports import Port
from midonet import utils


class TestPort(unittest.TestCase):

    tenent = None
    router = None
    test_tenant_name = "TEST_TENANT"
    test_router_name = "TEST_ROUTER"

    @classmethod
    def setUpClass(cls):
        mc = MidonetClient()
        cls.tenant = mc.tenants()
        cls.router = mc.routers()
        cls.port = mc.ports()
        cls.router_port = mc.router_ports()
        cls.vif = mc.vifs()

        try:
            cls.tenant.create(cls.test_tenant_name)
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.tenant.delete(cls.test_tenant_name)

    def test_create_list_get_delete(self):
        resp, content = self.router.create(self.test_tenant_name, self.test_router_name)
        router_uuid = utils.get_uuid(resp['location'])

        resp, content = self.router_port.create(router_uuid, "192.168.10.0", 24,
                                "192.168.10.2", "1.1.1.1", 32)

        port_uuid = utils.get_uuid(resp['location'])
        import uuid

        vif_uuid = str(uuid.uuid4())
        r, c = self.vif.create(vif_uuid, port_uuid)
        vif_uuid = utils.get_uuid(r['location'])

        self.vif.list()
        self.vif.get(vif_uuid)
        self.vif.delete(vif_uuid)



if __name__ == '__main__':
    unittest.main()
