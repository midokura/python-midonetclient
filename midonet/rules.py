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


# ----------- Chains -----------
def list_rule_chains(request, router_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/' + router_uuid + '/chains'
    resp, body = cl.get(url)
    debug_print("List Router Rule Chains", resp, body)
    return body


def get_rule_chain(request, chain_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'chains/' + chain_uuid
    resp, body = cl.get(url)
    debug_print("Get rule chain", resp, body)
    return body


def create_rule_chain(request, chain_name, router_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/' + router_uuid + '/chains'
    resp, body = cl.post(url, {"name": chain_name})
    debug_print("Create rule chain", resp, body)
    return body


def delete_rule_chain(request, chain_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'chains/' + chain_uuid
    resp, body = cl.delete(url)
    debug_print("Delete rule chain", resp, body)
    return body


# ----------- Rules -----------
def list_chain_rules(request, chain_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'chains/' + chain_uuid + '/rules'
    resp, body = cl.get(url)
    debug_print("List chain rules", resp, body)
    return body


def get_rule(request, rule_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'rules/' + rule_uuid
    resp, body = cl.get(url)
    debug_print("Get rule", resp, body)
    return body


def create_rule(request, chain_uuid, rule_type, position, jump_chain_id, flow_action,
                nat_targets, cond_invert, in_ports, inv_in_ports, out_ports,
                inv_out_ports, nw_tos, nw_proto, inv_nw_proto, nw_src_address,
                nw_src_length, inv_nw_src, nw_dst_address, nw_dst_length,
                inv_nw_dst, tp_src_start, tp_src_end, inv_tp_src, tp_dst_start,
                tp_dst_end, inv_tp_dst):
    
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'chains/' + chain_uuid + '/rules'
   
    data = { 'type' : rule_type,
             'position' : position,
             'condInvert' : cond_invert,
             'invNwProto' : inv_nw_proto,
             }

    #Getting conditional requirements
    if rule_type == 'jump':
        data['jumpChainId'] = jump_chain_id
        data["jumpChainName"] = 'jump_chain_name' #TODO
    elif rule_type == 'dnat' or rule_type == 'snat':
        data['flowAction'] = flow_action
        data['natTargets'] = nat_targets
    elif rule_type == 'rev_dnat' or rule_type == 'rev_snat':
        data['flowAction'] = flow_action

    if in_ports:
        data['inPorts'] = in_ports # Must be a list not a string
        data['invInPorts'] = inv_in_ports
        
    if out_ports:
        data['outPorts'] = out_ports # Must be a list not a string
        data['invOutPorts'] = inv_out_ports

    if nw_tos:
        data['nwTos'] = nw_tos
        data["invNwTos"] = False # inv_nw_tos #TODO
        
    if nw_proto:
        data['nwProto'] = nw_proto
        
    if nw_src_address:
        data['nwSrcAddress'] = nw_src_address
        data['nwSrcLength']= nw_src_length
        data['invNwSrc'] = inv_nw_src
        
    if nw_dst_address:
        data['nwDstAddress'] = nw_dst_address
        data['nwDstLength'] = nw_dst_length
        data['invNwDst'] = inv_nw_dst
        
    if tp_src_start:
        data['tpSrcStart'] = tp_src_start
        data['tpSrcEnd'] = tp_src_end
        data['invTpSrc'] = inv_tp_src
        
    if tp_dst_start:
        data['tpDstStart'] = tp_dst_start
        data['tpDstEnd'] = tp_dst_end
        data['invTpDst'] = inv_tp_dst

    resp, body = cl.post(url, data)
    debug_print("Create Rule", resp, body)
    return body


def delete_rule(request, rule_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'rules/' + rule_uuid
    resp, body = cl.delete(url)
    debug_print("Delete rule", resp, body)
    return body
