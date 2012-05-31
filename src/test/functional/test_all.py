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


from test_bridge import TestBridge
from test_chain import TestChain
from test_port import TestPort
from test_route import TestRoute
from test_router import TestRouter
from test_rule import TestRule
from test_tenant import TestTenant
from test_dhcp import TestDhcp
from test_dhcp_host import TestDhcpHost
from test_port_group import TestPortGroup

#TODO: automatic test class loading
test_cases = (
              TestBridge,
              TestChain,
              TestPort,
              TestRoute,
              TestRouter,
              TestRule,
              TestTenant,
              TestDhcp,
              TestDhcpHost,
              TestPortGroup
              )


if __name__ == '__main__':
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
