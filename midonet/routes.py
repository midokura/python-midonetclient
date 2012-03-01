# Copyright 2012 Midokura Japan KK

from resource import ResourceBase

class Route(ResourceBase):

    def create(self, router_uuid, type, srcNetworkAddr, srcNetworkLength,
                        dstNetworkAddr, dstNetworkLength, weight,
                        nextHopPort=None, nextHopGateway=None ):

        path =  'routers/%s/routes' % router_uuid
        body ={ "type": type,
                "srcNetworkAddr": srcNetworkAddr,
                "srcNetworkLength": srcNetworkLength, #int
                "dstNetworkAddr": dstNetworkAddr,
                "dstNetworkLength": dstNetworkLength, #int
                "weight": weight } #int

        if type == 'Normal':
            body["nextHopPort"] = nextHopPort
        if nextHopGateway:
            body["nextHopGateway"] = nextHopGateway

        return self.cl.post(path, body)


    def list(self, router_uuid):
        path = 'routers/%s/routes' % router_uuid
        return self.cl.get(path)


def list_routes(request, router_id):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/%s/routes' % router_id
    resp, body = cl.get(url)
    debug_print("List Router Routes", resp, body)
    return body


def route_display_listing(route_list):
    for r in route_list:
        r['real_id'] = r['id']
        r['id']      = r['id'].replace("-", "-\n") if r['id'] else '--'
    return route_list


def get_route(request, route_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routes/' + route_uuid
    resp, body = cl.get(url)
    debug_print("Get Route", resp, body)
    return body


def delete_route(request, route_uuid):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routes/' + route_uuid
    resp, body = cl.delete(url)
    debug_print("Delete Route", resp, body)
    return body


def delete_all_router_routes(request, router_id):
    """ Deletes all the routes associated with the specified router
    """
    for route in list_routes(request, router_id):
        delete_route(request, route['id'])


#Create a new route on a router that sets the next hop port to a  port.
#'{"srcNetworkAddr": "10.0.0.0", "srcNetworkLength": 24, "type": "Normal", "dstNetworkAddr": "192.168.0.0", "dstNetworkLength": 24, "nextHopPort": "fee55096-5669-452e-bd7c-4a79229fe85f", "nextHopGateway": "192.168.0.1", "weight": 100}'
# localhost:8080/midolmanj-mgmt/v1/routers/6dffe7dd-2d5b-46d4-ae73-cc78bbb16997/routes
#
#Create a new black hole route.
#'{"srcNetworkAddr": "10.0.0.0", "srcNetworkLength": 24, "type": "BlackHole", "dstNetworkAddr": "192.168.0.0", "dstNetworkLength": 24, "weight": 100}'
#
#Create a new reject route.
#'{"srcNetworkAddr": "10.0.0.0", "srcNetworkLength": 24, "type": "Reject", "dstNetworkAddr": "192.168.0.0", "dstNetworkLength": 24, "weight": 100}'
#
def create_route(request, router_id, type, srcNetworkAddr, srcNetworkLength,
                        dstNetworkAddr, dstNetworkLength, weight,
                        nextHopPort=None, nextHopGateway=None ):
    cl = MidonetClient(request)
    url = settings.MIDONET_URL + 'routers/%s/routes' % router_id
    body ={ "type": type,
            "srcNetworkAddr": srcNetworkAddr,
            "srcNetworkLength": srcNetworkLength, #int
            "dstNetworkAddr": dstNetworkAddr,
            "dstNetworkLength": dstNetworkLength, #int
            "weight": weight } #int

    if type == 'Normal':
        body["nextHopPort"] = nextHopPort
        if nextHopGateway:
            body["nextHopGateway"] = nextHopGateway

    resp, body = cl.post(url, body)
    debug_print("Create Router Route", resp, body)
    return body
