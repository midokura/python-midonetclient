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

import logging

from midonetclient import url_provider, util
from midonetclient import vendor_media_type as mt

LOG = logging.getLogger(__name__)


class LicenseUrlProviderMixin(url_provider.UrlProviderMixin):
    """License URL provider mixin

    This mixin provides URLs for licenses.
    """

    def license_url(self, lic_id):
        return self.template_url("licenseTemplate", lic_id)

    def licenses_url(self):
        return self.resource_url("licenses")

    def license_status_url(self, lic_id):
        return self.license_url(lic_id) + "/status"


class LicenseClientMixin(LicenseUrlProviderMixin):
    """License mixin

    Mixin that defines all the Neutron license operations in MidoNet API.
    """

    @util.convert_case
    def create_license(self, lic):
        LOG.info("create_license %r", lic)
        return self.client.post(self.licenses_url(),
                                mt.APPLICATION_LICENSE_JSON, body=lic,
                                accept=mt.APPLICATION_OCTET_STREAM)

    def delete_license(self, lic_id):
        LOG.info("delete_license %r", lic_id)
        self.client.delete(self.license_url(lic_id))

    @util.convert_case
    def get_license(self, lic_id, fields=None):
        LOG.info("get_license %r", lic_id)
        return self.client.get(self.license_url(lic_id),
                               mt.APPLICATION_LICENSE_JSON)

    @util.convert_case
    def get_licenses(self, filters=None, fields=None, sorts=None, limit=None,
                     marker=None, page_reverse=False):
        LOG.info("get_licenses")
        return self.client.get(self.licenses_url(),
                               mt.APPLICATION_LICENSE_COLLECTION_JSON)

    @util.convert_case
    def get_license_status(self, lic_id):
        LOG.info("get_license_status %r", lic_id)
        return self.client.get(self.license_status_url(lic_id),
                               mt.APPLICATION_LICENSE_STATUS_JSON)
