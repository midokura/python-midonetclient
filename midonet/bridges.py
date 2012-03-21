# Copyright 2012 Midokura Japan KK

from resource import ResourceBase
            
class Bridge(ResourceBase):

    def create(self, tenant_id, name):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['bridges']
        data = {"name": name}
        return self.cl.post(uri, data)

    def list(self, tenant_id):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['bridges']
        return self.cl.get(uri)

    def update(self, tenant_id, bridge_uuid, name):
        response, content = self.cl.tenants().get(tenant_id)
        response, bridges =  self.cl.get(content['bridges'])
        bridge_uri = find_resource(bridges, bridge_uuid)

        data = {"name": name}
        return self.cl.put(bridge_uri, data)


    def get(self, tenant_id, bridge_uuid):
        response, content = self.cl.tenants().get(tenant_id)
        response, bridges =  self.cl.get(content['bridges'])
        bridge_uri = self._find_resource(bridges, bridge_uuid)

        return self.cl.get(bridge_uri)


    def delete(self, tenant_id, bridge_uuid):
        response, content = self.cl.tenants().get(tenant_id)
        response, bridges =  self.cl.get(content['bridges'])
        bridge_uri = self._find_resource(bridges, bridge_uuid)

        return self.cl.delete(bridge_uri)

