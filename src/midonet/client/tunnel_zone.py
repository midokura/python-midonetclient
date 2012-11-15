# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase

class TunnelZone(ResourceBase):

    def __init__(self, http, uri, dto, mt, lmt):
        super(TunnelZone, self).__init__(http, uri, dto)
        self.tunnel_zone_host_media_type = mt
        self.tunnel_zone_host_list_media_type = lmt

    def name(self, name):
        self.dto['name'] = name
        return self

    def get_name(self):
        return self.dto['name']

    def get_type(self):
        return self.dto['type']

    def get_id(self):
        return self.dto['id']
