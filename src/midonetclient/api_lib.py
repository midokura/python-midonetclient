# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Midokura PTE LTD.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# @author: Tomoe Sugihara <tomoe@midokura.com>, Midokura
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura

import exc
import httplib2
import json
import logging
import urllib

LOG = logging.getLogger(__name__)


def do_request(uri, method, body=None, query=None, headers=None):

    LOG.debug("do_request: uri=%s, method=%s" % (uri, method))
    LOG.debug("do_request: body=%s" % body)
    LOG.debug("do_request: headers=%s" % headers)

    if body != None:
        data = json.dumps(body)
    else:
        data = '{}'

    if query:
        uri += '?' + urllib.urlencode(query)

    if headers == None:
        headers = {}

    h = httplib2.Http()
    response, content = h.request(uri, method, data, headers=headers)

    LOG.debug("do_request: response=%s" % response)
    LOG.debug("do_request: content=%s" % content)

    if int(response['status']) > 300:
        e = exc.get_exception(response['status'])(content)
        LOG.error("Raising an exeption: (%r): %r" % (e, str(e)))
        raise e
    try:
        body = json.loads(content) if content else None
        return response, body
    except ValueError:
        return response, content
