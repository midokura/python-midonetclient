# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Port(ResourceBase):

    class RouterPort(ResourceBase):

        # create a materialized port
        def create(self, router_uuid,
                   networkAddress, networkLength, portAddress,
                   localNetworkAddress, localNetworkLength):

            uri = self.cl.midonet_uri +  'routers/%s/ports' % router_uuid
            data = { "networkAddress": networkAddress,
                     "networkLength": networkLength, #int
                     "portAddress": portAddress,
                     "localNetworkAddress": localNetworkAddress,
                     "localNetworkLength": localNetworkLength } #int
            return self.cl.post(uri, data)

        def list(self, router_uuid):
            uri = self.cl.midonet_uri + 'routers/%s/ports' % router_uuid
            return self.cl.get(uri)

        # get and delete are implemented in the super class.


    class BridgePort(ResourceBase):

        def create(self, bridge_uuid):
            uri = self.cl.midonet_uri + 'bridges/%s/ports' % bridge_uuid
            return self.cl.post(uri, {})

        def list(self, bridge_uuid):
            uri = self.cl.midonet_uri + 'bridges/%s/ports' % bridge_uuid
            return self.cl.get(uri)


