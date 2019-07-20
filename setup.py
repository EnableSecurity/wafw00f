#!/usr/bin/env python

import io
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    desc = f.read()

setup(
    name='wafw00f',
    version=__import__('wafw00f').__version__,
    long_description=desc,
    long_description_content_type='text/markdown',
    author='Sandro Gauci',
    author_email='sandro@enablesecurity.com',
    license='BSD License',
    url='https://github.com/enablesecurity/wafw00f',
    packages=find_packages(),
    scripts=['wafw00f/bin/wafw00f'],
    install_requires=[
        'pluginbase',
        'html5lib'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Topic :: Internet',
        'Topic :: Security',
        'Topic :: System :: Networking :: Firewalls',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='waf firewall detector fingerprint',
    extras_require={
        'dev': [
            'prospector',
        ],
        'test': [
            'httpretty',
            'coverage',
            'coveralls',
            'python-coveralls',
            'nose',
        ],
        'docs': [
            'Sphinx',
        ],
    },
    test_suite='nose.collector',
)
