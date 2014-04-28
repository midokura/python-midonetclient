#!/usr/bin/env python

from midonetclient.api import MidonetApi
import sys

def lookup_tagged_resources(api, tag):
    print 'Looking up bridges with tag: %s' % tag
    bridges = api.get_tagged_resources(tag)
    if bridges:
      print '-Found %d resources.' % len(bridges)
    else:
      print '-No resources found.\n'
      return

    for index, bridge in enumerate(bridges):
      print('-Bridge %d' % index)
      print('    Name: %s' % bridge.get_name())
      print('    id: %s' % bridge.get_id())
      print('    tenant id: %s' % bridge.get_tenant_id())

    print '\n'

def main():
    mn_uri = 'http://localhost:8081'
    mc = MidonetApi(mn_uri, 'admin', 'password')

    lookup_tagged_resources(mc, 'tomohiko_tag1')
    lookup_tagged_resources(mc, 'tomohiko_tag2')
    lookup_tagged_resources(mc, 'tomohiko_tag3')

if __name__ == '__main__':
    main()
