#!/usr/bin/env python


NAME = 'Better WP Security'


def is_waf(self):
    normalresponse, _ = self.normalrequest()
    link_header = normalresponse.getheader('Link') or ""

    if "https://api.w.org/" not in link_header:
        # Does not appear to be a wordpress at all
        return False

    r = self.request("GET", "/wp-content/plugins/better-wp-security/")

    if not r:
        return False

    pluginresponse, _ = r

    return pluginresponse.status == 200
