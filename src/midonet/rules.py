# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Rule(ResourceBase):

    def _rules_uri(self, tenant_id, chain_uuid):
        response, chain = self.cl.chains().get(tenant_id, chain_uuid)
        return chain['rules']

    def _rule_uri(self, tenant_id, chain_uuid, rule_uuid):
        rules_uri = self._rules_uri(tenant_id, chain_uuid)
        response, rules = self.cl.get(rules_uri)
        return self._find_resource(rules, rule_uuid)


    def create(self, tenant_id,
                    chain_uuid,
                    cont_invert,
                    in_ports,
                    inv_in_ports,
                    out_ports,
                    inv_out_ports,
                    nw_tos,
                    inv_nw_tos,
                    nw_proto,
                    inv_nw_proto,
                    nw_src_address,
                    nw_src_length,
                    inv_nw_src,
                    nw_dst_address,
                    nw_dst_length,
                    inv_nw_dst,
                    tp_src_start,
                    tp_src_end,
                    inv_tp_src,
                    tp_dst_start,
                    tp_dst_end,
                    inv_tp_dst,
                    type_,
                    jump_chain_id,
                    jump_chain_name,
                    flow_action,
                    nat_targets,
                    position ):


        uri = self._rules_uri(tenant_id, chain_uuid)

        data = {
            "condInvert": cont_invert,
            "inPorts": in_ports,
            "invInPorts": inv_in_ports,
            "outPorts": out_ports,
            "invOutPorts":inv_out_ports,
            "nwTos": nw_tos,
            "invNwTos": inv_nw_tos,
            "nwProto": nw_proto,
            "invNwProto": inv_nw_proto,
            "nwSrcAddress": nw_src_address,
            "nwSrcLength": nw_src_length,
            "invNwSrc":inv_nw_src,
            "nwDstAddress": nw_dst_address,
            "nwDstLength": nw_dst_length,
            "invNwDst": inv_nw_dst,
            "tpSrcStart": tp_src_start,
            "tpSrcEnd": tp_src_end,
            "invTpSrc": inv_tp_src,
            "tpDstStart": tp_dst_start,
            "tpDstEnd": tp_dst_end,
            "invTpDst": inv_tp_dst,
            "type": type_,
            "jumpChainId": jump_chain_id,
            "jumpChainName": jump_chain_name,
            "flowAction": flow_action,
            "natTargets": nat_targets,
            "position": position
            }

        return self.cl.post(uri, data)

    def list(self, tenant_id, chain_uuid):
        rules_uri = self._rules_uri(tenant_id, chain_uuid)
        return self.cl.get(rules_uri)

    def get(self, tenant_id, chain_uuid, rule_uuid):
        rule_uri = self._rule_uri(tenant_id, chain_uuid, rule_uuid)
        return self.cl.get(rule_uri)

    def delete(self, tenant_id, chain_uuid, rule_uuid):
        rule_uri = self._rule_uri(tenant_id, chain_uuid, rule_uuid)
        return self.cl.delete(rule_uri)



    # utility methods.
    # NOTE: would be better to move them, e.g. to utility module
    def create_dnat_rule(self, tenant_id, chain_uuid,
                         nw_dst_address,   #floating
                         new_dst_address): #fixed

        return self.create(tenant_id, chain_uuid, False, None, False, None,
                        False, 0, False, None, False,
                        None, 0, False, nw_dst_address, 32, False, 0, 0,
                        False, 0, 0, False, 'dnat', None, None, 'accept',
                        [[[new_dst_address, new_dst_address], [0,0]]], 1)

    def create_snat_rule(self, tenant_id, chain_uuid,
                         new_nw_src_address, #floating
                         nw_src_address):    #fixed

        return self.create(tenant_id, chain_uuid, False, None, False, None,
                        False, 0, False, None, False,
                        nw_src_address, 32, False, None, 0, False, 0, 0,
                        False, 0, 0, False, 'snat', None, None, 'accept',
                        [[[new_nw_src_address, new_nw_src_address], [0,0]]], 1)

