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

    BlockDoS (BlockDoS)
    Armor Defense (Armor)
    ACE XML Gateway (Cisco)
    Malcare (Inactiv)
    RSFirewall (RSJoomla!)
    PerimeterX (PerimeterX)
    Varnish (OWASP)
    Barracuda Application Firewall (Barracuda Networks)
    Anquanbao (Anquanbao)
    NetContinuum (Barracuda Networks)
    HyperGuard (Art of Defense)
    Incapsula (Imperva Inc.)
    Safedog (SafeDog)
    NevisProxy (AdNovum)
    SEnginx (Neusoft)
    BitNinja (BitNinja)
    Janusec Application Gateway (Janusec)
    NinjaFirewall (NinTechNet)
    Edgecast (Verizon Digital Media)
    Alert Logic (Alert Logic)
    Cloudflare (Cloudflare Inc.)
    SecureSphere (Imperva Inc.)
    Bekchy (Faydata Technologies Inc.)
    Kona Site Defender (Akamai)
    Wallarm (Wallarm Inc.)
    Cloudfront (Amazon)
    aeSecure (aeSecure)
    eEye SecureIIS (BeyondTrust)
    VirusDie (VirusDie LLC)
    DOSarrest (DOSarrest Internet Security)
    SiteGround (SiteGround)
    Chuang Yu Shield (Yunaq)
    Yunsuo (Yunsuo)
    NAXSI (NBS Systems)
    UTM Web Protection (Sophos)
    Approach (Approach)
    NetScaler AppFirewall (Citrix Systems)
    DynamicWeb Injection Check (DynamicWeb)
    Xuanwudun
    WebTotem (WebTotem)
    Comodo (Comodo CyberSecurity Solutions)
    WTS-WAF (WTS)
    PowerCDN (PowerCDN)
    BIG-IP Access Policy Manager (F5 Networks)
    BinarySec (BinarySec)
    Greywizard (Grey Wizard)
    Shield Security (One Dollar Plugin)
    ASP.NET Generic Protection (Microsoft)
    CacheWall (Varnish)
    Expression Engine (EllisLab)
    Airlock (Phion/Ergon)
    WatchGuard (WatchGuard Technologies)
    WP Cerber Security (Cerber Tech)
    Yunjiasu (Baidu Cloud Computing)
    DenyALL (Rohde & Schwarz CyberSecurity)
    AnYu (AnYu Technologies)
    Secure Entry (United Security Providers)
    ISA Server (Microsoft)
    Yundun (Yundun)
    FirePass (F5 Networks)
    GoDaddy Website Protection (GoDaddy)
    Imunify360 (CloudLinux)
    Safe3 Web Firewall (Safe3)
    WebSEAL (IBM)
    NSFocus (NSFocus Global Inc.)
    360WangZhanBao (360 Technologies)
    Squarespace (Squarespace)
    Imperva SecureSphere
    Bluedon (Bluedon IST)
    AliYunDun (Alibaba Cloud Computing)
    Wordfence (Feedjit)
    Palo Alto Next Gen Firewall (Palo Alto Networks)
    Tencent Cloud Firewall (Tencent Technologies)
    West263CDN
    WebARX (WebARX Security Solutions)
    Mission Control Application Shield (Mission Control)
    BIG-IP Local Traffic Manager (F5 Networks)
    Sitelock (TrueShield)
    ZScaler (Accenture)
    CrawlProtect (Jean-Denis Brun)
    Teros (Citrix Systems)
    AWS Elastic Load Balancer (Amazon)
    Cloudbric (Penta Security)
    StackPath (StackPath)
    URLScan (Microsoft)
    Sucuri (Sucuri Inc.)
    TransIP Web Firewall (TransIP)
    OnMessage Shield (BlackBaud)
    Distil (Distil Networks)
    Profense (ArmorLogic)
    ModSecurity (SpiderLabs)
    FortiWeb (Fortinet)
    XLabs Security WAF (XLabs)
    ASP.NET RequestValidationMode (Microsoft)
    Jiasule (Jiasule)
    ChinaCache CDN Load Balancer (ChinaCache)
    URLMaster SecurityCheck (iFinity/DotNetNuke)
    Reblaze (Reblaze)
    Newdefend (NewDefend)
    Trafficshield (F5 Networks)
    KS-WAF (KnownSec)
    SiteGuard (Sakura Inc.)
    CdnNS Application Gateway (CdnNs/WdidcNet)
    DataPower (IBM)
    WebKnight (AQTRONIX)
    BIG-IP Application Security Manager (F5 Networks)
    Barikode (Ethic Ninja)
    Zenedge (Zenedge)
    SonicWall (Dell)
    DotDefender (Applicure Technologies)
    USP Secure Entry Server
    AppWall (Radware)

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

Contact [me](mailto:sandro@enablesecurity.com)

