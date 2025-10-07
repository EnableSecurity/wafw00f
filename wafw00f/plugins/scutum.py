#!/usr/bin/env python3
"""
Copyright (C) 2025, WAFW00F Developers.
See the LICENSE file for copying permission.
"""

NAME = "Scutum (Secure Sky Technology Inc.)"


def is_waf(self):
    if self.matchHeader(("Server", "Scutum")):
        return True

    return False
