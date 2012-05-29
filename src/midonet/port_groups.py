# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class PortGroup(ResourceBase):

    vender_media_type = \
            'application/vnd.com.midokura.midolman.mgmt.PortGroup+json'
    vender_media_type_collection = \
        'application/vnd.com.midokura.midolman.mgmt.collection.PortGroup+json'

    def _get_pg_uri(self, tenant_id, port_group_id):
        response, pgs = self.list(tenant_id)
        return self._find_resource(pgs, port_group_id)

    def create(self, tenant_id, name):
        response, tenant = self.cl.tenants().get(tenant_id)
        data = {'tenantId': tenant_id, 'name': name}
        headers = {'Content-Type': self.vender_media_type}
        return self.cl.post(tenant['portGroups'], data, headers)

    def list(self, tenant_id):
        response, tenant = self.cl.tenants().get(tenant_id)
        headers = {'Accept': self.vender_media_type_collection}
        return self.cl.get(tenant['portGroups'], headers)

    def get(self, tenant_id, port_group_id):
        headers = {'Accept': self.vender_media_type}
        return self.cl.get(self._get_pg_uri(tenant_id, port_group_id), headers)

    def delete(self, tenant_id, port_group_id):
        return self.cl.delete(self._get_pg_uri(tenant_id, port_group_id))
