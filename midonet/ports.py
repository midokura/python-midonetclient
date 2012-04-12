# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Port(ResourceBase):

    class RouterPort(ResourceBase):

        def _ports_uri(self, tenant_id, router_uuid):
            response, content = self.cl.tenants().get(tenant_id)
            response, routers =  self.cl.get(content['routers'])
            router_uri =  self._find_resource(routers, router_uuid)
            response, router =  self.cl.get(router_uri)
            return  router['ports'] 

        def _port_uri(self, tenant_id, router_uuid, port_uuid):
            ports_uri = self._ports_uri(tenant_id, router_uuid)
            response, ports =  self.cl.get(ports_uri)
            return self._find_resource(ports, port_uuid)

        # create a materialized port
        def create(self, tenant_id, router_uuid,
                   networkAddress, networkLength, portAddress,
                   localNetworkAddress, localNetworkLength):

            uri = self._ports_uri(tenant_id, router_uuid)
            data = { "networkAddress": networkAddress,
                     "networkLength": networkLength, #int
                     "portAddress": portAddress,
                     "localNetworkAddress": localNetworkAddress,
                     "localNetworkLength": localNetworkLength}  #int
            return self.cl.post(uri, data)

        def list(self, tenant_id, router_uuid):
            uri = self._ports_uri(tenant_id, router_uuid)
            return self.cl.get(uri)

        def get(self, tenant_id, router_uuid, port_uuid):
            port_uri = self._port_uri(tenant_id, router_uuid, port_uuid)
            return self.cl.get(port_uri)

        def delete(self, tenant_id, router_uuid, port_uuid):
            port_uri = self._port_uri(tenant_id, router_uuid, port_uuid)
            return self.cl.delete(port_uri)


    class BridgePort(ResourceBase):

        def _ports_uri(self, tenant_id, bridge_uuid):
            response, content = self.cl.tenants().get(tenant_id)
            response, bridges =  self.cl.get(content['bridges'])
            bridge_uri =  self._find_resource(bridges, bridge_uuid)
            response, bridge =  self.cl.get(bridge_uri)
            return  bridge['ports'] 

        def _port_uri(self, tenant_id, bridge_uuid, port_uuid):
            ports_uri = self._ports_uri(tenant_id, bridge_uuid)
            response, ports =  self.cl.get(ports_uri)
            return self._find_resource(ports, port_uuid)


        def create(self, tenant_id, bridge_uuid):
            uri = self._ports_uri(tenant_id, bridge_uuid)
            return self.cl.post(uri, {})

        def list(self, tenant_id, router_uuid):
            uri = self._ports_uri(tenant_id, router_uuid)
            return self.cl.get(uri)

        def get(self, tenant_id, router_uuid, port_uuid):
            port_uri = self._port_uri(tenant_id, router_uuid, port_uuid)
            return self.cl.get(port_uri)

        def delete(self, tenant_id, router_uuid, port_uuid):
            port_uri = self._port_uri(tenant_id, router_uuid, port_uuid)
            return self.cl.delete(port_uri)
