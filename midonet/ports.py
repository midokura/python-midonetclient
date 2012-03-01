# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Port(ResourceBase):

    path = 'ports'

    class RouterPort(ResourceBase):

        # create a materialized port
        def create(self, router_uuid,
                   networkAddress, networkLength, portAddress,
                   localNetworkAddress, localNetworkLength):

            path = 'routers/%s/ports' % router_uuid
            data = { "networkAddress": networkAddress,
                     "networkLength": networkLength, #int
                     "portAddress": portAddress,
                     "localNetworkAddress": localNetworkAddress,
                     "localNetworkLength": localNetworkLength } #int
            return self.cl.post(path, data)

        def list(self, router_uuid):
            path = 'routers/%s/ports' % router_uuid
            return self.cl.get(path)

        # get and delete are implemented in the super class.


    class BridgePort(ResourceBase):

        def create(self, bridge_uuid):
            path = 'bridges/%s/ports' % bridge_uuid
            return self.cl.post(url, {})

        def list(self, bridge_uuid):
            path = 'bridges/%s/ports' % bridge_uuid
            return self.cl.get(path)


