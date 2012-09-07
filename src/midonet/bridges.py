# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Bridge(ResourceBase):

    def _bridge_uri(self, tenant_id, bridge_uuid):
        response, bridges =  self.list(tenant_id)
        return self._find_resource(bridges, bridge_uuid)

    def create(self, tenant_id, name, inbound_filter_id=None,
               outbound_filter_id=None):

        uri =  self.uri
        data = {"name": name,
                "tenantId": tenant_id,
                "inboundFilterId": inbound_filter_id,
                "outboundFilterId": outbound_filter_id}
        return self.cl.post(uri, data)

    def list(self, tenant_id):
        return self.cl.get(self.uri + "?tenant_id=" + tenant_id)

    def update(self, tenant_id, bridge_uuid, data):
        bridge_uri = self._bridge_uri(tenant_id, bridge_uuid)
        return self.cl.put(bridge_uri, data)

    def get(self, tenant_id, bridge_uuid):
        bridge_uri = self._bridge_uri(tenant_id, bridge_uuid)
        return self.cl.get(bridge_uri)

    def delete(self, tenant_id, bridge_uuid):
        bridge_uri = self._bridge_uri(tenant_id, bridge_uuid)
        return self.cl.delete(bridge_uri)

    def peer_ports(self, tenant_id, router_uuid):
        response, bridge = self.get(tenant_id, router_uuid)
        uri =  bridge['peerPorts']
        return self.cl.get(uri)
