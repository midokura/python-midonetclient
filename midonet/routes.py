# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Route(ResourceBase):

    def create(self, router_uuid, type, srcNetworkAddr, srcNetworkLength,
                        dstNetworkAddr, dstNetworkLength, weight,
                        nextHopPort=None, nextHopGateway=None ):

        path =  'routers/%s/routes' % router_uuid
        body ={ "type": type,
                "srcNetworkAddr": srcNetworkAddr,
                "srcNetworkLength": srcNetworkLength, #int
                "dstNetworkAddr": dstNetworkAddr,
                "dstNetworkLength": dstNetworkLength, #int
                "weight": weight } #int

        if type == 'Normal':
            body["nextHopPort"] = nextHopPort
        if nextHopGateway:
            body["nextHopGateway"] = nextHopGateway

        return self.cl.post(path, body)


    def list(self, router_uuid):
        path = 'routers/%s/routes' % router_uuid
        return self.cl.get(path)

