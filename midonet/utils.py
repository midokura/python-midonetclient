# Copyright (C) 2011 Midokura Japan KK

"""
Internal Utility Functions
"""

import logging
import os.path

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger('midonet.client')

def debug_print(msg, resp, body):
    LOG.debug('-' * 10)
    LOG.debug("%s :",   msg)
    LOG.debug("Resp: %s" % resp)
    LOG.debug("Body: %s" % body)
    LOG.debug('-' * 10)

def get_uuid(response):
    return os.path.basename(response['location'])

