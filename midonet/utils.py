# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2011 Midokura KK
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Internal Utility Functions
"""

import re
import openstack.compute
from django.conf import settings

DEBUG = True


def get_nova_connection(request):
    """ Gets an openstack.compute API Client connection that can make HTTP
        calls directly through it's get, post put & delete methods.
        like: resp, body = client.put(url, body=body)
    """
    management_url = "%s/%s" % (settings.OPENSTACK_1_1_URL,
                                request.user.tenant_id)
    override = {
        'auth_token' : request.user.token,
        'management_url' : management_url}

    cf = openstack.compute.Config(None, None, overrides=override)

    client = openstack.compute.ComputeClient(cf)
    client.auth_token = request.user.token
    client.management_url = management_url
    #client.authenticate()
    return client


def instance_to_ec2(openstack_id):
    """ converts from an openstack API int instance id to an EC2 API string id
    """
    return "i-%08x" % int(openstack_id)


def instance_to_open(ec2_id):
    """ converts from an EC2 API string instance id to an openstack API int id
    """
    m = re.search('i-0*(.+)', ec2_id)
    return m.group(1)


def debug_print(msg, resp, body):
    if DEBUG:
        print msg + ":\n" + '-' * 10
        print "Resp: %s" % resp + "\n" + '-' * 10
        print "Body: %s" % body + "\n" + '-' * 10

def dummy_image_id():
    try:
        return int(settings.DUMMY_IMAGE_ID)
    except AttributeError:
        return 1

def list_items_per_page():
    try:
        return settings.LIST_ITEMS_PER_PG
    except AttributeError:
        return 100

class testUser:
    def __init__(self, token, tenant_id):
        self.token = token
        self.tenant_id = tenant_id


class testRequest:
    def __init__(self, token, tenant):
        self.user = testUser(token, tenant)
