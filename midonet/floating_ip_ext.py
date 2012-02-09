# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2011 Midokura KK
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from utils import get_nova_connection, debug_print
from novaclient.v1_1 import client as nova_client
from django_openstack.api import url_for, novaclient


class fip:
    def __init__(self):
        self.ip = ''

# associate a floating ip address to a vm
def server_add_floating_ip(request, server_id, address):
    fip = novaclient(request).floating_ips.get(address)
    cl = get_nova_connection(request)
    resp, body = cl.post("/servers/%i/action" % int(server_id),
                          body={"addFloatingIp": {"address": fip.ip}})
    debug_print("Add Floating IP", resp, body)
    return body

# disassociate the floating ip from the server
def server_remove_floating_ip(request, server_id, address):
    fip = novaclient(request).floating_ips.get(address)
    cl = get_nova_connection(request)
    resp, body = cl.post("/servers/%i/action" % int(server_id),
                          body={"removeFloatingIp": {"address": fip.ip}})
    debug_print("Remove Floating IP", resp, body)
    return body


def tenant_floating_ip_list(request):
    cl = get_nova_connection(request)
    resp, body = cl.get('/os-floating-ips')
    debug_print("List Floating IP's", resp, body)
    return body["floating_ips"]


def tenant_floating_ip_get(request, floating_ip_id):
    """
    Fetches a floating ip.
    """
    return novaclient(request).floating_ips.get(floating_ip_id)


def floating_ip_block_allocate(request, cidr):
    cl = get_nova_connection(request)
    resp, body = cl.post("/mido-floating-ips",  body={"cidr": cidr})
    debug_print("Allocate Floating IP", resp, body)
    return body


def floating_ip_block_list(request):
    cl = get_nova_connection(request)
    resp, body = cl.get("/mido-floating-ips")
    debug_print("List Floating IP", resp, body)
    return body["floating_ips"]


def floating_ip_block_delete(request, cidr):
    """
    Releases floating ip from the pool of a tenant.
    """
    cl = get_nova_connection(request)
    resp, body = cl.post("/mido-floating-ips/delete_cidr",  body={"cidr": cidr})
    debug_print("Release Floating IP", resp, body)
    return body
