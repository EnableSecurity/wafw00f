<h1 align="center">
  <a href="https://github.com/enablesecurity/wafw00f"><img src="https://i.imgur.com/uAgp49o.png" alt="wafw00f"/></a>
  <br>
  WAFW00F
</h1>
<p align="center">
  <b>The Web Application Firewall Fingerprinting Tool.</b>
  <br>
  <b>
    &mdash; From <a href="https://enablesecurity.com">Enable Security</a>
  </b>
</p>
<p align="center">
  <a href="https://docs.python.org/3/download.html">
    <img src="https://img.shields.io/badge/Python-3.x/2.x-green.svg">
  </a>
  <a href="https://github.com/EnableSecurity/wafw00f/releases">
    <img src="https://img.shields.io/badge/Version-v2.2.0%20(stable)-blue.svg">
  </a>
  <a href="https://github.com/EnableSecurity/wafw00f/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203%20Clause-orange.svg">
  </a>
  <a href="https://app.travis-ci.com/github/EnableSecurity/wafw00f">
    <img src="https://app.travis-ci.com/EnableSecurity/wafw00f.svg">
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
                  \  ____/                      )
                  ,,                           ) (_
             .-. -    _______                 ( |__|
            ()``; |==|_______)                .)|__|
            / ('        /|\                  (  |__|
        (  /  )        / | \                  . |__|
         \(_)_))      /  |  \                   |__|

                    ~ WAFW00F : v2.2.0 ~
    The Web Application Firewall Fingerprinting Toolkit

[+] Can test for these WAFs:

  WAF Name                        Manufacturer
  --------                        ------------

  ACE XML Gateway                  Cisco
  aeSecure                         aeSecure
  AireeCDN                         Airee
  Airlock                          Phion/Ergon
  Alert Logic                      Alert Logic
  AliYunDun                        Alibaba Cloud Computing
  Anquanbao                        Anquanbao
  AnYu                             AnYu Technologies
  Approach                         Approach
  AppWall                          Radware
  Armor Defense                    Armor
  ArvanCloud                       ArvanCloud
  ASP.NET Generic                  Microsoft
  ASPA Firewall                    ASPA Engineering Co.
  Astra                            Czar Securities
  AWS Elastic Load Balancer        Amazon
  AzionCDN                         AzionCDN
  Azure Front Door                 Microsoft
  Barikode                         Ethic Ninja
  Barracuda                        Barracuda Networks
  Bekchy                           Faydata Technologies Inc.
  Beluga CDN                       Beluga
  BIG-IP Local Traffic Manager     F5 Networks
  BinarySec                        BinarySec
  BitNinja                         BitNinja
  BlockDoS                         BlockDoS
  Bluedon                          Bluedon IST
  BulletProof Security Pro         AITpro Security
  CacheWall                        Varnish
  CacheFly CDN                     CacheFly
  Comodo cWatch                    Comodo CyberSecurity
  CdnNS Application Gateway        CdnNs/WdidcNet
  ChinaCache Load Balancer         ChinaCache
  Chuang Yu Shield                 Yunaq
  Cloudbric                        Penta Security
  Cloudflare                       Cloudflare Inc.
  Cloudfloor                       Cloudfloor DNS
  Cloudfront                       Amazon
  CrawlProtect                     Jean-Denis Brun
  DataPower                        IBM
  DenyALL                          Rohde & Schwarz CyberSecurity
  Distil                           Distil Networks
  DOSarrest                        DOSarrest Internet Security
  DotDefender                      Applicure Technologies
  DynamicWeb Injection Check       DynamicWeb
  Edgecast                         Verizon Digital Media
  Eisoo Cloud Firewall             Eisoo
  Expression Engine                EllisLab
  BIG-IP AppSec Manager            F5 Networks
  BIG-IP AP Manager                F5 Networks
  Fastly                           Fastly CDN
  FirePass                         F5 Networks
  FortiWeb                         Fortinet
  GoDaddy Website Protection       GoDaddy
  Greywizard                       Grey Wizard
  Huawei Cloud Firewall            Huawei
  HyperGuard                       Art of Defense
  Imunify360                       CloudLinux
  Incapsula                        Imperva Inc.
  IndusGuard                       Indusface
  Instart DX                       Instart Logic
  ISA Server                       Microsoft
  Janusec Application Gateway      Janusec
  Jiasule                          Jiasule
  Kona SiteDefender                Akamai
  KS-WAF                           KnownSec
  KeyCDN                           KeyCDN
  LimeLight CDN                    LimeLight
  LiteSpeed                        LiteSpeed Technologies
  Open-Resty Lua Nginx             FLOSS
  Oracle Cloud                     Oracle
  Malcare                          Inactiv
  MaxCDN                           MaxCDN
  Mission Control Shield           Mission Control
  ModSecurity                      SpiderLabs
  NAXSI                            NBS Systems
  Nemesida                         PentestIt
  NevisProxy                       AdNovum
  NetContinuum                     Barracuda Networks
  NetScaler AppFirewall            Citrix Systems
  Newdefend                        NewDefend
  NexusGuard Firewall              NexusGuard
  NinjaFirewall                    NinTechNet
  NullDDoS Protection              NullDDoS
  NSFocus                          NSFocus Global Inc.
  OnMessage Shield                 BlackBaud
  Palo Alto Next Gen Firewall      Palo Alto Networks
  PerimeterX                       PerimeterX
  PentaWAF                         Global Network Services
  pkSecurity IDS                   pkSec
  PT Application Firewall          Positive Technologies
  PowerCDN                         PowerCDN
  Profense                         ArmorLogic
  Puhui                            Puhui
  Qcloud                           Tencent Cloud
  Qiniu                            Qiniu CDN
  Qrator                           Qrator
  Reblaze                          Reblaze
  RSFirewall                       RSJoomla!
  RequestValidationMode            Microsoft
  Sabre Firewall                   Sabre
  Safe3 Web Firewall               Safe3
  Safedog                          SafeDog
  Safeline                         Chaitin Tech.
  SecKing                          SecKing
  eEye SecureIIS                   BeyondTrust
  SecuPress WP Security            SecuPress
  SecureSphere                     Imperva Inc.
  Secure Entry                     United Security Providers
  SEnginx                          Neusoft
  ServerDefender VP                Port80 Software
  Shield Security                  One Dollar Plugin
  Shadow Daemon                    Zecure
  SiteGround                       SiteGround
  SiteGuard                        Sakura Inc.
  Sitelock                         TrueShield
  SonicWall                        Dell
  UTM Web Protection               Sophos
  Squarespace                      Squarespace
  SquidProxy IDS                   SquidProxy
  StackPath                        StackPath
  Sucuri CloudProxy                Sucuri Inc.
  Tencent Cloud Firewall           Tencent Technologies
  Teros                            Citrix Systems
  Trafficshield                    F5 Networks
  TransIP Web Firewall             TransIP
  URLMaster SecurityCheck          iFinity/DotNetNuke
  URLScan                          Microsoft
  UEWaf                            UCloud
  Varnish                          OWASP
  Viettel                          Cloudrity
  VirusDie                         VirusDie LLC
  Wallarm                          Wallarm Inc.
  WatchGuard                       WatchGuard Technologies
  WebARX                           WebARX Security Solutions
  WebKnight                        AQTRONIX
  WebLand                          WebLand
  RayWAF                           WebRay Solutions
  WebSEAL                          IBM
  WebTotem                         WebTotem
  West263 CDN                      West263CDN
  Wordfence                        Defiant
  WP Cerber Security               Cerber Tech
  WTS-WAF                          WTS
  360WangZhanBao                   360 Technologies
  XLabs Security WAF               XLabs
  Xuanwudun                        Xuanwudun
  Yundun                           Yundun
  Yunsuo                           Yunsuo
  Yunjiasu                         Baidu Cloud Computing
  YXLink                           YxLink Technologies
  Zenedge                          Zenedge
  ZScaler                          Accenture
