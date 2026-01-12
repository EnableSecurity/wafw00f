#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Anubis (Techaro)'


def is_waf(self) -> bool:
    if self.matchCookie(r'-anubis-auth='):
        return True

    if self.matchContent(r'/\.within\.website/x/cmd/anubis/'):
        return True

    if self.matchContent(r'<script id="anubis_version"'):
        return True

    if self.matchContent(r'<script id="anubis_challenge"'):
        return True

    if self.matchContent(r'Protected by.*Anubis.*From.*Techaro'):
        return True

    if self.matchContent(r'github\.com/TecharoHQ/anubis'):
        return True

    return False
