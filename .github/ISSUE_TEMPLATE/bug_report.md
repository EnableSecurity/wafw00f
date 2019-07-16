---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: sandrogauci

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Command that reproduces the issue. e.g. `wafw00f http://example.org -a -vv`

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. Windows, Linux]
 - OS version, distribution: 
 - Python version: [e.g. python 3.2]

**Debug output**
Paste the output that you get when passing `-vv` to wafw00f. Example:

```
INFO:root:The url www.example.org should start with http:// or https:// .. fixing (might make this unusable)
Checking http://www.example.org
INFO:root:starting wafw00f on http://www.example.org
INFO:wafw00f:Sending GET /
send: 'GET / HTTP/1.1\r\nHost: www.example.org\r\nAccept-Encoding: identity\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nAccept: */*\r\nUser-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b1) Gecko/20081007 Firefox/3.0\r\n\r\n'
reply: 'HTTP/1.1 200 OK\r\n'
header: Accept-Ranges: bytes
header: Cache-Control: max-age=604800
header: Content-Type: text/html; charset=UTF-8
header: Date: Tue, 30 Apr 2019 13:23:52 GMT
header: Etag: "1541025663+ident"
header: Expires: Tue, 07 May 2019 13:23:52 GMT
header: Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
header: Server: ECS (dcb/7EC9)
header: Vary: Accept-Encoding
header: X-Cache: HIT
header: Content-Length: 1270
INFO:wafw00f:Checking for Yunjiasu (Baidu Cloud Computing)
INFO:wafw00f:Checking for PowerCDN (PowerCDN)
INFO:wafw00f:Checking for ChinaCache CDN Load Balancer (ChinaCache)
INFO:wafw00f:Checking for Edgecast (Verizon Digital Media)
INFO:root:Ident WAF: ['Edgecast (Verizon Digital Media)']
The site http://www.example.org is behind Edgecast (Verizon Digital Media) WAF.
Number of requests: 1
```

**Additional context**
Add any other context about the problem here.
