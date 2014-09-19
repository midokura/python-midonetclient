# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2014 Midokura Europe SARL, All Rights Reserved.
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
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura

from midonetclient import auth_lib, util


def convert_case(f):
    def wrapper(*args, **kwargs):
        new_args = list()
        for arg in args:
            new_args.append(util.convert_dict_keys(arg, util.snake_to_camel))

        new_kwargs = dict()
        for k, v in kwargs.iteritems():
            new_kwargs[k] = util.convert_dict_keys(v, util.snake_to_camel)

        return util.convert_dict_keys(f(*new_args, **new_kwargs),
                                      util.camel_to_snake)

    return wrapper


class HttpClient(object):

    def __init__(self, base_uri, username, password, project_id=None):
        self.auth_lib = auth_lib.Auth(base_uri + '/login', username, password,
                                      project_id)

    def delete(self, uri):
        self.auth_lib.do_request(uri, 'DELETE')

    def get(self, uri, media_type, params=None):
        headers = {"Accept": media_type}
        resp, data = self.auth_lib.do_request(uri, 'GET', query=params,
                                              headers=headers)
        return data

    def post(self, uri, media_type, body=None):
        headers = {"Content-Type": media_type, "Accept": media_type}
        resp, data = self.auth_lib.do_request(uri, 'POST', body=body,
                                              headers=headers)
        return data

    def put(self, uri, media_type, body=None):
        headers = {"Content-Type": media_type}
        resp, data = self.auth_lib.do_request(uri, 'PUT', body=body,
                                              headers=headers)
        return data


class CaseAwareHttpClient(HttpClient):
    """Temporary class that converts input and output dictionary keys between
    camel and snake cases to bridge between MidoNet and Neutron APIs.  When
    the MidoNet API or cluster change to handle the snake case, remove this."""

    @convert_case
    def get(self, uri, media_type, params=None):
        return super(CaseAwareHttpClient, self).get(uri, media_type,
                                                    params=params)

    @convert_case
    def post(self, uri, media_type, body=None):
        return super(CaseAwareHttpClient, self).post(uri, media_type,
                                                     body=body)

    @convert_case
    def put(self, uri, media_type, body=None):
        return super(CaseAwareHttpClient, self).put(uri, media_type, body=body)
