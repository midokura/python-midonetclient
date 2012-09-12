# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase

class AdRoute(ResourceBase):

    media_type = 'application/vnd.com.midokura.midolman.mgmt.AdRoute+json'

    def __init__(self, http, uri, dto):
        super(AdRoute, self).__init__(http, uri, dto)

    def get_id(self):
        return self.dto['id']

    def get_nw_prefix(self):
        return self.dto['nwPrefix']

    def get_prefix_length(self):
        return self.dto['prefixLength']

    def nw_prefix(self, nw):
        self.dto['nwPrefix'] = nw
        return self

    def nw_prefix_length(self, length):
        self.dto['prefixLength'] = length
        return self

