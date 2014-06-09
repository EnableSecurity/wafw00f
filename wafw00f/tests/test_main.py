#!/usr/bin/env python


from unittest import TestCase

from wafw00f import WafW00F


class WafW00FTestCase(TestCase):

    def test_is360wzb(self):
        # curl -I http://www.58dm.com/
        self.__assert_waf('www.58dm.com', '360WangZhanBao')

    def test_isanquanbao(self):
        # curl -I http://www.51cdz.com/
        self.__assert_waf('www.51cdz.com', 'Anquanbao')

    def test_ischinacache(self):
        # curl -I http://s1.meituan.net/
        self.__assert_waf('s1.meituan.net', 'ChinaCache-CDN')

    def test_ispowercdn(self):
        # curl -I http://www.jjwxc.net/
        self.__assert_waf('www.jjwxc.net', 'PowerCDN')

    def test_iswest263cdn(self):
        # curl -I http://hsht.hs3w.com/
        self.__assert_waf('hsht.hs3w.com', 'West263CDN')

    def __assert_waf(self, host, vendor):
        attacker = WafW00F(host)
        waf = attacker.wafdetections[vendor](attacker)
        self.assertTrue(waf)
