# Copyright 2012 Midokura Japan KK

from resource import ResourceBase
            
class DhcpHost(ResourceBase):

    def create(self, tenant_id, bridge_uuid, subnet, mac, ip, name=None):
        response, dhcp = self.cl.dhcps().get(tenant_id, bridge_uuid, subnet)
        uri =  dhcp['hosts']
        data = {
            "macAddr": mac,
            "ipAddr": ip,
            "name": name
            } 
        return self.cl.post(uri, data)

    def list(self, tenant_id, bridge_uuid, subnet):
        response, dhcp = self.cl.dhcps().get(tenant_id, bridge_uuid, subnet)
        uri =  dhcp['hosts']
        return self.cl.get(uri)

    def get(self, tenant_id, bridge_uuid, subnet, mac):
        response, dhcp = self.cl.dhcps().get(tenant_id, bridge_uuid, subnet)
        uri =  dhcp['hosts'] + '/' +  mac
        return self.cl.get(uri)

    def delete(self, tenant_id, bridge_uuid, subnet, mac):
        response, dhcp = self.cl.dhcps().get(tenant_id, bridge_uuid, subnet)
        uri =  dhcp['hosts'] + '/' +  mac
        return self.cl.delete(uri)

