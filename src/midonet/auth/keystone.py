
from keystoneclient.v2_0 import client as keystone_client

from datetime import datetime
from datetime import timedelta

class KeystoneAuth:

    def __init__(self, uri, username, password, tenant_id=None,
                 tenant_name=None):
        self.uri = uri
        self.username = username
        self.password = password
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.token = None
        self.token_expires = None
        self.headers = {}

    def generate_auth_header(self):

        if (self.token_expires == None or
            self.token_expires - datetime.now() < timedelta(seconds=60*60)):
            try:
                self.token = self.get_token()
                self.token_expires = datetime.strptime(self.token.expires,
                        '%Y-%m-%dT%H:%M:%SZ')
            except Exception as e:
                print 'failed ', e

        self.headers["X-Auth-Token"] = self.token.id
        return self.headers

    def get_token(self):
        if (self.token_expires == None or
                self.token_expires - datetime.now() < timedelta(seconds=60*60)):
            ks_conn = keystone_client.Client(endpoint=self.uri)
            self.token = ks_conn.tokens.authenticate(
                    username=self.username, password=self.password,
                    tenant_id=self.tenant_id, tenant_name=self.tenant_name)
        return self.token

