# WAFW00F

WAFW00F identifies and fingerprints Web Application Firewall (WAF) products.

## How does it work?

To do its magic, WAFW00F does the following:

- Sends a _normal_ HTTP request and analyses the response; this identifies a
  number of WAF solutions.
- If that is not successful, it sends a number of (potentially malicious) HTTP
  requests and uses simple logic to deduce which WAF it is.
- If that is also not successful, it analyses the responses previously
  returned and uses another simple algorithm to guess if a WAF or security
  solution is actively responding to our attacks.

For further details, check out the source code on the main site,
[github.com/EnableSecurity/wafw00f](https://github.com/EnableSecurity/wafw00f).

## What does it detect?

It detects a number of WAFs. To view which WAFs it is able to detect run
WAFW00F with the `-l` option. At the time of writing the output is as follows:

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

    WAFW00F - Web Application Firewall Detection Tool

Can test for these WAFs:

aeSecure (aeSecure)
Airlock (Phion/Ergon)
Alert Logic (Alert Logic)
AliYunDun (Alibaba Cloud Computing)
Anquanbao (Anquanbao)
AnYu (AnYu Technologies)
Approach (Approach)
Armor Defense (Armor)
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
CacheWall (Varnish)
CdnNS Application Gateway (CdnNs/WdidcNet)
WP Cerber Security (Cerber Tech)
ChinaCache CDN Load Balancer (ChinaCache)
Chuang Yu Shield (Yunaq)
ACE XML Gateway (Cisco)
Cloudbric (Penta Security)
Cloudflare (Cloudflare Inc.)
Cloudfront (Amazon)
Comodo cWatch (Comodo CyberSecurity)
CrawlProtect (Jean-Denis Brun)
DenyALL (Rohde & Schwarz CyberSecurity)
Distil (Distil Networks)
DOSarrest (DOSarrest Internet Security)
DotDefender (Applicure Technologies)
DynamicWeb Injection Check (DynamicWeb)
Edgecast (Verizon Digital Media)
Expression Engine (EllisLab)
BIG-IP Access Policy Manager (F5 Networks)
BIG-IP Application Security Manager (F5 Networks)
BIG-IP Local Traffic Manager (F5 Networks)
FirePass (F5 Networks)
Trafficshield (F5 Networks)
FortiWeb (Fortinet)
GoDaddy Website Protection (GoDaddy)
Greywizard (Grey Wizard)
HyperGuard (Art of Defense)
DataPower (IBM)
Imunify360 (CloudLinux)
Incapsula (Imperva Inc.)
Instart DX (Instart Logic)
ISA Server (Microsoft)
Janusec Application Gateway (Janusec)
Jiasule (Jiasule)
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
OnMessage Shield (BlackBaud)
Open-Resty Lua Nginx WAF
Palo Alto Next Gen Firewall (Palo Alto Networks)
PerimeterX (PerimeterX)
pkSecurity Intrusion Detection System
PowerCDN (PowerCDN)
Profense (ArmorLogic)
AppWall (Radware)
Reblaze (Reblaze)
RSFirewall (RSJoomla!)
ASP.NET RequestValidationMode (Microsoft)
Sabre Firewall (Sabre)
Safe3 Web Firewall (Safe3)
Safedog (SafeDog)
Safeline (Chaitin Tech.)
SecuPress WordPress Security (SecuPress)
Secure Entry (United Security Providers)
eEye SecureIIS (BeyondTrust)
SecureSphere (Imperva Inc.)
SEnginx (Neusoft)
Shield Security (One Dollar Plugin)
SiteGround (SiteGround)
SiteGuard (Sakura Inc.)
Sitelock (TrueShield)
SonicWall (Dell)
UTM Web Protection (Sophos)
Squarespace (Squarespace)
StackPath (StackPath)
Sucuri CloudProxy (Sucuri Inc.)
Tencent Cloud Firewall (Tencent Technologies)
Teros (Citrix Systems)
TransIP Web Firewall (TransIP)
URLMaster SecurityCheck (iFinity/DotNetNuke)
URLScan (Microsoft)
Varnish (OWASP)
VirusDie (VirusDie LLC)
Wallarm (Wallarm Inc.)
WatchGuard (WatchGuard Technologies)
WebARX (WebARX Security Solutions)
WebKnight (AQTRONIX)
WebSEAL (IBM)
WebTotem (WebTotem)
West263 Content Delivery Network
Wordfence (Feedjit)
WTS-WAF (WTS)
360WangZhanBao (360 Technologies)
XLabs Security WAF (XLabs)
Xuanwudun
Yundun (Yundun)
Yunsuo (Yunsuo)
Zenedge (Zenedge)
ZScaler (Accenture)
```

## How do I use it?

First, install the tools as described [here](#how-do-i-install-it).

For help please make use of the `--help` option. The basic usage is to pass it
a URL as an argument. Example:

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


## How do I install it?

The following should do the trick:

    python setup.py install

## Looking for pentesters?

More information about the services that we offer at [Enable Security](http://enablesecurity.com/)

## How do I write my own new checks?

Follow the instructions on the [wiki](https://github.com/EnableSecurity/wafw00f/wiki/How-to-write-new-WAF-checks)

## Questions?

Pull up an [issue](https://github.com/enablesecurity/wafw00f/issues/new) or contact [me](mailto:sandro@enablesecurity.com).

