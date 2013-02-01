
from keystoneclient.v2_0 import client as keystone_client

from datetime import datetime
from datetime import timedelta

import logging
LOG = logging.getLogger(__name__)
SAFETY_WINDOW_SECONDS = 60 * 60  # 1 hour


class KeystoneAuth:

    def __init__(self, uri, username, password, tenant_id=None,
                 tenant_name=None):
        self.uri = uri
        self.username = username
        self.password = password
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.token = None
        self.token_expires_at = None
        self.headers = {}

    def generate_auth_header(self, regenerate=False):
        if (self._needs_regeneration(regenerate)):
            try:
                LOG.info('generating token...')
                self.token = self.get_token(regenerate)
            except Exception as e:
                print 'failed ', e

        self.headers["X-Auth-Token"] = self.token.id
        return self.headers

    def get_token(self, regenerate=False):
        if (self._needs_regeneration(regenerate)):
            ks_conn = keystone_client.Client(endpoint=self.uri)
            self.token = ks_conn.tokens.authenticate(
                    username=self.username, password=self.password,
                    tenant_id=self.tenant_id, tenant_name=self.tenant_name)
            self.token_expires_at = datetime.strptime(self.token.expires,
                                                      '%Y-%m-%dT%H:%M:%SZ')
        return self.token

    def _needs_regeneration(self, regenerate):
        # yes, of course for the first time
        if self.token_expires_at == None:
            return True
        # sure, if you asked
        if regenerate:
            return True
        # check for expiration
        return self._token_expires()

    def _token_expires(self):
        return (self.token_expires_at - datetime.utcnow()) < \
            timedelta(seconds=SAFETY_WINDOW_SECONDS)
