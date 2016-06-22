#!/usr/bin/env python


NAME = 'Better WP Security'


def is_waf(self):
    r = self.normalrequest()

    if r is None:
        return False

    normalresponse, _ = r

    link_header = normalresponse.getheader('Link') or ""

    if "https://api.w.org/" not in link_header:
        # Does not appear to be a wordpress at all
        return False

    r = self.request("GET", self.path + "wp-content/plugins/better-wp-security/")

    if r is None:
        return False

    pluginresponse, _ = r

    return pluginresponse.status == 200
