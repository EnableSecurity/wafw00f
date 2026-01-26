#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Reflected Networks (Reflected Networks)'


def is_waf(self):
    if self.matchContent('<img class="logo loader" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAbgAAABHCAIAAAD6G8WcAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw') and \
        self.matchStatus(403) and \
        self.matchContent(r'content="Request is denied"') and \
        self.matchContent(r'<title>Forbidden</title>'):
        return True

    return False
