# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Host(ResourceBase):

    def list(self):
        return self.cl.get(self.cl.hosts_uri)

    def get(self, host_id):
        res, hosts = self.list()
        return self._find_resource(hosts, host_id)

    def get_interface_port_map(self, host_id):
        res, host = self.get(host_id)
        return self.cl.get(host['interfacePortMap'])

    def add_interface_port_map(self, host_id, port_id, if_name):
        res, host = self.get(host_id)
        data = {"portId": port_id , "interfaceName": if_name }
        return selfcl.post(host['interfacePortMap'], data)


    def del_interface_port_map(self, host_id, port_id):
        res, host = self.get(host_id)
        data = {"portId": port_id}
        return selfcl.post(host['interfacePortMap'], data)




