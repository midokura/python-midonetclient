# Copyright (C) 2011 Midokura Japan KK

"""
Internal Utility Functions
"""

import logging
import os.path

logging.basicConfig()
LOG = logging.getLogger('nova...midonet.client')

def debug_print(msg, resp, body):
    LOG.debug('-' * 10)
    LOG.debug("%s :",   msg)
    LOG.debug("Resp: %s" % resp)
    LOG.debug("Body: %s" % body)

def get_uuid(response):
    return os.path.basename(response['location'])

