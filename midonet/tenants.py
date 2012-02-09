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

def create_mido_tenant(request, tenant_uuid):
    """ After creating a tenant in keystone, this function needs to be called
        to initialize the tenant in midonet's Zookeeper DB """
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'tenants'
    resp, body = cl.post(url, {"id": tenant_uuid })
    debug_print("Create Mido Tenant", resp, body)
    return body