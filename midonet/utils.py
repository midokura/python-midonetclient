# Copyright (C) 2011 Midokura Japan KK

"""
Internal Utility Functions
"""

import logging
logging.basicConfig(level=logging.DEBUG)

def debug_print(msg, resp, body):
    logging.debug('-' * 10)
    logging.debug("%s :",   msg)
    logging.debug("Resp: %s" % resp)
    logging.debug("Body: %s" % body)
    logging.debug('-' * 10)
