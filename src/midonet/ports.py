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

        # create a port
        def create(self, tenant_id, router_uuid, type_,
                   networkAddress, networkLength, portAddress,
                   localNetworkAddress=None, localNetworkLength=None,
                   inbound_filter_id=None, outbound_filter_id=None,
                   vif_id=None):

            uri = self._ports_uri(tenant_id, router_uuid)
            data = { "type": type_,
                     "networkAddress": networkAddress,
                     "networkLength": networkLength, #int
                     "portAddress": portAddress,
                     "localNetworkAddress": localNetworkAddress,
                     "localNetworkLength": localNetworkLength,  #int
                     "inboundFilterId": inbound_filter_id,
                     "outboundFilterId": outbound_filter_id,
                     "vifId": vif_id}
            return self.cl.post(uri, data)

        def list(self, tenant_id, router_uuid):
            uri = self._ports_uri(tenant_id, router_uuid)
            return self.cl.get(uri)

        def get(self, tenant_id, router_uuid, port_uuid):
            port_uri = self._port_uri(tenant_id, router_uuid, port_uuid)
            return self.cl.get(port_uri)

        def update(self, tenant_id, router_uuid, port_uuid, data):
            port_uri = self._port_uri(tenant_id, router_uuid, port_uuid)
            return self.cl.put(port_uri, data)

        def delete(self, tenant_id, router_uuid, port_uuid):
            port_uri = self._port_uri(tenant_id, router_uuid, port_uuid)
            return self.cl.delete(port_uri)

        def link(self, tenant_id, router_uuid, port_uuid, peer_id):
            response, port = self.get(tenant_id, router_uuid, port_uuid)
            link_uri = port['link']
            data = {'peerId': peer_id}
            return self.cl.post(link_uri, data)

        def unlink(self, tenant_id, router_uuid, port_uuid):
            response, port = self.get(tenant_id, router_uuid, port_uuid)
            link_uri = port['link']
            data = {'peerId': None}
            return self.cl.post(link_uri, data)


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


        def create(self, tenant_id, bridge_uuid, type_, inbound_filter_id=None,
                   outbound_filter_id=None, port_group_ids=None):
            uri = self._ports_uri(tenant_id, bridge_uuid)
            data = { 'type': type_,
                     'inboundFilterId': inbound_filter_id,
                     'outboundFilterId': outbound_filter_id,
                     'portGroupIDs': port_group_ids
                     }
            return self.cl.post(uri, data)

        def list(self, tenant_id, bridge_uuid):
            uri = self._ports_uri(tenant_id, bridge_uuid)
            return self.cl.get(uri)

        def get(self, tenant_id, bridge_uuid, port_uuid):
            port_uri = self._port_uri(tenant_id, bridge_uuid, port_uuid)
            return self.cl.get(port_uri)

        def update(self, tenant_id, bridge_uuid, port_uuid, data):
            port_uri = self._port_uri(tenant_id, bridge_uuid, port_uuid)
            return self.cl.put(port_uri, data)

        def delete(self, tenant_id, bridge_uuid, port_uuid):
            port_uri = self._port_uri(tenant_id, bridge_uuid, port_uuid)
            return self.cl.delete(port_uri)

        def link(self, tenant_id, bridge_uuid, port_uuid, peer_id):
            response, port = self.get(tenant_id, bridge_uuid, port_uuid)
            link_uri = port['link']
            data = {'peerId': peer_id}
            return self.cl.post(link_uri, data)

        def unlink(self, tenant_id, bridge_uuid, port_uuid):
            response, port = self.get(tenant_id, bridge_uuid, port_uuid)
            link_uri = port['link']
            data = {'peerId': None}
            return self.cl.post(link_uri, data)
