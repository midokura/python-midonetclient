# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from tunnel_zone_host import TunnelZoneHost

class TunnelZone(ResourceBase):

    def __init__(self, http, uri, dto, mt=None, lmt=None):
        super(TunnelZone, self).__init__(http, uri, dto)
        self.tunnel_zone_host_media_type = mt
        self.tunnel_zone_host_list_media_type = lmt

    def _get_tunnel_zone_host_media_type(self):
        if self.tunnel_zone_host_media_type:
            return self.tunnel_zone_host_media_type
        elif self.dto.get('type') == 'gre':
            return 'application/vnd.com.midokura.midolman.mgmt.GreTunnelZoneHost+json'
        elif self.dto.get('type') == 'capwap':
            return 'application/vnd.com.midokura.midolman.mgmt.CapwapTunnelZoneHost+json'


    def _get_tunnel_zone_host_list_media_type(self):
        if self.tunnel_zone_host_list_media_type:
            return self.tunnel_zone_host_list_media_type
        elif self.dto.get('type') == 'gre':
            return 'application/vnd.com.midokura.midolman.mgmt.collection.GreTunnelZoneHost+json'
        elif self.dto.get('type') == 'capwap':
            return 'application/vnd.com.midokura.midolman.mgmt.collection.CapwapTunnelZoneHost+json'

    def name(self, name):
        self.dto['name'] = name
        return self

    def get_name(self):
        return self.dto['name']

    def get_type(self):
        return self.dto['type']

    def get_id(self):
        return self.dto['id']

    def get_hosts(self):
        headers = {'Content-Type': self._get_tunnel_zone_host_list_media_type(),
                   'Accept': self._get_tunnel_zone_host_list_media_type()}
        query={}
        return self.get_children(self.dto['hosts'], query, headers,
                TunnelZoneHost, [self._get_tunnel_zone_host_media_type()])

    def add_tunnel_zone_host(self):
        return TunnelZoneHost(self.web_resource, self.dto['hosts'], {},
                              self._get_tunnel_zone_host_media_type())

