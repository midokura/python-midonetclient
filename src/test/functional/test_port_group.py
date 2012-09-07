# Copyright 2012 Midokura Japan KK

import os
import sys
import unittest

TOPDIR = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                   os.pardir,
                                   os.pardir,
                                   os.pardir))
sys.path.insert(0, TOPDIR)

from midonet.client import MidonetClient
from midonet import utils

class TestPortGroup(unittest.TestCase):

    TENANT_ID = 'TEST-TENANT'
    PORT_GROUP_NAME = 'TEST-PORT-GROUP-NAME'

    @classmethod
    def setUpClass(cls):
        cls.mc = MidonetClient()
        cls.pg = cls.mc.port_groups()

    def test_create_list_get_delete(self):
        res, content = self.pg.create(self.TENANT_ID, self.PORT_GROUP_NAME)
        pg_uri = res['location']
        response, pgs = self.pg.list(self.TENANT_ID)
        res, pg = self.mc.get(pg_uri)
        res, pg = self.mc.delete(pg_uri)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
