# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2011 Midokura KK
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf import settings
from utils import debug_print
from client import MidonetClient


def list_routers(request):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'tenants/%s/routers' % request.user.tenant_id
    resp, body = cl.get(url)
    debug_print("List Routers", resp, body)
    return body


def get_router(request, router_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/' + router_uuid
    resp, body = cl.get(url)
    debug_print("Get Router", resp, body)
    return body


def delete_router(request, router_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/' + router_uuid
    resp, body = cl.delete(url)
    debug_print("Delete Router", resp, body)
    return body


def create_router(request, name):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'tenants/%s/routers' % request.user.tenant_id
    resp, body = cl.post(url, {"name": name})
    debug_print("Create Tenant Router", resp, body)
    return body


def link_router(request, source_router_id,
                network_address, network_length,
                port_address, peer_port_address,  peer_router_id):

    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/%s/routers' % source_router_id
    body = {
        "networkAddress": network_address,
        "networkLength": network_length,
        "portAddress": port_address,
        "peerPortAddress": peer_port_address,
        "peerRouterId": peer_router_id
        }
    resp, body = cl.post(url, body)
    debug_print("Link Router", resp, body)
    return body

def list_links(request, router_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/%s/routers' % router_uuid
    resp, body = cl.get(url)
    debug_print("List Links", resp, body)
    return body

def remove_all_links(request, router_uuid):
    cl = MidonetClient(request)
    for link in list_links(request, router_uuid):
        url = settings.MIDONET_URL + 'routers/' + router_uuid + '/routers/' + link['peerRouterId']
        resp, body = cl.delete(url)
        debug_print("Delete Router Link", resp, body)
