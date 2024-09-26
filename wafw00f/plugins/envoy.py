#!/usr/bin/env python
'''
Copyright (C) 2022, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Envoy (EnvoyProxy)'


def is_waf(self):
    if self.matchHeader(('server', 'envoy')):
        return True

    if self.matchHeader(('x-envoy-upstream-service-time', '.+')):
        return True

    if self.matchHeader(('x-envoy-downstream-service-cluster', '.+')):
        return True

    if self.matchHeader(('x-envoy-downstream-service-node', '.+')):
        return True

    if self.matchHeader(('x-envoy-external-address', '.+')):
        return True

    if self.matchHeader(('x-envoy-force-trace', '.+')):
        return True

    if self.matchHeader(('x-envoy-internal', '.+')):
        return True

    if self.matchHeader(('x-envoy-original-dst-host', '.+')):
        return True

    if self.matchHeader(('x-envoy-original-path', '.+')):
        return True

    if self.matchHeader(('x-envoy-local-overloaded', '.+')):
        return True

    return False
