#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'Reflected Networks (Reflected Networks)'


def is_waf(self):
    if self.matchContent(r'<b>Request ID</b>') and \
        self.matchContent('<img class="logo loader" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAbgAAABHCAIAAAD6G8WcAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMS1jMDAwIDc5LmRhYmFjYmIsIDIwMjEvMDQvMTQtMDA6Mzk6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMy4wIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo4NzUwMTkzQjkzMUExMUVDOTcyN0UzNDdGNzZENTdCMiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo4NzUwMTkzQzkzMUExMUVDOTcyN0UzNDdGNzZENTdCMiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjg3NTAxOTM5OTMxQTExRUM5NzI3RTM0N0Y3NkQ1N0IyIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjg3NTAxOTNBOTMxQTExRUM5NzI3RTM0N0Y3NkQ1N0IyIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+aSp5xgAAKvRJREFUeNrsXQdcE2f/J4OEFQh7T5GtgAouxNlqX0et1j1a22qHq9rxvlW7rK3a4eiw1j3rqKNu1DpwgQwBAdl7BNlJCITM/y8ELk8ugxCCyr/3NR8/ueMu99zdc9/n+xvP70hSqdSIAAECBAhoBpm4BAQIECCgHdRe1NakEnZMRo2vg/') and \
        self.matchStatus(403) and \
        self.matchContent(r'content="Request is denied"') and \
        self.matchContent(r'<title>Forbidden</title>'):
        return True

    return False
