#!/usr/bin/env python


from unittest import TestCase

import httpretty

from wafw00f.main import WafW00F


class WafW00FTestCase(TestCase):

    def test_is360wzb(self):
        """
        ::

           $ curl -I http://www.58dm.com/
           HTTP/1.1 200 OK
           Server: nginx/1.4.3.6
           Date: Tue, 10 Jun 2014 12:42:21 GMT
           Content-Type: text/html
           Connection: keep-alive
           X-Powered-By-360WZB: wangzhan.360.cn
           Content-Location: http://www.58dm.com/index.html
           Last-Modified: Tue, 10 Jun 2014 04:10:42 GMT
           ETag: "6a8d27f26184cf1:daa"
           VAR-Cache: HIT
           Accept-Ranges: bytes
           cache-control: max-age=7200
           age: 0
        """
        self.__assert_waf('www.58dm.com', '360WangZhanBao', {'X-Powered-By-360WZB': 'wangzhan.360.cn'})

    def test_isanquanbao(self):
        """
        ::

           $ curl -I http://www.51cdz.com/
           HTTP/1.1 200 OK
           Server: ASERVER/1.2.9-3
           Date: Tue, 10 Jun 2014 12:41:42 GMT
           Content-Type: text/html
           Content-Length: 76789
           Connection: keep-alive
           Content-Location: http://www.51cdz.com/index.html
           Last-Modified: Sun, 01 Jun 2014 15:39:34 GMT
           Accept-Ranges: bytes
           ETag: "766fe9afaf7dcf1:41fc"
           X-Powered-By-Anquanbao: MISS from chn-tj-ht-se2
        """
        self.__assert_waf('www.51cdz.com', 'Anquanbao', {'X-Powered-By-Anquanbao': 'MISS from chn-tj-ht-se2'})

    def test_ischinacache(self):
        """
        ::

           $ curl -I http://s1.meituan.net/
           HTTP/1.0 404 Not Found
           Server: Tengine
           Date: Tue, 10 Jun 2014 12:40:19 GMT
           Content-Type: text/html; charset=iso-8859-1
           Timing-Allow-Origin: *
           Powered-By-ChinaCache: MISS from 0100102396
           X-Cache: MISS from DXT-BJ-104
           X-Cache-Lookup: MISS from DXT-BJ-104:80
           X-Cache: MISS from DXT-BJ-219
           X-Cache-Lookup: MISS from DXT-BJ-219:80
           Connection: close
        """
        self.__assert_waf('s1.meituan.net', 'ChinaCache-CDN', {'Powered-By-ChinaCache': 'fake'})

    def test_ispowercdn(self):
        """
        ::

           $ curl -I http://www.jjwxc.net/
           HTTP/1.1 200 OK
           Date: Tue, 10 Jun 2014 01:17:09 GMT
           Content-Type: text/html
           Last-Modified: Mon, 09 Jun 2014 17:30:04 GMT
           Content-Encoding: gzip
           X-Cache: HIT from BGP-1-233-ZZ-JJCDN
           X-Cache-Lookup: HIT from BGP-1-233-ZZ-JJCDN:80
           Age: 6052
           PowerCDN: HIT from ak244.powercdn.com
           Via: 1.1 ak244.powercdn.com (PowerCDN/2.4)
           Connection: keep-alive
        """
        self.__assert_waf('www.jjwxc.net', 'PowerCDN', {'PowerCDN': 'HIT from ak244.powercdn.com'})

    def test_iswest263cdn(self):
        """
        ::

           $ curl -I http://hsht.hs3w.com/
           HTTP/1.0 400 Bad Request
           Content-Length: 39
           Content-Type: text/html
           Date: Tue, 10 Jun 2014 12:33:50 GMT
           X-Cache: MISS from WT263CDN-1231786
           X-Cache-Lookup: MISS from WT263CDN-1231786:80
           X-Cache: MISS from test.abc.com
           X-Cache-Lookup: MISS from test.abc.com:80
           Via: 1.0 WT263CDN-1231786 (squid/3.0.STABLE20), 1.0 test.abc.com (squid/3.0.STABLE20)
           Connection: close
        """
        self.__assert_waf('hsht.hs3w.com', 'West263CDN', {'X-Cache': 'MISS from WT263CDN-1231786'})

    @httpretty.activate
    def __assert_waf(self, host, vendor, fake_headers):
        httpretty.register_uri(httpretty.GET, 'http://%s/' % host, body='fake text', adding_headers=fake_headers)
        attacker = WafW00F(host)
        waf = attacker.wafdetections[vendor](attacker)
        self.assertTrue(waf)
