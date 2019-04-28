#!/usr/bin/env python


NAME = 'StackPath (StackPath)'


def is_waf(self):
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        _, page = r
        if all(i in page for i in (b'This website is using a security service to protect itself',
            b'You performed an action that triggered the service and blocked your request')):
            return True
    return False