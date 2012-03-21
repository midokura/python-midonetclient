# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Router(ResourceBase):

    def create(self, tenant_id, name):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['routers']
        data = {"name": name}
        return self.cl.post(uri, data)

    def list(self, tenant_id):
        response, content = self.cl.tenants().get(tenant_id)
        uri =  content['routers']
        return self.cl.get(uri)

    def update(self, tenant_id, router_uuid, name):
        response, content = self.cl.tenants().get(tenant_id)
        response, routers =  self.cl.get(content['routers'])
        router_uri =  find_resource(routers, router_uuid)
        data = {"name": name}
        return self.cl.put(router_uri, data)

    def get(self, tenant_id, router_uuid):
        response, content = self.cl.tenants().get(tenant_id)
        response, routers =  self.cl.get(content['routers'])
        router_uri = self._find_resource(routers, router_uuid)

        return self.cl.get(router_uri)

    def delete(self, tenant_id, router_uuid):
        response, content = self.cl.tenants().get(tenant_id)
        response, routers =  self.cl.get(content['routers'])
        router_uri = self._find_resource(routers, router_uuid)

        return self.cl.delete(router_uri)


    def link_router_create(self, tenant_id, router_uuid,
             network_address, network_length,
             port_address, peer_port_address,  peer_router_uuid):

        response, content = self.get(tenant_id, router_uuid)
        uri = content['peerRouters']
        data = {
            "networkAddress": network_address,
            "networkLength": network_length,
            "portAddress": port_address,
            "peerPortAddress": peer_port_address,
            "peerRouterId": peer_router_uuid
            }
        return self.cl.post(uri, data)

    def link_router_list(self, tenant_id, router_uuid):
        response, content = self.get(tenant_id, router_uuid)
        uri = content['peerRouters']
        return self.cl.get(uri)

    def link_router_get(self, tenant_id, router_uuid, peer_router_uuid):
        response, content = self.get(tenant_id, router_uuid)
        uri = content['peerRouters'] + '/' + peer_router_uuid
        return self.cl.get(uri)

    def link_router_delete(self, tenant_id, router_uuid, peer_router_uuid):
        response, content = self.get(tenant_id, router_uuid)
        uri = content['peerRouters'] + '/' + peer_router_uuid
        return self.cl.delete(uri)

    def link_bridge_create(self, tenant_id, router_uuid,
             network_address, network_length,
             port_address, bridge_uuid):

        response, content = self.get(tenant_id, router_uuid)
        uri = content['bridges']
        data = {
            "networkAddress": network_address,
            "networkLength": network_length,
            "portAddress": port_address,
            "bridgeId": bridge_uuid
            }
        return self.cl.post(uri, data)


    def link_bridge_list(self, tenant_id, router_uuid):
        response, content = self.get(tenant_id, router_uuid)
        uri = content['bridges']
        return self.cl.get(uri)


    def link_bridge_get(self, tenant_id, router_uuid, bridge_uuid):
        response, content = self.get(tenant_id, router_uuid)
        uri = content['bridges'] + '/' + bridge_uuid
        return self.cl.get(uri)

    def link_bridge_delete(self, tenant_id, router_uuid, bridge_uuid):
        response, content = self.get(tenant_id, router_uuid)
        uri = content['bridges'] + '/' + bridge_uuid
        return self.cl.delete(uri)

