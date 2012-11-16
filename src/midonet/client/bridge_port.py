# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
import port_type

class BridgePort(ResourceBase):

    media_type = 'application/vnd.com.midokura.midolman.mgmt.Port+json'

    def __init__(self, http, uri, dto):
        super(BridgePort, self).__init__(http, uri, dto)

    def get_id(self):
        return self.dto['id']

    def get_type(self):
        return self.dto['type']

    def get_device_id(self):
        return self.dto['deviceId']

    def get_inbound_filter_id(self):
        return self.dto['inboundFilterId']

    def get_outbound_filter_id(self):
        return self.dto['outboundFilterId']

    def inbound_filter_id(self, id_) :
        self.dto['inboundFilterId'] = id_
        return self

    def outbound_filter_id(self, id_) :
        self.dto['outboundFilterId'] = id_
        return self

    def vif_id(self, id_) :
        self.dto['vifId'] = id_
        return self

    def link(self, peer_uuid):
        self.dto['peerId'] = peer_uuid
        headers = {'Content-Type': self.media_type}
        self.web_resource.post(self.dto['link'], self.dto, headers=headers)
        return self.web_resource.get(self.dto['uri'], headers=headers)

    def unlink(self):
        self.dto['peerId'] = None
        headers = {'Content-Type': self.media_type}
        self.web_resource.post(self.dto['link'], self.dto, headers=headers)
        return self.web_resource.get(self.dto['uri'], headers=headers)
