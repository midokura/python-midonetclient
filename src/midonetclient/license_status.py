# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2014 Midokura SARL.
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
# @author: Alex Bikfalvi <alex.bikfalvi@midokura.com>, Midokura

from midonetclient import vendor_media_type
from midonetclient.resource_base import ResourceBase

class LicenseStatus(ResourceBase):

    media_type =  vendor_media_type.APPLICATION_LICENSE_STATUS_JSON_V1

    def __init__(self, uri, dto, auth):
        super(LicenseStatus, self).__init__(uri, dto, auth)

    def is_valid(self):
        return self.dto['valid']

    def get_message(self):
        return self.dto['message']
