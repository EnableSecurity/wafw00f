try:
    import httplib
except ImportError:
    import http.client as httplib


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
        conn_factory = httplib.HTTPConnection
        query_path = "%(scheme)s://%(host)s%(path)s" % dict(
                scheme="https" if ssl else "http",
                host=target,
                path=path)
        return conn_factory, self.host, self.port, query_path
    
    def terminate(self):
        pass


class Socks5Proxy:

    def __init__(self, host, port):
        import socket
        self.host = host
        self.port = port
        self.original = socket.socket

    def prepare(self, target, port, path, ssl):
        import socks
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, self.host, self.port)
        httplib.socket.socket = socks.socksocket

        conn_factory = httplib.HTTPSConnection if ssl else httplib.HTTPConnection
        return conn_factory, target, port, path
    
    def terminate(self):
        httplib.socket.socket = self.original
