# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from port_group_port import PortGroupPort
import vendor_media_type

class PortGroup(ResourceBase):

    media_type = vendor_media_type.APPLICATION_PORTGROUP_JSON

    def __init__(self, http, uri, dto):
        super(PortGroup, self).__init__(http, uri, dto)

    def name(self, name):
        self.dto['name'] = name
        return self

    def tenant_id(self, tenant_id):
        self.dto['tenantId'] = tenant_id
        return self

    def get_name(self):
        return self.dto['name']

    def get_id(self):
        return self.dto['id']

    def get_ports(self, query={}):
        headers = {'Content-Type':
                       vendor_media_type.\
                       APPLICATION_PORTGROUP_PORT_COLLECTION_JSON}
        return self.get_children(self.dto['ports'], query, headers,
                                 PortGroupPort)


    def add_port_group_port(self):
        return PortGroupPort(self.web_resource, self.dto['ports'], {})
