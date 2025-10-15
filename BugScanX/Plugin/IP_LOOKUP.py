from ..C_M import CM; C = CM()
from ..OUTPUT import out_dir


# ————— isExtrect Domain —————
def isExtrect(soup):

    return {
        row.find_all('td')[0].text.strip()
        for row in soup.find_all('tr')
        if row.find_all('td')
    }


# ————— REVERSE IP LOOKUP with RapidDNS —————
def RapidDNS(IP):

    domains = set()

    print(f"\n{C.INFO}{C.C} Reverse IP LookUp with RapidDNS\n")

    try:
        response = C.requests.get(f"https://rapiddns.io/s/{IP}?full=1&down=1")

        if response.ok:
            soup = C.BeautifulSoup(response.content, 'html.parser')

            domains.update(isExtrect(soup))

        print(f"{C.P}   |\n   ╰{C.R} Total ┈{C.OG}➢ {C.PN}{len(domains)}  {C.G}Domains / IPs\n")

        return domains

    except C.requests.exceptions.RequestException as e:
        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")
        return set()


# ————— REVERSE IP LOOKUP with YouGetSignal —————
def YouGetSignal(IP):

    domains = set()

    print(f"\n{C.INFO}{C.C} Reverse IP LookUp with YouGetSignal\n")

    try:
        response = C.requests.post('https://domains.yougetsignal.com/domains.php', data={'remoteAddress': IP})

        if response.ok:

            domains.update(
                domain[0] for domain in response.json().get('domainArray', [])
            )

        print(f"{C.P}   |\n   ╰{C.R} Total ┈{C.OG}➢ {C.PN}{len(domains)}  {C.G}Domains / IPs\n")

        return domains

    except C.requests.exceptions.RequestException as e:
        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")
        return set()


# ————— REVERSE IP LOOKUP —————
def REVERSE_IP_LOOKUP(IP):

    print(f"\n{C.X}{C.C} Reverse IP LookUp\n\n"
         f"{C.INFO}{C.C} Need Internet Connection...\n")

    base = IP.rsplit('.', 1)[0]

    Output_Path = out_dir(f"{base}_reverse_ip.txt")

    all_IPs = set()

    all_IPs.update(RapidDNS(IP))
    all_IPs.update(YouGetSignal(IP))

    print(f"{C.R}{'_' * 61}\n\n"
        f"\n{C.INFO} {C.C}FINAL UNIQUE IPs\n")

    with open(Output_Path, "w") as f:
        for IPs in all_IPs:

            print(f'{C.G}{IPs}')

            f.write(f"{IPs}\n")

    print(f"\n\n{C.S}{C.Y} OUTPUT {C.E} {C.PN}{len(all_IPs)} {C.C} IPs : {C.Y}{Output_Path} {C.G}✔\n")

    exit(0)