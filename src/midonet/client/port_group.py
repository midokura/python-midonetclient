# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase

class PortGroup(ResourceBase):

    media_type = 'application/vnd.com.midokura.midolman.mgmt.PortGroup+json'

    def __init__(self, http, uri, dto):
        super(PortGroup, self).__init__(http, uri, dto)

    def name(self, name):
        self.dto['name'] = name
        return self

    def tenant_id(self, tenant_id):
        self.dto['tenantId'] = tenant_id
        return self

    def get_name(self):
        return self.dto['name']

    def get_id(self):
        return self.dto['id']

