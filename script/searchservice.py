#!/usr/bin/env python

from midonetclient.api import MidonetApi
import sys

_MN_URI = 'http://localhost:8081'
_MC = MidonetApi(_MN_URI, 'admin', 'password')

def lookup_tagged_bridges(tag):
    print 'Looking up bridges with tag: %s' % tag
    bridges = _MC.get_tagged_resources(tag)
    if bridges:
      print '-Found %d resources.' % len(bridges)
    else:
      print '-No resources found.\n'
      return

    for bridge in bridges:
      print('-Bridge')
      print('    Name: %s' % bridge.get_name())
      print('    id: %s' % bridge.get_id())
      print('    tenant id: %s' % bridge.get_tenant_id())

    print '\n'
