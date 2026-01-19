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
    <img src="https://img.shields.io/badge/Python-3.8+-green.svg">
  </a>
  <a href="https://github.com/EnableSecurity/wafw00f/releases">
    <img src="https://img.shields.io/badge/Version-v2.3.2%20(stable)-blue.svg">
  </a>
  <a href="https://github.com/EnableSecurity/wafw00f/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203%20Clause-orange.svg">
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


                  ?              ,.   (   .      )        .      "
          __        ??          ("     )  )'     ,'        )  . (`     '`
    (___()'`;   ???          .; )  ' (( (" )    ;(,     ((  (  ;)  "  )")
    /,___ /`                 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( ' )
    \\   \\                 |____|____|____|____|____|____|____|____|____|

                                ~ WAFW00F : v2.3.2 ~
                  ~ Sniffing Web Application Firewalls since 2014 ~

[+] Can test for these WAFs:

  WAF Name                        Manufacturer
  --------                        ------------

  360PanYun                        360 Technologies
  360WangZhanBao                   360 Technologies
  ACE XML Gateway                  Cisco
  ASP.NET Generic                  Microsoft
  ASPA Firewall                    ASPA Engineering Co.
  AWS Elastic Load Balancer        Amazon
  AireeCDN                         Airee
  Airlock                          Phion/Ergon
  Alert Logic                      Alert Logic
  AliYunDun                        Alibaba Cloud Computing
  AnYu                             AnYu Technologies
  Anquanbao                        Anquanbao
  Anubis                           Techaro
  AppWall                          Radware
  Approach                         Approach
  Armor Defense                    Armor
  ArvanCloud                       ArvanCloud
  Astra                            Czar Securities
  Azion Edge Firewall              Azion
  Azure Application Gateway        Microsoft
  Azure Front Door                 Microsoft
  BIG-IP AP Manager                F5 Networks
  BIG-IP AppSec Manager            F5 Networks
  BIG-IP Local Traffic Manager     F5 Networks
  Barikode                         Ethic Ninja
  Barracuda                        Barracuda Networks
  Baffin Bay                       Mastercard
  Bekchy                           Faydata Technologies Inc.
  Beluga CDN                       Beluga
  BinarySec                        BinarySec
  BitNinja                         BitNinja
  BlockDoS                         BlockDoS
  Bluedon                          Bluedon IST
  BulletProof Security Pro         AITpro Security
  CacheFly CDN                     CacheFly
  CacheWall                        Varnish
  CdnNS Application Gateway        CdnNs/WdidcNet
  ChinaCache Load Balancer         ChinaCache
  Chuang Yu Shield                 Yunaq
  Cloud Protector                  Rohde & Schwarz CyberSecurity
  Cloudbric                        Penta Security
  Cloudflare                       Cloudflare Inc.
  Cloudfloor                       Cloudfloor DNS
  Cloudfront                       Amazon
  Comodo cWatch                    Comodo CyberSecurity
  CrawlProtect                     Jean-Denis Brun
  DDoS-GUARD                       DDOS-GUARD CORP.
  DOSarrest                        DOSarrest Internet Security
  DataPower                        IBM
  DenyALL                          Rohde & Schwarz CyberSecurity
  Distil                           Distil Networks
  DotDefender                      Applicure Technologies
  DynamicWeb Injection Check       DynamicWeb
  Edgecast                         Verizon Digital Media
  Eisoo Cloud Firewall             Eisoo
  Envoy                            EnvoyProxy
  Expression Engine                EllisLab
  Fastly                           Fastly CDN
  FirePass                         F5 Networks
  FortiGate                        Fortinet
  FortiGuard                       Fortinet
  FortiWeb                         Fortinet
  GoDaddy Website Protection       GoDaddy
  Google Cloud App Armor           Google Cloud
  Greywizard                       Grey Wizard
  Huawei Cloud Firewall            Huawei
  HyperGuard                       Art of Defense
  ISA Server                       Microsoft
  Imunify360                       CloudLinux
  Incapsula                        Imperva Inc.
  IndusGuard                       Indusface
  Instart DX                       Instart Logic
  Janusec Application Gateway      Janusec
  Jiasule                          Jiasule
  KS-WAF                           KnownSec
  Kemp LoadMaster                  Progress Software
  KeyCDN                           KeyCDN
  Kona SiteDefender                Akamai
  LimeLight CDN                    LimeLight
  Link11 WAAP                      Link11
  LiteSpeed                        LiteSpeed Technologies
  Malcare                          Inactiv
  MaxCDN                           MaxCDN
  Mission Control Shield           Mission Control
  ModSecurity                      SpiderLabs
  NAXSI                            NBS Systems
  NSFocus                          NSFocus Global Inc.
  Nemesida                         PentestIt
  NetContinuum                     Barracuda Networks
  NetScaler AppFirewall            Citrix Systems
  NevisProxy                       AdNovum
  Newdefend                        NewDefend
  NexusGuard Firewall              NexusGuard
  NinjaFirewall                    NinTechNet
  NullDDoS Protection              NullDDoS
  OnMessage Shield                 BlackBaud
  Open-Resty Lua Nginx             FLOSS
  Oracle Cloud                     Oracle
  PT Application Firewall          Positive Technologies
  Palo Alto Next Gen Firewall      Palo Alto Networks
  PentaWAF                         Global Network Services
  PerimeterX                       PerimeterX
  PowerCDN                         PowerCDN
  Profense                         ArmorLogic
  Puhui                            Puhui
  Qcloud                           Tencent Cloud
  Qiniu                            Qiniu CDN
  Qrator                           Qrator
  RSFirewall                       RSJoomla!
  RayWAF                           WebRay Solutions
  Reblaze                          Reblaze
  RequestValidationMode            Microsoft
  SEnginx                          Neusoft
  Sabre Firewall                   Sabre
  Safe3 Web Firewall               Safe3
  Safedog                          SafeDog
  Safeline                         Chaitin Tech.
  Scutum                           Secure Sky Technology Inc.
  SecKing                          SecKing
  SecuPress WP Security            SecuPress
  Secure Entry                     United Security Providers
  SecureSphere                     Imperva Inc.
  ServerDefender VP                Port80 Software
  Shadow Daemon                    Zecure
  Shield Security                  One Dollar Plugin
  SiteGround                       SiteGround
  SiteGuard                        EG Secure Solutions Inc.
  Sitelock                         TrueShield
  SonicWall                        Dell
  Squarespace                      Squarespace
  SquidProxy IDS                   SquidProxy
  StackPath                        StackPath
  Sucuri CloudProxy                Sucuri Inc.
  Tencent Cloud Firewall           Tencent Technologies
  Teros                            Citrix Systems
  ThreatX                          A10 Networks
  Trafficshield                    F5 Networks
  TransIP Web Firewall             TransIP
  UEWaf                            UCloud
  URLMaster SecurityCheck          iFinity/DotNetNuke
  URLScan                          Microsoft
  UTM Web Protection               Sophos
  Variti                           Variti
  Varnish                          OWASP
  Viettel                          Cloudrity
  VirusDie                         VirusDie LLC
  WP Cerber Security               Cerber Tech
  WTS-WAF                          WTS
  Wallarm                          Wallarm Inc.
  WatchGuard                       WatchGuard Technologies
  WebARX                           WebARX Security Solutions
  WebKnight                        AQTRONIX
  WebLand                          WebLand
  WebSEAL                          IBM
  WebTotem                         WebTotem
  West263 CDN                      West263CDN
  Wordfence                        Defiant
  XLabs Security WAF               XLabs
  Xuanwudun                        Xuanwudun
  YXLink                           YxLink Technologies
  Yundun                           Yundun
  Yunjiasu                         Baidu Cloud Computing
  Yunsuo                           Yunsuo
  ZScaler                          Accenture
  Zenedge                          Zenedge
  aeSecure                         aeSecure
  eEye SecureIIS                   BeyondTrust
  pkSecurity IDS                   pkSec
  wpmudev WAF                      Incsub
  Shieldon Firewall                Shieldon.io
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

                    ~ WAFW00F : v2.3.2 ~
    The Web Application Firewall Fingerprinting Toolkit

[*] Checking https://example.org
[+] The site https://example.org is behind Edgecast (Verizon Digital Media) WAF.
[~] Number of requests: 2
```

## How do I install it?

### Install from PyPI (recommended)
Run:
```
python3 -m pip install wafw00f
```
or
```
pip3 install wafw00f
```

### Via Docker
It is also possible to run it within a docker container. Clone this repository first and build the Docker image using:
```
docker build . -t wafw00f
```
Now you can run:
```
docker run --rm -it wafw00f https://example.com
```

### From source
> NOTE: Be careful to not break your system packages while installing wafw00f. Use venv as and when required.

Clone the repository:
```
git clone https://github.com/enablesecurity/wafw00f.git
```
Then:
```
cd wafw00f/
python3 -m pip install .
```

Or, by using pipx directly:
```
pipx install git+https://github.com/EnableSecurity/wafw00f.git
```

## Final Words

__Questions?__ Pull up an [issue on GitHub Issue Tracker](https://github.com/enablesecurity/wafw00f/issues/new) or contact [me](mailto:sandro@enablesecurity.com).
[Pull requests](https://github.com/enablesecurity/wafw00f/pulls), [ideas and issues](https://github.com/enablesecurity/wafw00f/issues) are highly welcome.

Some useful links:

- [Documentation/Wiki](https://github.com/enablesecurity/wafw00f/wiki/)
- [Pypi Package Repository](https://pypi.org/project/wafw00f)

Presently being developed and maintained by:

- Sandro Gauci ([@SandroGauci](https://twitter.com/sandrogauci))
- Pinaki Mondal ([@0xInfection](https://twitter.com/0xinfection))
