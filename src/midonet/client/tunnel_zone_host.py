# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase

class TunnelZoneHost(ResourceBase):

    def __init__(self, http, uri, dto):
        super(TunnelZoneHost, self).__init__(http, uri, dto, mt)
        self.media_type = mt

    def host_id(self, host_id):
        self.dto['hostId'] = host_id
        return self

    def ip_address(self, ip_address):
        self.dto['ipAddress'] = ip_address
        return self

    def get_tunnel_zone_id(self):
        return self.dto['tunnelZoneId']

    def get_host_id(self):
        return self.dto['hostId']

    def get_ip_address(self):
        return self.dto['ipAddress']

