# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Chain(ResourceBase):

    def _chains_uri(self, tenant_id, router_uuid):
        response, content = self.cl.tenants().get(tenant_id)
        response, routers =  self.cl.get(content['routers'])
        router_uri =  self._find_resource(routers, router_uuid)
        response, router =  self.cl.get(router_uri)
        return  router['chains'] 

    def _chain_uri(self, tenant_id, router_uuid, chain_uuid):
        chains_uri = self._chains_uri(tenant_id, router_uuid)
        response, chains =  self.cl.get(chains_uri)
        return self._find_resource(chains, chain_uuid)

    def create(self, tenant_id, router_uuid, name, table="NAT"):
        uri = self._chains_uri(tenant_id, router_uuid)
        data = { "name": name, "table": table }
        return self.cl.post(uri, data)

    def list(self, tenant_id, router_uuid):
        uri = self._chains_uri(tenant_id, router_uuid)
        return self.cl.get(uri)

    def get(self, tenant_id, router_uuid, chain_uuid):
        chain_uri = self._chain_uri(tenant_id, router_uuid, chain_uuid)
        return self.cl.get(chain_uri)

    def delete(self, tenant_id, router_uuid, chain_uuid):
        chain_uri = self._chain_uri(tenant_id, router_uuid, chain_uuid)
        return self.cl.delete(chain_uri)


