from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()
from ..OUTPUT import out_dir


# ————— 𝐢𝐬𝐄𝐱𝐭𝐫𝐞𝐜𝐭 𝐃𝐨𝐦𝐚𝐢𝐧 —————
def isExtrect(soup):

    return {
        row.find_all('td')[0].text.strip()
        for row in soup.find_all('tr')
        if row.find_all('td')
    }


# ————— 𝐑𝐄𝐕𝐄𝐑𝐒𝐄 𝐈𝐏 𝐋𝐎𝐎𝐊𝐔𝐏 𝐰𝐢𝐭𝐡 𝐑𝐚𝐩𝐢𝐝𝐃𝐍𝐒 —————
def RapidDNS(IP):

    domains = set()

    print(f"\n{C.INFO}{C.C} Reverse IP LookUp with RapidDNS\n")

    try:
        response = M.requests.get(f"https://rapiddns.io/s/{IP}?full=1&down=1")

        if response.ok:
            soup = M.BeautifulSoup(response.content, 'html.parser')

            domains.update(isExtrect(soup))

        print(f"{C.P}   |\n   ╰{C.CC} Total ┈{C.OG}➢ {C.PN}{len(domains)}  {C.G}Domains / IPs\n")

        return domains

    except M.requests.exceptions.RequestException as e:
        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")
        return set()


# ————— 𝐑𝐄𝐕𝐄𝐑𝐒𝐄 𝐈𝐏 𝐋𝐎𝐎𝐊𝐔𝐏 𝐰𝐢𝐭𝐡 𝐘𝐨𝐮𝐆𝐞𝐭𝐒𝐢𝐠𝐧𝐚𝐥 —————
def YouGetSignal(IP):

    domains = set()

    print(f"\n{C.INFO}{C.C} Reverse IP LookUp with YouGetSignal\n")

    try:
        response = M.requests.post('https://domains.yougetsignal.com/domains.php', data={'remoteAddress': IP})

        if response.ok:

            domains.update(
                domain[0] for domain in response.json().get('domainArray', [])
            )

        print(f"{C.P}   |\n   ╰{C.CC} Total ┈{C.OG}➢ {C.PN}{len(domains)}  {C.G}Domains / IPs\n")

        return domains

    except M.requests.exceptions.RequestException as e:
        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")
        return set()


# ————— 𝐑𝐄𝐕𝐄𝐑𝐒𝐄 𝐈𝐏 𝐋𝐎𝐎𝐊𝐔𝐏 —————
def REVERSE_IP_LOOKUP(IP):

    print(f"\n{C.X}{C.C} Reverse IP LookUp\n\n"
         f"{C.INFO}{C.C} Need Internet Connection...\n")

    base = IP.rsplit('.', 1)[0]

    Output_Path = out_dir(f"{base}_reverse_ip.txt")

    all_IPs = set()

    all_IPs.update(RapidDNS(IP))
    all_IPs.update(YouGetSignal(IP))

    print(f"{C.CC}{'_' * 61}\n\n"
        f"\n{C.INFO} {C.C}FINAL UNIQUE IPs\n")

    with open(Output_Path, "w") as f:
        for IPs in all_IPs:

            print(f'{C.G}{IPs}')

            f.write(f"{IPs}\n")

    exit(
        f"\n{C.CC}{'_' * 61}\n\n"
        f"\n{C.S}{C.C} Total Reverse IPs {C.E} {C.OG}︻デ═一 {C.PN}{len(all_IPs)}\n"
        f"{C.P}         |\n         ╰{C.CC} OUTPUT ┈{C.OG}➢ {C.Y}{Output_Path} {C.G}✔\n"
    )