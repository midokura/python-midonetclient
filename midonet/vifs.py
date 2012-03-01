# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Vif(ResourceBase):

    path = 'vifs'

    def create(self, vif_uuid, port_uuid):
        data = {"portId": port_uuid, "id": vif_uuid }

        return super(Vif, self).create(data)
