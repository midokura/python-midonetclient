# Copyright 2012 Midokura Japan KK



from resource import ResourceBase

class Router(ResourceBase):

    def create(self, tenant_id, name):
        body = {"name": name}
        path = 'tenants/%s/routers'% tenant_id
        return self.cl.post(path, body)

    def list(self, tenant_id):
        path = 'tenants/%s/routers'% tenant_id
        return self.cl.get(path)

    # get() and delete() are implemented in the super class
