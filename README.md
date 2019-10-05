<h1 align="center">
  <a href="https://github.com/enablesecurity/wafw00f"><img src="https://i.imgur.com/uAgp49o.png" alt="wafw00f"/></a>
  <br>
  WAFW00F
</h1>
<p align="center">
  <b>The #1 Web Application Firewall Fingerprinting Tool.</b>
  <br>
  <b>
    &mdash; From <a href="https://enablesecurity.com">Enable Security</a> & <a href="https://twitter.com/0xInfection">0xInfection</a>
  </b>
</p>
<p align="center">
  <a href="https://docs.python.org/3/download.html">
    <img src="https://img.shields.io/badge/Python-3.x/2.x-green.svg">
  </a>
  <a href="https://github.com/EnableSecurity/wafw00f/releases">
    <img src="https://img.shields.io/badge/Version-v1.0.0%20(stable)-blue.svg">
  </a>
  <a href="https://github.com/EnableSecurity/wafw00f/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203%20Clause-orange.svg">
  </a> 
  <a href="https://travis-ci.org/EnableSecurity/wafw00f">
    <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg?logo=travis">
  </a>
</p>

## How does it work?
To do its magic, WAFW00F does the following:

- Sends a _normal_ HTTP request and analyses the response; this identifies a
  number of WAF solutions.
- If that is not successful, it sends a number of (potentially malicious) HTTP
  requests and uses simple logic to deduce which WAF it is.
- If that is also not successful, it analyses the responses previously
  returned and uses another simple algorithm to guess if a WAF or security
  solution is actively responding to our attacks.

