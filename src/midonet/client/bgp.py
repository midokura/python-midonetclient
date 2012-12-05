# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
from ad_route import AdRoute
import vendor_media_type

class Bgp(ResourceBase):

    media_type = vendor_media_type.APPLICATION_BGP_JSON

    def __init__(self, http, uri, dto):
        super(Bgp, self).__init__(http, uri, dto)

    def get_id(self):
        return self.dto['id']

    def get_local_as(self):
        return self.dto['localAS']

    def get_peer_as(self):
        return self.dto['peerAS']

    def get_peer_addr(self):
        return self.dto['peerAddr']

    def local_as(self, local_as):
        self.dto['localAS'] = local_as
        return self

    def peer_as(self, peer_as):
        self.dto['peerAS'] = peer_as
        return self

    def peer_addr(self, addr):
        self.dto['peerAddr'] = addr
        return self

    def get_ad_routes(self):
        query = {}
        headers = {'Content-Type':
                   vendor_media_type.APPLICATION_AD_ROUTE_COLLECTION_JSON}
        return self.get_children(self.dto['adRoutes'], query, headers,
                                 AdRoute)
    def add_ad_route(self):
        return AdRoute(self.web_resource, self.dto['adRoutes'], {})
