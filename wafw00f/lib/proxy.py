import socket

try:
    import httplib
except ImportError:
    import http.client as httplib

try:
    import socks
except ImportError:
    socks = None


class NullProxy:

    def prepare(self, target, port, path, ssl):
        conn_factory = httplib.HTTPSConnection if ssl else httplib.HTTPConnection
        return conn_factory, target, port, path
    
    def terminate(self):
        pass


class HttpProxy:

    def __init__(self, host, port):
        self.host = host
        self.port = port        

    def prepare(self, target, port, path, ssl):
        if ssl:
            conn_factory = httplib.HTTPConnection
            query_path = path            
        else:        
            conn_factory = httplib.HTTPConnection
            query_path = "%(scheme)s://%(host)s%(path)s" % dict(
                    scheme="http",
                    host=target,
                    path=path)
        return conn_factory, self.host, self.port, query_path
    
    def terminate(self):
        pass


class Socks5Proxy:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.original = socket.socket
        self.original_create = socket.create_connection

    def prepare(self, target, port, path, ssl):
        def proxy_create_connection(address, timeout=4, source_address=None):
            return socks.create_connection(address, proxy_type=socks.PROXY_TYPE_SOCKS5, proxy_addr=self.host, proxy_port=self.port, source_address=source_address, timeout=timeout)

        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, self.host, self.port)
        httplib.socket.socket = socks.socksocket
        httplib.socket.create_connection = proxy_create_connection

        conn_factory = httplib.HTTPSConnection if ssl else httplib.HTTPConnection
        return conn_factory, target, port, path
    
    def terminate(self):
        httplib.socket.socket = self.original
        httplib.socket.create_connection = self.original_create