For further details, check out the source code on our [main repository](https://github.com/EnableSecurity/wafw00f).

## What does it detect?
WAFW00F can detect a number of firewalls, a list of which is as below:

```
$ wafw00f -l

                 ______
                /      \
               (  Woof! )
                \______/                      )
                ,,                           ) (_
           .-. -    _______                 ( |__|
          ()``; |==|_______)                .)|__|
          / ('        /|\                  (  |__|
      (  /  )        / | \                  . |__|
       \(_)_))      /  |  \                   |__|

    WAFW00F - The Web Application Firewall Detection Tool

Can test for these WAFs:

aeSecure (aeSecure)
Airlock (Phion/Ergon)
Alert Logic (Alert Logic)
AliYunDun (Alibaba Cloud Computing)
Anquanbao (Anquanbao)
AnYu (AnYu Technologies)
Approach (Approach)
AppTrana (Indusface)
Armor Defense (Armor)
ArvanCloud (ArvanCloud)
ASPA Firewall (ASPA Engineering Co.)
ASP.NET Generic Protection (Microsoft)
Astra Web Protection (Czar Securities)
AWS Elastic Load Balancer (Amazon)
Yunjiasu (Baidu Cloud Computing)
Barikode (Ethic Ninja)
Barracuda Application Firewall (Barracuda Networks)
Bekchy (Faydata Technologies Inc.)
BinarySec (BinarySec)
BitNinja (BitNinja)
BlockDoS (BlockDoS)
Bluedon (Bluedon IST)
BulletProof Security Pro (AITpro Security)
CacheWall (Varnish)
CdnNS Application Gateway (CdnNs/WdidcNet)
WP Cerber Security (Cerber Tech)
ChinaCache CDN Load Balancer (ChinaCache)
Chuang Yu Shield (Yunaq)
ACE XML Gateway (Cisco)
Cloudbric (Penta Security)
Cloudflare (Cloudflare Inc.)
Cloudfloor Application Firewall (Cloudfloor DNS)
Cloudfront (Amazon)
Comodo cWatch (Comodo CyberSecurity)
CrawlProtect (Jean-Denis Brun)
DenyALL (Rohde & Schwarz CyberSecurity)
Distil (Distil Networks)
DOSarrest (DOSarrest Internet Security)
DotDefender (Applicure Technologies)
DynamicWeb Injection Check (DynamicWeb)
e3Learning Firewall
Edgecast (Verizon Digital Media)
Eisoo Cloud Firewall (Eisoo)
Expression Engine (EllisLab)
BIG-IP Access Policy Manager (F5 Networks)
BIG-IP Application Security Manager (F5 Networks)
BIG-IP Local Traffic Manager (F5 Networks)
FirePass (F5 Networks)
Trafficshield (F5 Networks)
FortiWeb (Fortinet)
GoDaddy Website Protection (GoDaddy)
Greywizard (Grey Wizard)
Huawei Cloud Firewall (Huawei)
HyperGuard (Art of Defense)
DataPower (IBM)
Imunify360 (CloudLinux)
Incapsula (Imperva Inc.)
IndusGuard (Indusface)
Instart DX (Instart Logic)
ISA Server (Microsoft)
Janusec Application Gateway (Janusec)
Jiasule (Jiasule)
KeyCDN (KeyCDN)
KS-WAF (KnownSec)
Kona Site Defender (Akamai)
LiteSpeed Firewall (LiteSpeed Technologies)
Malcare (Inactiv)
Mission Control Application Shield (Mission Control)
ModSecurity (SpiderLabs)
NAXSI (NBS Systems)
Nemesida (PentestIt)
NetContinuum (Barracuda Networks)
NetScaler AppFirewall (Citrix Systems)
NevisProxy (AdNovum)
Newdefend (NewDefend)
NexusGuard Firewall (NexusGuard)
NinjaFirewall (NinTechNet)
NSFocus (NSFocus Global Inc.)
NullDDoS Protection (NullDDoS)
OnMessage Shield (BlackBaud)
Open-Resty Lua Nginx WAF
Palo Alto Next Gen Firewall (Palo Alto Networks)
PentaWAF (Global Network Services)
PerimeterX (PerimeterX)
pkSecurity Intrusion Detection System
PowerCDN (PowerCDN)
Profense (ArmorLogic)
Positive Technologies Application Firewall (PT Security)
Puhui (Puhui)
Qiniu (Qiniu CDN)
AppWall (Radware)
Reblaze (Reblaze)
RSFirewall (RSJoomla!)
ASP.NET RequestValidationMode (Microsoft)
Sabre Firewall (Sabre)
Safe3 Web Firewall (Safe3)
Safedog (SafeDog)
Safeline (Chaitin Tech.)
SecKing (SecKing)
SecuPress WordPress Security (SecuPress)
Secure Entry (United Security Providers)
eEye SecureIIS (BeyondTrust)
SecureSphere (Imperva Inc.)
SEnginx (Neusoft)
ServerDefender VP (Port80 Software)
Shadow Daemon (Zecure)
Shield Security (One Dollar Plugin)
SiteGround (SiteGround)
SiteGuard (Sakura Inc.)
Sitelock (TrueShield)
SonicWall (Dell)
UTM Web Protection (Sophos)
Squarespace (Squarespace)
SquidProxy IDS
StackPath (StackPath)
Sucuri CloudProxy (Sucuri Inc.)
Tencent Cloud Firewall (Tencent Technologies)
Teros (Citrix Systems)
TransIP Web Firewall (TransIP)
UEWaf (UCloud)
URLMaster SecurityCheck (iFinity/DotNetNuke)
URLScan (Microsoft)
Varnish (OWASP)
Viettel (Cloudrity)
VirusDie (VirusDie LLC)
Wallarm (Wallarm Inc.)
WatchGuard (WatchGuard Technologies)
WebARX (WebARX Security Solutions)
WebKnight (AQTRONIX)
WebLand (WebLand)
RayWAF (WebRay Solutions)
WebSEAL (IBM)
WebTotem (WebTotem)
West263 Content Delivery Network
Wordfence (Defiant)
WTS-WAF (WTS)
360WangZhanBao (360 Technologies)
XLabs Security WAF (XLabs)
Xuanwudun
Yundun (Yundun)
Yunsuo (Yunsuo)
YXLink (YxLink Technologies)
Zenedge (Zenedge)
ZScaler (Accenture)
```

## How do I use it?
First, install the tools as described [here](#how-do-i-install-it).

For help you can make use of the `--help` option. The basic usage is to pass
an URL as an argument. Example:
```
$  wafw00f https://example.org

             ______
            /      \
           (  Woof! )
            \______/                      )
            ,,                           ) (_
       .-. -    _______                 ( |__|
      ()``; |==|_______)                .)|__|
      / ('        /|\                  (  |__|
  (  /  )        / | \                  . |__|
   \(_)_))      /  |  \                   |__|

    WAFW00F - Web Application Firewall Detection Tool

Checking https://example.org
The site https://example.org is behind Edgecast (Verizon Digital Media) WAF.
Number of requests: 1
```

## How do I install it?
The following should do the trick:
```
python setup.py install
```

## Final Words
__Questions?__ Pull up an [issue on GitHub Issue Tracker](https://github.com/enablesecurity/wafw00f/issues/new) or contact [me](mailto:sandro@enablesecurity.com). [Pull requests](https://github.com/enablesecurity/wafw00f/pulls), [ideas and issues](https://github.com/enablesecurity/wafw00f/issues) are highly welcome. If you wish to see what how WAFW00F is being developed, check out the [Development Board](https://github.com/enablesecurity/wafw00f/projects/1).

> Copyright © [Enable Security](https://enablesecurity.com) & [0xInfection](https://twitter.com/0xInfection).
