# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Midokura PTE LTD.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# @author: Tomoe Sugihara <tomoe@midokura.com>, Midokura
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura
# @author: Artem Dmytrenko <art@midokura.com>, Midokura

from midonetclient import vendor_media_type
from midonetclient.resource_base import ResourceBase


class TraceCondition(ResourceBase):

    media_type = vendor_media_type.APPLICATION_CONDITION_JSON

    def __init__(self, uri, dto, auth):
        super(TraceCondition, self).__init__(uri, dto, auth)

    def is_cond_invert(self):
        return self.dto['condInvert']

    def is_inv_dl_dst(self):
        return self.dto['invDlDst']

    def is_inv_dl_src(self):
        return self.dto['invDlSrc']

    def is_inv_dl_type(self):
        return self.dto['invDlType']

    def is_inv_in_ports(self):
        return self.dto['invInPorts']

    def is_inv_nw_dst(self):
        return self.dto['invNwDst']

    def is_inv_nw_proto(self):
        return self.dto['invNwProto']

    def is_inv_nw_src(self):
        return self.dto['invNwSrc']

    def is_inv_nw_tos(self):
        return self.dto['invNwTos']

    def is_inv_out_ports(self):
        return self.dto['invOutPorts']

    def is_inv_port_group(self):
        return self.dto['invPortGroup']

    def is_inv_tp_dst(self):
        return self.dto['invTpDst']

    def is_inv_tp_src(self):
        return self.dto['invTpSrc']

    def is_match_forward_flow(self):
        return self.dto['matchForwardFlow']

    def is_match_return_flow(self):
        return self.dto['matchReturnFlow']

    def get_dl_dst(self):
        return self.dto['dlDst']

    def get_dl_src(self):
        return self.dto['dlSrc']

    def get_dl_type(self):
        return self.dto['dlType']

    def get_id(self):
        return self.dto['id']

    def get_in_ports(self):
        return self.dto['inPorts']

    def get_nw_dst_address(self):
        return self.dto['nwDstAddress']

    def get_nw_dst_length(self):
        return self.dto['nwDstLength']

    def get_nw_proto(self):
        return self.dto['nwProto']

    def get_nw_src_address(self):
        return self.dto['nwSrcAddress']

    def get_nw_src_length(self):
        return self.dto['nwSrcLength']

    def get_nw_tos(self):
        return self.dto['nwTos']

    def get_out_ports(self):
        return self.dto['outPorts']

    def get_port_group(self):
        return self.dto['portGroup']

    def get_tp_src_start(self):
        return self.dto['tpSrcStart']

    def get_tp_dst_start(self):
        return self.dto['tpDstStart']

    def get_tp_src_end(self):
        return self.dto['tpSrcEnd']

    def get_tp_dst_end(self):
        return self.dto['tpDstEnd']

    def inv_port_group(self, inv_port_group):
        self.dto['invPortGroup'] = inv_port_group
        return self

    def tp_src_start(self, tp_src_start):
        self.dto['tpSrcStart'] = tp_src_start
        return self

    def dl_src(self, dl_src):
        self.dto['dlSrc'] = dl_src
        return self

    def inv_nw_dst(self, inv_nw_dst):
        self.dto['invNwDst'] = inv_nw_dst
        return self

    def dl_dst(self, dl_dst):
        self.dto['dlDst'] = dl_dst
        return self

    def match_forward_flow(self, match_forward_flow):
        self.dto['matchForwardFlow'] = match_forward_flow
        return self

    def tp_src_end(self, tp_src_end):
        self.dto['tpSrcEnd'] = tp_src_end
        return self

    def inv_tp_src(self, inv_tp_src):
        self.dto['invTpSrc'] = inv_tp_src
        return self

    def match_return_flow(self, match_return_flow):
        self.dto['matchReturnFlow'] = match_return_flow
        return self

    def inv_nw_src(self, inv_nw_src):
        self.dto['invNwSrc'] = inv_nw_src
        return self

    def out_ports(self, out_ports):
        self.dto['outPorts'] = out_ports
        return self

    def nw_dst_length(self, nw_dst_length):
        self.dto['nwDstLength'] = nw_dst_length
        return self

    def inv_out_ports(self, inv_out_ports):
        self.dto['invOutPorts'] = inv_out_ports
        return self

    def dl_type(self, dl_type):
        self.dto['dlType'] = dl_type
        return self

    def inv_nw_tos(self, inv_nw_tos):
        self.dto['invNwTos'] = inv_nw_tos
        return self

    def port_group(self, port_group):
        self.dto['portGroup'] = port_group
        return self

    def inv_dl_dst(self, inv_dl_dst):
        self.dto['invDlDst'] = inv_dl_dst
        return self

    def inv_in_ports(self, inv_in_ports):
        self.dto['invInPorts'] = inv_in_ports
        return self

    def inv_dl_type(self, inv_dl_type):
        self.dto['invDlType'] = inv_dl_type
        return self

    def inv_tp_dst(self, inv_tp_dst):
        self.dto['invTpDst'] = inv_tp_dst
        return self

    def nw_tos(self, nw_tos):
        self.dto['nwTos'] = nw_tos
        return self

    def nw_proto(self, nw_proto):
        self.dto['nwProto'] = nw_proto
        return self

    def nw_src_length(self, nw_src_length):
        self.dto['nwSrcLength'] = nw_src_length
        return self

    def in_ports(self, in_ports):
        self.dto['inPorts'] = in_ports
        return self

    def nw_dst_address(self, nw_dst_address):
        self.dto['nwDstAddress'] = nw_dst_address
        return self

    def nw_src_address(self, nw_src_address):
        self.dto['nwSrcAddress'] = nw_src_address
        return self

    def inv_nw_proto(self, inv_nw_proto):
        self.dto['invNwProto'] = inv_nw_proto
        return self

    def cond_invert(self, cond_invert):
        self.dto['condInvert'] = cond_invert
        return self

    def tp_dst_end(self, tp_dst_end):
        self.dto['tpDstEnd'] = tp_dst_end
        return self

    def inv_dl_src(self, inv_dl_src):
        self.dto['invDlSrc'] = inv_dl_src
        return self

    def tp_dst_start(self, tp_dst_start):
        self.dto['tpDstStart'] = tp_dst_start
        return self
