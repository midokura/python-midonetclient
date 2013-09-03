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


import json
import logging
import urllib

import httplib2
import webob
from socket import error as socket_error
from midonetclient import midoapi_exceptions


# TODO: lots of duplicates with auth_lib => merge both ?

LOG = logging.getLogger(__name__)


http_errors = dict((str(e.code), e) for e in
                   webob.exc.HTTPClientError.__subclasses__() +
                   webob.exc.HTTPServerError.__subclasses__())


def is_http_error(status, content):
    """check if http status is error and return Error object or else None"""
    return http_errors[status](content) if int(status) > 300 else False


def fail_if(err):
    """write log and raise exception if err is not None"""
    if err:
        LOG.error("http error => raising exception (%r): %r" % (err, str(err)))
        raise err


def from_json(content):
    """try to deserialize json string if not empty or else return raw input"""
    try:
        if content:
            return json.loads(content)
    except ValueError:
        LOG.warning("do_request: failed to json.load() request content")
    return content


def do_request(uri, method, body=None, query=None, headers=None):
    """Process a http rest request with input and output json strings.

    Sends json string serialized from body to uri with verb method and returns
    a 2-tuple made of http response, and content deserialized into an object.
    """

    LOG.debug("do_request: uri=%s, method=%s" % (uri, method))
    LOG.debug("do_request: body=%s" % body)
    LOG.debug("do_request: headers=%s" % headers)

    if query:
        uri += '?' + urllib.urlencode(query)
    data = json.dumps(body) if body is not None else '{}'
    headers = headers or dict()

    try:
        response, content = httplib2.Http().request(uri, method, data,
                                                    headers=headers)
    except socket_error as serr:
        if serr[1] == "ECONNREFUSED":
            raise midoapi_exceptions.MidoApiConnectionRefused()
        raise

    LOG.debug("do_request: response=%s | content=%s" % (response, content))

    fail_if(is_http_error(response['status'], content))

    return response, from_json(content)
