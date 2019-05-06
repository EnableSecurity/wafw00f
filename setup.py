#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='wafw00f',
    version=__import__('wafw00f').__version__,
    description=('WAFW00F identifies and fingerprints '
                 'Web Application Firewall (WAF) products.'),
    author='Sandro Gauci',
    author_email='sandro@enablesecurity.com',
    license='BSD License',
    url='https://github.com/sandrogauci/wafw00f',
    packages=find_packages(),
    scripts=['wafw00f/bin/wafw00f'],
    install_requires=[
        'beautifulsoup4',
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
