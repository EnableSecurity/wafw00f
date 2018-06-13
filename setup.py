#!/usr/bin/env python


from setuptools import setup, find_packages


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
    install_requires=[
        'beautifulsoup4==4.6.0',
        'pluginbase==0.7',
        'html5lib==1.0.1'
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
            'prospector==0.10.1',
        ],
        'test': [
            'httpretty==0.8.10',
            'coverage==3.7.1',
            'coveralls==0.5',
            'python-coveralls==2.5.0',
            'nose==1.3.6',
        ],
        'docs': [
            'Sphinx==1.3.1',
        ],
    },
    test_suite='nose.collector',
)
