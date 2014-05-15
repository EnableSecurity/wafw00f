#!/usr/bin/env python


from setuptools import setup, find_packages
from pip.req import parse_requirements


def get_reqs():
    install_reqs = parse_requirements('requirements.txt')
    return [str(ir.req) for ir in install_reqs]


setup(
    name='wafw00f',
    version=__import__('wafw00f').__version__,
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
