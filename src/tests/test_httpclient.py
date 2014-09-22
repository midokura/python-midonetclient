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

from ddt import ddt, data
import mock
import unittest

from midonetclient import httpclient

FAKE_URL = "http://fake_url.com"
FAKE_USER = "fake_user"
FAKE_PWD = "fake_pwd"
FAKE_MEDIA_TYPE = "fake_media_type"

CASE_TEST_INPUT = [
    ({"fooBar": 0}, {"foo_bar": 0}),
    ([{"fooBar": 0}, {"fooBaz": 1}], [{"foo_bar": 0}, {"foo_baz": 1}])]


@ddt
class TestHttpClient(unittest.TestCase):

    def setUp(self):
        patcher = mock.patch('midonetclient.auth_lib.Auth')
        self.addCleanup(patcher.stop)
        mock_obj = patcher.start()
        self.mock_instance = mock_obj.return_value
        self.client = httpclient.CaseAwareHttpClient(FAKE_URL, FAKE_USER,
                                                     FAKE_PWD)

    def assert_request_body(self, body):
        self.mock_instance.do_request.assert_called_with(FAKE_URL, mock.ANY,
                                                         body=body,
                                                         headers=mock.ANY)

    @data(*CASE_TEST_INPUT)
    def test_get_with_case(self, d):
        camel, snake = d

        self.mock_instance.do_request.return_value = (None, camel)
        resp = self.client.get(FAKE_URL, FAKE_MEDIA_TYPE)

        self.assertTrue(cmp(snake, resp) == 0)

    @data(*CASE_TEST_INPUT)
    def test_post_with_case(self, d):
        camel, snake = d

        self.mock_instance.do_request.return_value = (None, camel)
        resp = self.client.post(FAKE_URL, FAKE_MEDIA_TYPE, body=snake)

        self.assert_request_body(camel)
        self.assertTrue(cmp(snake, resp) == 0)

    @data(*CASE_TEST_INPUT)
    def test_put_with_case(self, d):
        camel, snake = d

        self.mock_instance.do_request.return_value = (None, camel)
        resp = self.client.put(FAKE_URL, FAKE_MEDIA_TYPE, body=snake)

        self.assert_request_body(camel)
        self.assertTrue(cmp(snake, resp) == 0)
