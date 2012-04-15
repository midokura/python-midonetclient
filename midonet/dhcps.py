# Copyright 2012 Midokura Japan KK

from resource import ResourceBase
            
class Dhcp(ResourceBase):

    def create(self, tenant_id, bridge_uuid, subnet_addr, subnet_length, gateway ):
        response, bridge = self.cl.bridges().get(tenant_id, bridge_uuid)
        uri =  bridge['dhcpSubnets']
        data = {
            "subnetPrefix": subnet_addr,
            "subnetLength": subnet_length,
            "defaultGateway": gateway
            } 
        return self.cl.post(uri, data)

    def list(self, tenant_id, bridge_uuid):
        response, bridge = self.cl.bridges().get(tenant_id, bridge_uuid)
        uri =  bridge['dhcpSubnets']
        return self.cl.get(uri)

    def get(self, tenant_id, bridge_uuid, subnet):
        response, bridge = self.cl.bridges().get(tenant_id, bridge_uuid)
        uri =  bridge['dhcpSubnets'] + '/' + subnet
        return self.cl.get(uri)

    def delete(self, tenant_id, bridge_uuid, subnet):
        response, bridge = self.cl.bridges().get(tenant_id, bridge_uuid)
        uri =  bridge['dhcpSubnets'] + '/' + subnet
        return self.cl.delete(uri)

