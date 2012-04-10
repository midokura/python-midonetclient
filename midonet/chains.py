# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Chain(ResourceBase):


    def create(self, router_uuid, name, table="NAT"):
        uri = self.cl.midonet_uri +  'routers/%s/chains' % router_uuid
        data = { "name": name, "table": table }
        return self.cl.post(uri, data)

    def list(self, router_uuid):
        uri = self.cl.midonet_uri + 'routers/%s/chains' % router_uuid
        return self.cl.get(uri)


