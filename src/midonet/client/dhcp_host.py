# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase

class DhcpHost(ResourceBase):

    media_type = \
        'application/vnd.com.midokura.midolman.mgmt.DhcpHost+json'

    def __init__(self, http, uri, dto):
        super(DhcpHost, self).__init__(http, uri, dto)

    def get_name(self):
        return self.dto['name']

    def get_ip_addr(self):
        return self.dto['ipAddr']

    def get_mac_addr(self):
        return self.dto['macAddr']

    def name(self, name):
        self.dto['name'] = name
        return self

    def ip_addr(self, ipaddr):
        self.dto['ipAddr'] = ipaddr
        return self

    def mac_addr(self, macaddr):
        self.dto['macAddr'] = macaddr
        return self





