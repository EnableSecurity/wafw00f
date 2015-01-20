#!/usr/bin/env python


from setuptools import setup, find_packages


def get_reqs():
    req_lines = [line.strip() for line in open(
        'requirements/common.txt').readlines()]
    return list(filter(None, req_lines))


setup(
    name='wafw00f',
    version='0.9.3',
    description=('WAFW00F identifies and fingerprints '
                 'Web Application Firewall (WAF) products.'),
    author='sandrogauci',
    author_email='sandro@enablesecurity.com',
    license='BSD License',
    url='https://github.com/sandrogauci/wafw00f',
    packages=find_packages(),
    scripts=['wafw00f/bin/wafw00f'],
    install_requires=get_reqs(),
    test_suite='nose.collector',
)
