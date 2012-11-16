# Copyright 2011 Midokura Japan KK

import exceptions
import urllib

class ResourceBase(object):

    media_type = None
    resource_cache = {}

    def __init__(self, web, uri, dto):
        self.web_resource = web
        self.uri = uri
        self.dto = dto

    def create(self, headers={}):
        if self.media_type:
            headers['Content-Type'] = self.media_type
        resp, data = self.web_resource.post(self.uri, self.dto, headers)

        if self.media_type:
            headers['Accept'] = self.media_type
        res, self.dto = self.web_resource.get(resp['location'], headers=headers)
        if self.dto.get('id'):
            self.resource_cache[self.dto['id']] = self.dto['uri']
        return self

    def get(self, headers={}, **kwargs):
        if self.media_type:
            headers['Content-Type'] = self.media_type
            headers['Accept'] = self.media_type

        uri = self.dto['uri']
        res, self.dto =  self.web_resource.get(uri, headers=headers)
        return self

    def get_children(self, uri, query, headers, clazz, extra_args=None):
        resources = []
        res, dtos =  self.web_resource.get(uri, query=query, headers=headers)
        for dto in dtos:
            if dto.get('id'):
                self.resource_cache[dto['id']] = dto['uri']
            if extra_args is None:
                resources.append(clazz(self.web_resource, uri, dto))
            else:
                resources.append(clazz(self.web_resource, uri, dto, *extra_args))
        return resources

    def update(self, headers={}):
        if self.media_type:
            headers['Content-Type'] = self.media_type
        resp, body = self.web_resource.put(self.dto['uri'], self.dto, headers=headers)
        if self.media_type:
            headers['Accept'] = self.media_type
        resp, self.dto = self.web_resource.get(self.dto['uri'], headers=headers)
        return self

    def delete(self, headers={}):
        resp, junk =  self.web_resource.delete(self.dto['uri'], headers=headers)
        if self.dto.get('id'):
            del self.resource_cache[self.dto['id']]
        return None

    def _get_resource(self, clazz, id_, request_uri, filter_, collection_getter):
        if self.resource_cache.get(id_):
            return clazz(self.web_resource, request_uri,
                         {'uri': self.resource_cache.get(id_)}).get()
        else:
            found = False
            for resource in collection_getter(filter_):
                if resource.get_id() == id_:
                    found = True
                    return resource
            if not found:
                raise LookupError('Resource=%r, id=%r, not found')

    def __repr__(self):
        return self.__class__.__name__ + str(self.dto)

