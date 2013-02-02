# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from rule import Rule
import vendor_media_type

class Chain(ResourceBase):

    media_type = vendor_media_type.APPLICATION_CHAIN_JSON

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
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_RULE_COLLECTION_JSON}

        return self.get_children(self.dto['rules'], query, headers,
                                 Rule)
    def add_rule(self):
        return Rule(self.web_resource, self.dto['rules'], {})



