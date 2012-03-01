from webob import exc

code_exception_map = dict ((str(e.code), e) for e in
                           exc.HTTPClientError.__subclasses__() +
                           exc.HTTPServerError.__subclasses__())

def get_exception(status_code):
    return code_exception_map[status_code]
    
