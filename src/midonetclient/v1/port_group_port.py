# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
import vendor_media_type

class PortGroupPort(ResourceBase):

    media_type = vendor_media_type.APPLICATION_PORTGROUP_PORT_JSON

    def __init__(self, http, uri, dto):
        super(PortGroupPort, self).__init__(http, uri, dto)

    def get_port_group_id(self):
        return self.dto['portGroupId']

    def get_port_id(self):
        return self.dto['portId']

    def get_port_group(self):
        return self.dto['portGroup']

    def get_port(self):
        return self.dto['port']

    def port_id(self, id_):
        self.dto['portId'] = id_
        return self

