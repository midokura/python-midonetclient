# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2014 Midokura Europe SARL, All Rights Reserved.
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
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura

from midonetclient.neutron import media_type
from midonetclient import vendor_media_type


class UrlProviderMixin(object):
    """Base URL provider mixin

    In MidoNet API, a response contains URIs that are used to discover the
    available endpoints. This mixin contains methods to provide URLs.
    """

    def __init__(self):
        self.app = None
        self.neutron = None

    def _application_url(self):
        if self.app is None:
            self.app = self.client.get(self.base_uri,
                                       vendor_media_type.APPLICATION_JSON_V5)
        return self.app

    def _neutron_url(self):
        if self.neutron is None:
            app = self._application_url()
            self.neutron = self.client.get(app["neutron"], media_type.NEUTRON)
        return self.neutron

    def resource_url(self, name):
        return self._neutron_url()[name]

    def load_balancer_resource_url(self, name):
        return self.resource_url("load_balancer")[name]

    def template_url(self, name, id):
        return self._neutron_url()[name].replace("{id}", id)

    def load_balancer_template_url(self, name, id):
        return load_balancer_resource_url(name).replace("{id}", id)


class NetworkUrlProviderMixin(UrlProviderMixin):
    """Network URL provider mixin

    This mixin provides URLs for networks.
    """

    def network_url(self, id):
        return self.template_url("network_template", id)

    def networks_url(self):
        return self.resource_url("networks")

    def subnet_url(self, id):
        return self.template_url("subnet_template", id)

    def subnets_url(self):
        return self.resource_url("subnets")

    def port_url(self, id):
        return self.template_url("port_template", id)

    def ports_url(self):
        return self.resource_url("ports")


class L3UrlProviderMixin(UrlProviderMixin):
    """L3 URL provider mixin

    This mixin provides URLs for L3 constructs.
    """

    def router_url(self, id):
        return self.template_url("router_template", id)

    def routers_url(self):
        return self.resource_url("routers")

    def add_router_interface_url(self, router_id):
        return self.template_url("add_router_interface_template", router_id)

    def remove_router_interface_url(self, router_id):
        return self.template_url("remove_router_interface_template", router_id)

    def floating_ip_url(self, id):
        return self.template_url("floating_ip_template", id)

    def floating_ips_url(self):
        return self.resource_url("floating_ips")


class SecurityGroupUrlProviderMixin(UrlProviderMixin):
    """SG URL provider mixin

    This mixin provides URLs for SG and SG rules.
    """

    def security_group_url(self, id):
        return self.template_url("security_group_template", id)

    def security_groups_url(self):
        return self.resource_url("security_groups")

    def security_group_rule_url(self, id):
        return self.template_url("security_group_rule_template", id)

    def security_group_rules_url(self):
        return self.resource_url("security_group_rules")


class LoadBalancerUrlProviderMixin(UrlProviderMixin):
    """Load Balancer URL provider mixin

    This mixin provides URLs for Load Balancer resources
    """

    def vips_url(self):
        return self.load_balancer_resource_url("vips")

    def vip_url(self, id):
        return self.load_balancer_template_url("vip_template", id)

    def pools_url(self):
        return self.load_balancer_resource_url("pools")

    def pool_url(self, id):
        return self.load_balancer_template_url("pool_template", id)

    def members_url(self):
        return self.load_balancer_resource_url("members")

    def member_url(self, id):
        return self.load_balancer_template_url("member_template", id)

    def health_monitors_url(self):
        return self.load_balancer_resource_url("health_monitors")

    def health_monitor_url(self, id):
        return self.load_balancer_template_url("health_monitor_template", id)

    def pool_health_monitor_url(self, id):
        return self.load_balancer_resource_url("pool_health_monitor", id)