```

## How do I use it?

First, install the tools as described [here](#how-do-i-install-it).

For help you can make use of the `--help` option. The basic usage is to pass
an URL as an argument. Example:
```
$   wafw00f https://example.org

                   ______
                  /      \
                 (  Woof! )
                  \  ____/                      )
                  ,,                           ) (_
             .-. -    _______                 ( |__|
            ()``; |==|_______)                .)|__|
            / ('        /|\                  (  |__|
        (  /  )        / | \                  . |__|
         \(_)_))      /  |  \                   |__|

                    ~ WAFW00F : v2.2.0 ~
    The Web Application Firewall Fingerprinting Toolkit

[*] Checking https://example.org
[+] The site https://example.org is behind Edgecast (Verizon Digital Media) WAF.
[~] Number of requests: 2
```

## How do I install it?

The following should do the trick:

```
python setup.py install
```

It is also possible to run it within a docker container. Clone this repository first and build the Docker image using `docker build . -t wafw00f`.
Now you can run `docker run --rm -it wafw00f https://example.com`


## Final Words

__Questions?__ Pull up an [issue on GitHub Issue Tracker](https://github.com/enablesecurity/wafw00f/issues/new) or contact [me](mailto:sandro@enablesecurity.com).
[Pull requests](https://github.com/enablesecurity/wafw00f/pulls), [ideas and issues](https://github.com/enablesecurity/wafw00f/issues) are highly welcome. If you wish to see how WAFW00F is being developed, check out the [development board](https://github.com/enablesecurity/wafw00f/projects/1).

Some useful links:

- [Documentation/Wiki](https://github.com/enablesecurity/wafw00f/wiki/)
- [Pypi Package Repository](https://pypi.org/project/wafw00f)

Presently being developed and maintained by:

- Sandro Gauci ([@SandroGauci](https://twitter.com/sandrogauci))
- Pinaki Mondal ([@0xInfection](https://twitter.com/0xinfection))
