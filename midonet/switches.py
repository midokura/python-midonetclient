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


def list_all_switches():
    """  Gets all the bridges in the system. """
    return None

def list_switches(request):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'tenants/%s/bridges' % request.user.tenant_id
    resp, body = cl.get(url)
    debug_print("List Switches", resp, body)
    return body


def create_switch(request, switch_name):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'tenants/%s/bridges' % request.user.tenant_id
    resp, body = cl.post(url, {"name": switch_name })
    debug_print("Create Switch", resp, body)
    return body


def delete_switch(request, bridge_UUID):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'bridges/%s' % bridge_UUID
    resp, body = cl.delete(url)
    debug_print("Delete Switch", resp, body)
    return body


def get_switch(request, bridge_UUID):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'bridges/%s' % bridge_UUID
    resp, body = cl.get(url)
    debug_print("Get Switch", resp, body)
    return body
