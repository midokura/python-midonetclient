# Copyright 2012 Midokura Japan KK

from resource_base import ResourceBase
import vendor_media_type

class Rule(ResourceBase):

    media_type = vendor_media_type.APPLICATION_RULE_JSON

    def __init__(self, http, uri, dto):
        super(Rule, self).__init__(http, uri, dto)

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

    def get_chain_id(self):
        return self.dto['chainId']

    def get_dl_dst(self):
        return self.dto['dlDst']

    def get_dl_src(self):
        return self.dto['dlSrc']

    def get_dl_type(self):
        return self.dto['dlType']

    def get_flow_action(self):
        return self.dto['flowAction']

    def get_id(self):
        return self.dto['id']

    def get_in_ports(self):
        return self.dto['inPorts']

    def get_jump_chain_name(self):
        return self.dto['jumpChainName']

    def get_nat_targets(self):
        return self.dto['natTargets']

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

    def get_position(self):
        return self.dto['position']

    def get_tp_src_start(self):
        return self.dto['tpSrcStart']

    def get_tp_dst_start(self):
        return self.dto['tpDstStart']

    def get_properties(self):
        return self.dto['properties']

    def get_tp_src_end(self):
        return self.dto['tpSrcEnd']

    def get_tp_dst_end(self):
        return self.dto['tpDstEnd']

    def get_type(self):
        return self.dto['type']

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

    def position(self, position):
        self.dto['position'] = position
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

    def jump_chain_name(self, jump_chain_name):
        self.dto['jumpChainName'] = jump_chain_name
        return self

    def inv_dl_type(self, inv_dl_type):
        self.dto['invDlType'] = inv_dl_type
        return self

    def inv_tp_dst(self, inv_tp_dst):
        self.dto['invTpDst'] = inv_tp_dst
        return self

    def chain_id(self, chain_id):
        self.dto['chainId'] = chain_id
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

    def properties(self, properties):
        self.dto['properties'] = properties
        return self

    def cond_invert(self, cond_invert):
        self.dto['condInvert'] = cond_invert
        return self

    def tp_dst_end(self, tp_dst_end):
        self.dto['tpDstEnd'] = tp_dst_end
        return self

    def type(self, type):
        self.dto['type'] = type
        return self

    def inv_dl_src(self, inv_dl_src):
        self.dto['invDlSrc'] = inv_dl_src
        return self

    def tp_dst_start(self, tp_dst_start):
        self.dto['tpDstStart'] = tp_dst_start
        return self

    def flow_action(self, flow_action):
        self.dto['flowAction'] = flow_action
        return self

    def nat_targets(self, nat_targets):
        self.dto['natTargets'] = nat_targets
        return self

