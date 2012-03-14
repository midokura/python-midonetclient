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
        uri =  content['routers']
        return self.cl.get(uri)

    def update(self, bridge_uuid, name):

        data = {"name": name}
        uri = self.uri + '/' + bridge_uuid
        return self.cl.put(uri, data)

    # get() and delete() are implemented in the super class

