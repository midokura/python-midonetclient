# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase

class Host(ResourceBase):

    media_type = 'application/vnd.com.midokura.midolman.mgmt.Host+json'

    def __init__(self, http, uri, dto):
        super(Host, self).__init__(http, uri, dto)

    def get_id(self):
        return self.dto['id']

    def get_name(self):
        return self.dto['name']

    def get_interfaces(self):
        return self.dto['interfaces']

    def is_alive(self):
        return self.dto['alive']

    def get_addresses(self):
        return self.dto['addresses']

    #TODO: add interface port map
