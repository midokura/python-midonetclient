# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
import vendor_media_type

class AdRoute(ResourceBase):

    media_type = vendor_media_type.APPLICATION_AD_ROUTE_JSON

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

