#!/usr/bin/env python
 
import logging
import time

from midonetclient import api

logging.basicConfig(level=logging.DEBUG)

args = {
    'base_uri': "http://127.0.0.1:8080",
    #'base_uri': "http://127.0.0.1:8080/midonet",
    #'base_uri': "http://127.0.0.1:8080/midonet-api",
    'username': 'quantum',
    'password': 'quantum',
    'project_id': 'service',
}

mido = api.MidonetApi(**args)

for h in mido.get_hosts(): print h.get_name()

time.sleep(2)

for h in mido.get_hosts(): print h.get_name()
