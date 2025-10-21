<p align="center">
<a href="https://t.me/rktechnoindians"><img title="Made in INDIA" src="https://img.shields.io/badge/MADE%20IN-INDIA-SCRIPT?colorA=%23ff8100&colorB=%23017e40&colorC=%23ff0000&style=for-the-badge"></a>
</p>

<a name="readme-top"></a>

<div align="center">
    <img src="https://raw.githubusercontent.com/TechnoIndian/BugScanX/refs/heads/main/assets/logo.png" width="128" height="128"/>
    <p align="center"> 
        <a href="https://t.me/rktechnoindians"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=800&size=35&pause=1000&color=F74848&center=true&vCenter=true&random=false&width=435&lines=BugScanX" /></a>
    </p>
    <p>
        <b>All-in-One Tool for Finding SNI Bug Hosts</b>
    </p>
    <p>
        🔍 Bug Host Discovery • 🌐 SNI Host Scanning • 🛡️ HTTP Analysis • 📊 Host Intelligence
    </p>
</div>

<p align="center">
    <img src="https://img.shields.io/github/stars/TechnoIndian/BugScanX?color=e57474&labelColor=1e2528&style=for-the-badge"/>
    <img src="https://img.shields.io/pypi/dm/BugScan?color=67b0e8&labelColor=1e2528&style=for-the-badge"/>
    <img src="https://img.shields.io/pypi/v/BugScan?color=8ccf7e&labelColor=1e2528&style=for-the-badge"/>
    <img src="https://img.shields.io/github/license/TechnoIndian/BugScanX?color=f39c12&labelColor=1e2528&style=for-the-badge"/>
    <img src="https://img.shields.io/github/last-commit/TechnoIndian/BugScanX?color=9b59b6&labelColor=1e2528&style=for-the-badge"/>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B"/>
    <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS%20%7C%20Android-2D2D2D?style=for-the-badge&logo=windows&logoColor=white"/>
</p>

# Inspired

[![GitHub](https://img.shields.io/badge/GitHub-%2312100E?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aztecrabbit/bugscanner)

[![GitHub](https://img.shields.io/badge/GitHub-%2312100E?style=for-the-badge&logo=github&logoColor=white)](https://github.com/FreeNetLabs/BugScanX)


IPv4 & IPv6 Subnet Size Reference Table
-------
`❗ Be careful with IPv6 Scans, I wouldn't recommend scanning CIDR over 1 million number of IP ☠️`

| IPv4                                      | IPv6                                      |
|-------------------------------------------|-------------------------------------------|
| [![IPv4](https://img.shields.io/badge/IPv4-%238A2BE2?style=for-the-badge&logo=internet-explorer&logoColor=white)](https://technoindian.github.io/BugScanX/assets/IPv4.html) | [![IPv6](https://img.shields.io/badge/IPv6-%238A2BE2?style=for-the-badge&logo=internet-explorer&logoColor=white)](https://technoindian.github.io/BugScanX/assets/IPv6.html) |


Install
-------

[![PyPI](https://img.shields.io/badge/pypi-%233775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/BugScan)


**BugScanX**

    pip install BugScan

Updating
--------

    pip install --upgrade BugScan


# Usage Example


BugScanX ( File Mode )
-----

**BugScanX**


**Mode file ( File Path / Multi File Path )**

`Input File Path [ Support in File :- CIDR / IP / Host ( Domain / SubDomain )  ]`

    BugScanX Your_TXT_Path.txt
    
`Multi File`

    BugScanX Your_TXT_Path.txt Your_TXT_Path_2.txt Your_TXT_Path_3.txt

**Mode file ( CIDR & IP / Multi CIDR & IP )**

`Input CIDR ( IP-Range )`

    BugScanX 1.1.1.1/24
    
`Multi CIDR`

    BugScanX 1.1.1.1/24 1.0.0.1/24 104.16.0.0/30

**Mode file [ HOST ( Domain & SubDomain ) ]**

`Input HOST`

    BugScanX www.cloudflare.com
    
`Multi HOST`

    BugScanX www.cloudflare.com www.google.com

`Mixed No Limit ( But Keep Space ) 🥱`

    BugScanX scan.txt www.cloudflare.com google.com 1.0.0.1 1.1.1.1/30


BugScanX ( Addition Flags )
-----

**Addition Flag -p ( Port )**

`Input Port ( Defult is 80 )`

    BugScanX subdomain.txt --p 443
    
`Multi Port`
    
    BugScanX subdomain.txt --p 80 443 53

**Addition Flag -https**

    BugScanX subdomain.txt -http
    
**Addition Flag -m ( Input Methods, Defult is HEAD ) [ GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE ]**

    BugScanX subdomain.txt -m GET

**Addition Flag -rr ( RESPONSE Check )**

`-rr Response Check`

    BugScanX subdomain.txt -rr

**Addition Flag -t ( TimeOut ) -T ( Thareds ) -o ( Output )**

`-t ( Input Timeout, Defult is 3 )`

    BugScanX subdomain.txt -t 3
    
`-T ( Input Thareds, Defult is 64)`
    
    BugScanX subdomain.txt -T 100
    
`-o ( Disabled, Because Currently Forwarded to Default [ Default is /sdcard/ & $HOME ] )`
    
    BugScanX subdomain.txt -o /sdcard/other_result.txt

BugScanX ( Other Mode )
-----

**Mode -g CIDR To IP ( Input CIDR 127.0.0.0/24, NOTE Currently Supported Single CIDR )**

    BugScanX -g 127.0.0.0/24

**Mode -ip Domain to IPv4 & IPv6 IP Convert ( Input Host/Domain )**

    BugScanX -ip cloudflare.com

**Mode -op Check OpenPort ( Input Host/Domain/IP )**

    BugScanX -op cloudflare.com

**Mode -ping Ping Check ( Input Host/Domain/IP )**

    BugScanX -ping cloudflare.com

**Mode -r Reverse IP LookUp ( Input IP )**

    BugScanX -r 1.1.1.1

**Mode -s Sub Domains Finder ( Input Domain, NOTE Currently Supported Single Domain )**

    BugScanX -s cloudflare.com

**Mode -tls TLS Connection Check ( Input Host/Domain/IP )**

    BugScanX -tls cloudflare.com

**Mode -txt Split TXT File**

    BugScanX -txt subdomain.txt

Note
----

## 🇮🇳 Welcome By Techno India 🇮🇳

[![Telegram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)](https://t.me/rktechnoindians)
  </a><p>
[![Telegram](https://img.shields.io/badge/TELEGRAM-OWNER-red?style=for-the-badge&logo=telegram)](https://t.me/RK_TECHNO_INDIA)
</p>