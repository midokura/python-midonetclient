# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from dhcp_host import DhcpHost
import vendor_media_type

class DhcpSubnet(ResourceBase):

    media_type = vendor_media_type.APPLICATION_DHCP_SUBNET_JSON

    def __init__(self, http, uri, dto):
        super(DhcpSubnet, self).__init__(http, uri, dto)

    def get_default_gateway(self):
        return self.dto['defaultGateway']

    def get_subnet_prefix(self):
        return self.dto['subnetPrefix']

    def get_subnet_length(self):
        return self.dto['subnetLength']

    def default_gateway(self, gw):
        self.dto['defaultGateway'] = gw
        return self

    def subnet_prefix(self, prefix):
        self.dto['subnetPrefix'] = prefix
        return self

    def subnet_length(self, length):
        self.dto['subnetLength'] = length
        return self

    def get_dhcp_hosts(self):
        query = {}
        headers = {'Content-Type':
                       vendor_media_type.APPLICATION_DHCP_HOST_COLLECTION_JSON}
        return self.get_children(self.dto['hosts'], query, headers,
                                 DhcpHost)

    def add_dhcp_host(self):
        return DhcpHost(self.web_resource, self.dto['hosts'], {})

