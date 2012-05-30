# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Router(ResourceBase):

    def _router_uri(self, tenant_id, router_uuid):
        response, content = self.cl.tenants().get(tenant_id)
        response, routers =  self.cl.get(content['routers'])
        return self._find_resource(routers, router_uuid)

    def create(self, tenant_id, name, router_id=None):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['routers']
        data = {"name": name}
        if router_id:
            data['id'] = router_id
        return self.cl.post(uri, data)

    def list(self, tenant_id):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['routers']
        return self.cl.get(uri)

    def update(self, tenant_id, router_uuid, name, inbound_filter,
               outbound_filter):
        router_uri = self._router_uri(tenant_id, router_uuid)
        data = {'name': name, 'inboundFilter': inbound_filter,
                'outboundFilter': outbound_filter}
        return self.cl.put(router_uri, data)

    def get(self, tenant_id, router_uuid):
        router_uri = self._router_uri(tenant_id, router_uuid)
        return self.cl.get(router_uri)

    def delete(self, tenant_id, router_uuid):
        router_uri = self._router_uri(tenant_id, router_uuid)
        return self.cl.delete(router_uri)
