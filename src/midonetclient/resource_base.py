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

from webob import exc


class ResourceBase(object):

    media_type = None

    def __init__(self, uri, dto, auth):
        self.uri = uri
        self.dto = dto
        self.auth = auth

    def _ensure_media_type(self, key, headers):
        if not(key in headers and headers[key]):
            if self.media_type:
                headers[key] = self.media_type
            else:
                headers[key] = 'application/json'

    def _ensure_content_type(self, headers):
        self._ensure_media_type('Content-Type', headers)

    def _ensure_accept(self, headers):
        self._ensure_media_type('Accept', headers)

    def create(self, headers=None):
        if headers == None:
            headers = {}
        self._ensure_content_type(headers)
        resp, data = self.auth.do_request(self.uri, 'POST', body=self.dto,
                                          headers=headers)

        self._ensure_accept(headers)
        res, self.dto = self.auth.do_request(resp['location'], 'GET',
                                             headers=headers)
        return self

    def get(self, headers=None, **kwargs):
        if headers == None:
            headers = {}
        self._ensure_accept(headers)
        uri = self.dto['uri']
        res, self.dto = self.auth.do_request(uri, 'GET', headers=headers)
        return self

    def get_children(self, uri, query, headers, clazz, extra_args=None):
        self._ensure_accept(headers)
        resources = []
        res, dtos = self.auth.do_request(uri, 'GET', query=query,
                                         headers=headers)
        if dtos is None:  # work around for hosts API returning empty when
                          # there's no hosts
            return resources
        for dto in dtos:
            if extra_args is None:
                resources.append(clazz(uri, dto, self.auth))
            else:
                resources.append(clazz(uri, dto, self.auth, *extra_args))
        return resources

    def get_uri(self):
        return self.dto['uri']

    def update(self, headers=None):
        if headers == None:
            headers = {}
        self._ensure_content_type(headers)
        resp, body = self.auth.do_request(self.dto['uri'], 'PUT',
                                          body=self.dto, headers=headers)
        if self.media_type:
            headers['Accept'] = self.media_type
        resp, self.dto = self.auth.do_request(self.dto['uri'], 'GET',
                                              headers=headers)
        return self

    def delete(self, headers={}):
        resp, junk = self.auth.do_request(self.dto['uri'], 'DELETE',
                                          headers=headers)
        return None

    def __repr__(self):
        return self.__class__.__name__ + str(self.dto)
