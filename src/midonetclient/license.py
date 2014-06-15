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

class License(ResourceBase):

    media_type = vendor_media_type.APPLICATION_LICENSE_JSON_V1

    def __init__(self, uri, dto, auth):
        super(License, self).__init__(uri, dto, auth)

    def get_id(self):
        return self.dto['id']

    def get_issuer(self):
        return self.dto['issuerX500']

    def get_holder(self):
        return self.dto['holderX500']

    def get_issue_date(self):
        return self.dto['issueDate']

    def get_start_date(self):
        return self.dto['startDate']

    def get_end_date(self):
        return self.dto['endDate']

    def get_product(self):
        return self.dto['product']

    def get_description(self):
        return self.dto['description']

    def get_agent_quota(self):
        return self.dto['extra']['agentQuota']

    def is_valid(self):
        return self.dto['valid']