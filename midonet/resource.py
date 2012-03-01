# Copyright 2011 Midokura Japan KK

class ResourceBase(object):

    def accept(self, client):
        self.cl = client
        return self

    def create(self, data):
        return self.cl.post(self.path, data)

    def list(self):
        return self.cl.get(self.path)

    def get(self, id_):
       path = self.path + '/' + id_
       return self.cl.get(path)

    def delete(self, id_):
        path = self.path + '/' + id_
        return self.cl.delete(path)
