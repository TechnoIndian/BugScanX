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


Install
-------

[![PyPI](https://img.shields.io/badge/pypi-%233775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/BugScan)

**BugScanX**

    pip install BugScan

Updating
--------

    pip install --upgrade BugScan

Usage
-----

**BugScanX**


**Mode -f ( File_Path )**

`Input File Path ( Support Host/Domain/SubDomain/CIDR/IP )`

    BugScanX -f Your_TXT_Path.txt
    
`Multi File`

    BugScanX -f Your_TXT_Path.txt Your_TXT_Path_2.txt Your_TXT_Path_3.txt

**Mode -c ( CIDR / IP-Range )**

`Input CIDR ( IP-Range )`

    BugScanX -c 127.0.0.1/24
    
`Multi CIDR`

    BugScanX -c 127.0.0.1/24 128.0.0.0/24 104.18.25.0/30

BugScanX ( Addition Flags )
-----

**Addition Flag -p ( Port ) with -f & -c**

`Input Port ( Defult is 80 )`

    BugScanX -f subdomain.txt --p 443
    
`Multi Port`
    
    BugScanX -f subdomain.txt --p 80 443 53

**Addition Flag -https**

    BugScanX -f subdomain.txt -http
    
**Addition Flag -m ( Input Methods, Defult is HEAD ) [ GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE ]**

    BugScanX -f subdomain.txt -m GET

**Addition Flag -rr ( RESPONSE Check )**

`-rr Response Check`

    BugScanX -f subdomain.txt -rr

**Addition Flag -t ( TimeOut ) -T ( Thareds ) -o ( Output )**

`-t ( Input Timeout, Defult is 3 )`

    BugScanX -f subdomain.txt -t 3
    
`-T ( Input Thareds, Defult is 64)`
    
    BugScanX -f subdomain.txt -T 100
    
`-o ( Disabled, Because Currently Forwarded to Default [ Default is /sdcard/ & $HOME ] )`
    
    BugScanX -f subdomain.txt -o /sdcard/other_result.txt

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

    BugScanX -r 127.0.0.1

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