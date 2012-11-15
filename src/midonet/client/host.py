# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase

from host_interface import HostInterface
from host_interface_port import HostInterfacePort


class Host(ResourceBase):

    media_type = 'application/vnd.com.midokura.midolman.mgmt.Host+json'

    def __init__(self, http, uri, dto):
        super(Host, self).__init__(http, uri, dto)

    def get_id(self):
        return self.dto['id']

    def get_name(self):
        return self.dto['name']

    def is_alive(self):
        return self.dto['alive']

    def get_addresses(self):
        return self.dto['addresses']

    def get_interfaces(self, query):
        headers = {'Content-Type': 'application/vnd.com.midokura.midolman.mgmt.collection.Interface+json'}
        return self.get_children(self.dto['interfaces'], query, headers, HostInterface)

    def get_ports(self):
        headers = {'Content-Type': 'application/vnd.com.midokura.midolman.mgmt.collection.Interface+json'}
        query = {}
        return self.get_children(self.dto['ports'], query, headers, HostInterfacePort)

    def add_host_interface_port(self):
        return HostInterfacePort(self.web_resource, self.dto['ports'], {})


