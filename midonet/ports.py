# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2011 Midokura KK
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf import settings
import switches
from utils import debug_print
from client import MidonetClient


def list_router_ports(request, router_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/%s/ports' % router_uuid
    resp, body = cl.get(url)
    debug_print("List Router Ports", resp, body)
    return body


def get_port(request, port_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'ports/' + port_uuid
    resp, body = cl.get(url)
    debug_print("Get Port (%s)" % port_uuid, resp, body)
    return body


# delete router port same as delete switch port?
def delete_port(request, port_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'ports/%s' % port_uuid
    resp, body = cl.delete(url)
    debug_print("Delete Port", resp, body)
    return body


def delete_all_router_ports(request, router_uuid):
    for port in list_router_ports(request, router_uuid):
        delete_port(request, port['id'])


# Create a new port on a router that will be used to connect directly
# to a VM ('Materialized' port) or other non-MidoNet endpoints.
def create_port(request, source_router_id,
                             networkAddress, networkLength, portAddress,
                             localNetworkAddress, localNetworkLength):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/%s/ports' % source_router_id
    body = { "networkAddress": networkAddress,
            "networkLength": networkLength, #int
            "portAddress": portAddress,
            "localNetworkAddress": localNetworkAddress,
            "localNetworkLength": localNetworkLength } #int
    resp, body = cl.post(url, body)
    debug_print("Create Materialized", resp, body)
    return body


#Create a new port on a router that will be used to connect to another MidoNet virtual router('Logical' port).
#with an optional peer logical port ID specified to create a link to it.
# create_logical_port replaced by new link routers api

# ---------------- SWITCH PORTS ---------------

def create_switch_port(request, bridge_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'bridges/%s/ports' % bridge_uuid
    resp, body = cl.post(url, {})
    debug_print("Create Switch Port", resp, body)
    return body


def delete_switch_port(request, port_id):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'ports/%s' % port_id
    resp, body = cl.delete(url)
    return body


def list_switch_ports(request, bridge_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'bridges/%s/ports' % bridge_uuid
    resp, body = cl.get(url)
    debug_print("List Switch Ports", resp, body)
    return body
