# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
import vendor_media_type

class HostInterface(ResourceBase):

    media_type = vendor_media_type.APPLICATION_HOST_INTERFACE_PORT_JSON

    def __init__(self, http, uri, dto):
        super(Host, self).__init__(http, uri, dto)

    def get_addresses(self):
        return self.dto['addresses']

    def get_endpoint(self):
        return self.dto['endpoint']

    def get_host_id(self):
        return self.dto['hostId']

    def get_id(self):
        return self.dto['id']

    def get_mac(self):
        return self.dto['mac']

    def get_mtu(self):
        return self.dto['mtu']

    def get_name(self):
        return self.dto['name']

    def get_status(self):
        return self.dto['status']

    def get_status(self):
        return self.dto['status']

    def get_status_field(self, status_type):
        #TODO
        pass

    def get_type(self):
        return self.dto['type']
