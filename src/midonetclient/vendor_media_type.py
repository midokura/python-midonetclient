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


APPLICATION_JSON = "application/vnd.org.midonet.Application-v1+json"
APPLICATION_ERROR_JSON = "application/vnd.org.midonet.Error-v1+json"
APPLICATION_TENANT_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Tenant-v1+json"
APPLICATION_ROUTER_JSON = "application/vnd.org.midonet.Router-v1+json"
APPLICATION_ROUTER_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Router-v1+json"
APPLICATION_BRIDGE_JSON = "application/vnd.org.midonet.Bridge-v1+json"
APPLICATION_BRIDGE_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Bridge-v1+json"
APPLICATION_HOST_JSON = "application/vnd.org.midonet.Host-v1+json"
APPLICATION_HOST_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Host-v1+json"
APPLICATION_INTERFACE_JSON = "application/vnd.org.midonet.Interface-v1+json"
APPLICATION_INTERFACE_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Interface-v1+json"
APPLICATION_HOST_COMMAND_JSON = \
    "application/vnd.org.midonet.HostCommand-v1+json"
APPLICATION_HOST_COMMAND_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.HostCommand-v1+json"
APPLICATION_PORT_JSON = "application/vnd.org.midonet.Port-v1+json"
APPLICATION_PORT_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Port-v1+json"
APPLICATION_PORT_LINK_JSON = "application/vnd.org.midonet.PortLink-v1+json"
APPLICATION_ROUTE_JSON = "application/vnd.org.midonet.Route-v1+json"
APPLICATION_ROUTE_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Route-v1+json"
APPLICATION_PORTGROUP_JSON = "application/vnd.org.midonet.PortGroup-v1+json"
APPLICATION_PORTGROUP_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.PortGroup-v1+json"
APPLICATION_PORTGROUP_PORT_JSON = \
    "application/vnd.org.midonet.PortGroupPort-v1+json"
APPLICATION_PORTGROUP_PORT_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.PortGroupPort-v1+json"
APPLICATION_CHAIN_JSON = "application/vnd.org.midonet.Chain-v1+json"
APPLICATION_CHAIN_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Chain-v1+json"
APPLICATION_RULE_JSON = "application/vnd.org.midonet.Rule-v1+json"
APPLICATION_RULE_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Rule-v1+json"
APPLICATION_BGP_JSON = "application/vnd.org.midonet.Bgp-v1+json"
APPLICATION_BGP_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Bgp-v1+json"
APPLICATION_AD_ROUTE_JSON = "application/vnd.org.midonet.AdRoute-v1+json"
APPLICATION_AD_ROUTE_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.AdRoute-v1+json"
APPLICATION_VPN_JSON = "application/vnd.org.midonet.Vpn-v1+json"
APPLICATION_VPN_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Vpn-v1+json"
APPLICATION_DHCP_SUBNET_JSON = "application/vnd.org.midonet.DhcpSubnet-v1+json"
APPLICATION_DHCP_SUBNET_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.DhcpSubnet-v1+json"
APPLICATION_DHCP_HOST_JSON = "application/vnd.org.midonet.DhcpHost-v1+json"
APPLICATION_DHCP_HOST_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.DhcpHost-v1+json"
APPLICATION_MONITORING_QUERY_RESPONSE_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.mgmt.MetricQueryResponse-v1+json"
APPLICATION_MONITORING_QUERY_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.MetricQuery-v1+json"
APPLICATION_METRICS_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Metric-v1+json"
APPLICATION_METRIC_TARGET_JSON = \
    "application/vnd.org.midonet.MetricTarget-v1+json"
APPLICATION_TUNNEL_ZONE_JSON = "application/vnd.org.midonet.TunnelZone-v1+json"
APPLICATION_TUNNEL_ZONE_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.TunnelZone-v1+json"
APPLICATION_TUNNEL_ZONE_HOST_JSON = \
    "application/vnd.org.midonet.TunnelZoneHost-v1+json"
APPLICATION_TUNNEL_ZONE_HOST_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.TunnelZoneHost-v1+json"
APPLICATION_CAPWAP_TUNNEL_ZONE_HOST_JSON = \
    "application/vnd.org.midonet.CapwapTunnelZoneHost-v1+json"
APPLICATION_CAPWAP_TUNNEL_ZONE_HOST_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.CapwapTunnelZoneHost-v1+json"
APPLICATION_GRE_TUNNEL_ZONE_HOST_JSON = \
    "application/vnd.org.midonet.GreTunnelZoneHost-v1+json"
APPLICATION_GRE_TUNNEL_ZONE_HOST_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.GreTunnelZoneHost-v1+json"
APPLICATION_IPSEC_TUNNEL_ZONE_HOST_JSON = \
    "application/vnd.org.midonet.IpsecTunnelZoneHost-v1+json"
APPLICATION_IPSEC_TUNNEL_ZONE_HOST_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.IpsecTunnelZoneHost-v1+json"
APPLICATION_HOST_INTERFACE_PORT_JSON = \
    "application/vnd.org.midonet.HostInterfacePort-v1+json"
APPLICATION_HOST_INTERFACE_PORT_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.HostInterfacePort-v1+json"
APPLICATION_CONDITION_JSON = "application/vnd.org.midonet.Condition-v1+json"
APPLICATION_CONDITION_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Condition-v1+json"
APPLICATION_TRACE_JSON = "application/vnd.org.midonet.Trace-v1+json"
APPLICATION_TRACE_COLLECTION_JSON = \
    "application/vnd.org.midonet.collection.Trace-v1+json"
