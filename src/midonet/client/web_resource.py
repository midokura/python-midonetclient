import exc
import httplib2
import json
import logging
import urllib

from eventlet.semaphore import Semaphore

LOG = None


class WebResource(object):

    def __init__(self, auth=None, logger=None):
        global LOG

        self.h = httplib2.Http()
        self.auth = auth
        self.sem = Semaphore()
        if logger == None:
            logging.basicConfig()
            #LOG = logging.getLogger('midonet.http_resource')
            LOG = logging.getLogger('nova...midonet.client')
            LOG.setLevel(logging.DEBUG)
        else:
            LOG = logger

    def _do_request(self, uri, method, body='{}', headers={}, retries_left=1):
        if not method == 'DELETE':
            if not('Content-Type' in headers and \
                        headers['Content-Type']):
                headers['Content-Type'] = 'application/json'

        if self.auth:
            headers.update(self.auth.generate_auth_header())

        with self.sem:
            response, content = self.h.request(uri, method, body,
                                               headers=headers)

        boarder = '=' * 20
        req = '(%s on %s) ' % (method, uri)
        LOG.debug(boarder)
        LOG.debug('Req: %s',  req)
        LOG.debug('Req headers: %s', headers)
        LOG.debug('Req Body: %s' % body)
        LOG.debug('Resp: %s' % response)
        LOG.debug('Resp Body: %s' % content)
        LOG.debug(boarder)

        if int(response['status']) > 300:
            # In case of authentication error, try re-generating auth header
            if self.auth and response['status'] == '401' and retries_left > 0:
                self.auth.get_token(regenerate=True)
                retries_left -= 1
                self._do_request(uri, method, body, headers, retries_left)

            LOG.error("%s got an error status %s", req, response['status'])
            e = exc.get_exception(response['status'])(content)
            LOG.error("Raising an exeption: (%r): %r" % (e, str(e)))
            raise e
        try:
            body = json.loads(content) if content else None
            return response, body
        except ValueError:
            return response, content

    def get(self, uri, headers={}, query={}):
        if query != {}:
            uri += '?' + urllib.urlencode(query)

        return self._do_request(uri, 'GET', headers=headers)

    def put(self, uri, body, headers={}):
        return self._do_request(uri, 'PUT', json.dumps(body), headers=headers)

    def post(self, uri, body, headers={}):
        return self._do_request(uri, 'POST', json.dumps(body), headers=headers)

    def delete(self, uri, headers={}):
        return self._do_request(uri, 'DELETE', headers=headers)
