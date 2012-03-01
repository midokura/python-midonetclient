# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Tenant(ResourceBase):

    path = 'tenants'

    def create(self, id_=None):
        """ Create a tennant."""
        return super(Tenant, self).create({"id": id_})

    # list() and get() are implemented in the super class
