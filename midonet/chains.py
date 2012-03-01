# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Chain(ResourceBase):

    path = 'chains'

    def create(self, router_uuid, name, table="NAT"):
        path = 'routers/%s/chains' % router_uuid
        data = { "name": name, "table": table }
        return self.cl.post(path, data)

    def list(self, router_uuid):
        path = 'routers/%s/chains' % router_uuid
        return self.cl.get(path)


