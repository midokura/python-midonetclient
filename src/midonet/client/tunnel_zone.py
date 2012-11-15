# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase

class TunnelZone(ResourceBase):

    media_type = 'application/vnd.com.midokura.midolman.mgmt.TunnelZone+json'


    def __init__(self, http, uri, dto):
        super(TunnelZone, self).__init__(http, uri, dto)

    def name(self, name):
        self.dto['name'] = name
        return self

    def type(self, type_):
        self.dto['type'] = type_
        return self

    def get_name(self):
        return self.dto['name']

    def get_type(self):
        return self.dto['type']

    def get_id(self):
        return self.dto['id']

