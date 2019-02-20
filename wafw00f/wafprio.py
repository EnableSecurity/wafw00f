#!/usr/bin/env python

# NOTE: this priority list is used so that each check can be prioritized,
# so that the quick checks are done first and ones that require more
# requests, are done later


wafdetectionsprio = [
    # cached default request ones first
    'Profense',
    'AdNovum nevisProxy',
    'NetContinuum',
    'Incapsula WAF',
    'CloudFlare',
    'NSFocus',
    'DOSarrest',
    'Sucuri WAF',
    'Edgecast / Verizon Digital media',
    'Comodo WAF',
    'XLabs Security WAF',
    'FortiWeb',
    'Wallarm',
    'BlockDoS',
    'Radware AppWall',
    'Naxsi',
    'Safedog',
    'Mission Control Application Shield',
    'USP Secure Entry Server',
    'Cisco ACE XML Gateway',
    'Barracuda Application Firewall',
    'Art of Defence HyperGuard',
    'BinarySec',
    'Teros WAF',
    'F5 BIG-IP LTM',
    'F5 BIG-IP APM',
    'F5 BIG-IP ASM',
    'F5 FirePass',
    'F5 Trafficshield',
    'AWS WAF',
    'Ergon Airlock',
    'Citrix NetScaler',
    'IBM DataPower',
    # the next ones require attack strings to be sent
    'Trustwave ModSecurity',
    'IBM Web Application Security',
    'DenyALL WAF',
    'Applicure dotDefender',
    'Juniper WebApp Secure',
    'Microsoft URLScan',
    'Aqtronix WebKnight',
    'eEye Digital Security SecureIIS',
    'Imperva SecureSphere',
    'Microsoft ISA Server'
]
