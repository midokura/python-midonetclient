# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Route(ResourceBase):

    def create(self, tenant_id, router_uuid, type, srcNetworkAddr, srcNetworkLength,
                        dstNetworkAddr, dstNetworkLength, weight,
                        nextHopPort=None, nextHopGateway=None ):

        response, routers =  self.cl.routers().list(tenant_id)
        router_uri =  self._find_resource(routers, router_uuid)
        response, router =  self.cl.get(router_uri)
        uri = router['routes']
        data ={ "type": type,
                "srcNetworkAddr": srcNetworkAddr,
                "srcNetworkLength": srcNetworkLength, #int
                "dstNetworkAddr": dstNetworkAddr,
                "dstNetworkLength": dstNetworkLength, #int
                "weight": weight } #int

        if type == 'Normal':
            data["nextHopPort"] = nextHopPort
        if nextHopGateway:
            data["nextHopGateway"] = nextHopGateway

        return self.cl.post(uri, data)


    def list(self, tenant_id, router_uuid):
        response, routers =  self.cl.get(self.cl.routers_uri + "?tenant_id=" + tenant_id)
        router_uri =  self._find_resource(routers, router_uuid)
        response, router =  self.cl.get(router_uri)
        uri = router['routes']
        return self.cl.get(uri)

    def get(self, tenant_id, router_uuid, route_uuid):
        response, routers =  self.cl.routers().list(tenant_id)
        router_uri =  self._find_resource(routers, router_uuid)
        response, router =  self.cl.get(router_uri)

        response, routes = self.cl.get(router['routes'])
        route_uri = self._find_resource(routes, route_uuid)
        return self.cl.get(route_uri)



    def delete(self, tenant_id, router_uuid, route_uuid):
        response, routers =  self.cl.routers().list(tenant_id)
        router_uri =  self._find_resource(routers, router_uuid)
        response, router =  self.cl.get(router_uri)

        response, routes = self.cl.get(router['routes'])
        route_uri = self._find_resource(routes, route_uuid)

        return self.cl.delete(route_uri)

