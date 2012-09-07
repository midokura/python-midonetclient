# Copyright (C) 2011 Midokura Japan KK

"""
Internal Utility Functions
"""

import logging
import os.path

logging.basicConfig()
LOG = logging.getLogger('nova...midonet.client')
LOG.setLevel(logging.DEBUG)

def debug_print(msg, req_body, resp, resp_body):
    LOG.debug('-' * 10)
    LOG.debug("%s :",   msg)
    LOG.debug("Req Body: %s" % req_body)
    LOG.debug("Resp: %s" % resp)
    LOG.debug("Resp Body: %s" % resp_body)

def get_uuid(response):
    return os.path.basename(response['location'])

