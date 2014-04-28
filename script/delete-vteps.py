#!/usr/bin/env python

from midonetclient.api import MidonetApi
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

args = {
    'base_uri': "http://127.0.0.1:8080/midonet-api",
    'username': 'quantum',
    'password': 'quantum',
    'project_id': 'service',
}

def main():
    mc = MidonetApi(**args)
    vtep_management_ip = '119.15.112.22'

    # Delete a new VTEP
    vtep = mc.delete_vtep(vtep_management_ip)
    print 'Deleted a VTEP.'


if __name__ == '__main__':
    main()
