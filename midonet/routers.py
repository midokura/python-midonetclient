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

    def update(self, router_uuid, name):

        body = {"name": name}
        path = self.path + '/' + router_uuid
        return self.cl.put(path, body)

    # get() and delete() are implemented in the super class

    def link_create(self, router_uuid,
             network_address, network_length,
             port_address, peer_port_address,  peer_router_uuid):

        path = 'routers/%s/routers' % router_uuid

        body = {
            "networkAddress": network_address,
            "networkLength": network_length,
            "portAddress": port_address,
            "peerPortAddress": peer_port_address,
            "peerRouterId": peer_router_uuid
            }
        return self.cl.post(path, body)


    def link_list(self, router_uuid):
        path = 'routers/%s/routers' % router_uuid
        return self.cl.get(path)


    def link_get(self, router_id, peer_router_id):
       path = 'routers/%s/routers/%s' % (router_id, peer_router_id)
       return self.cl.get(path)


    def link_delete(self, router_id, peer_router_id):
       path = 'routers/%s/routers/%s' % (router_id, peer_router_id)
       return self.cl.delete(path)
