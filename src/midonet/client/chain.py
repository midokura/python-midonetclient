# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from rule import Rule

class Chain(ResourceBase):

    media_type = 'application/vnd.com.midokura.midolman.mgmt.Chain+json'

    def __init__(self, http, uri, dto):
        super(Chain, self).__init__(http, uri, dto)

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

    def get_rules(self):
        query = {}
        headers = \
            {'Content-Type':
             'application/vnd.com.midokura.midolman.mgmt.collection.Rule+json'}
        return self.get_children(self.dto['rules'], query, headers,
                                 Rule)
    def add_rule(self):
        return Rule(self.web_resource, self.dto['rules'], {})



