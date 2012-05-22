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

class TestTenant(unittest.TestCase):

    t = None

    @classmethod
    def setUpClass(cls):
        mc = MidonetClient()
        cls.t = mc.tenants()
        cls.t.delete("Ika")

    def test_list(self):
        self.t.list()

    def test_create_get_delete(self):
        self.t.create("Ika")
        self.t.get("Ika")
        self.t.delete("Ika")

    def test_create_without_id_get_delete(self):
        r, c = self.t.create()
        id_ = utils.get_uuid(r)
        self.t.get(id_)
        self.t.delete(id_)


if __name__ == '__main__':
    unittest.main()
