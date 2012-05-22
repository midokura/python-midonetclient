# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Chain(ResourceBase):

    def _chains_uri(self, tenant_id):
        response, tenant = self.cl.tenants().get(tenant_id)
        return  tenant['chains']

    def _chain_uri(self, tenant_id, chain_uuid):
        response, chains = self.list(tenant_id)
        return self._find_resource(chains, chain_uuid)

    def create(self, tenant_id, name):
        uri = self._chains_uri(tenant_id )
        data = { "name": name }
        return self.cl.post(uri, data)

    def list(self, tenant_id):
        uri = self._chains_uri(tenant_id)
        return self.cl.get(uri)

    def get(self, tenant_id, chain_uuid):
        chain_uri = self._chain_uri(tenant_id, chain_uuid)
        return self.cl.get(chain_uri)

    def delete(self, tenant_id, chain_uuid):
        chain_uri = self._chain_uri(tenant_id, chain_uuid)
        return self.cl.delete(chain_uri)

