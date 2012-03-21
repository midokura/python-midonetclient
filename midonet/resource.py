# Copyright 2011 Midokura Japan KK

import exceptions

class ResourceBase(object):

    def _find_resource(self, content, id_):
        for c in content:
            if c['id'] == id_:
                return c['uri']
        raise exceptions.LookupError('resource not found', id_)

    def accept(self, client, uri):
        self.cl = client
        self.uri = uri
        return self

    def create(self, data):
        return self.cl.post(self.uri, data)

    def list(self):
        return self.cl.get(self.uri)

    def get(self, id_):
       uri = self.uri + '/' + id_
       return self.cl.get(uri)

    def delete(self, id_):
        uri = self.uri + '/' + id_
        return self.cl.delete(uri)

