from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()
from ..OUTPUT import out_dir


# ————— 𝐂𝐫𝐭𝐒𝐇 —————
def CrtSH(domain):

    subdomains = set()

    print(f"\n{C.INFO} {C.C}SUBDOMAINS FIND WITH CrtSH\n")

    try:
        response = M.requests.get(f"https://crt.sh/?q={domain}&output=json")

        if response and response.headers.get('Content-Type') == 'application/json':
            for entry in response.json():
                subdomains.update(entry['name_value'].splitlines())

            print(f"{C.P}   |\n   ╰{C.CC} Total ┈{C.OG}➢ {C.PN}{len(subdomains)} {C.G}subdomains\n")

        return subdomains

    except M.requests.exceptions.RequestException as e:
        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")
        return set()


# ————— 𝐇𝐚𝐜𝐤𝐞𝐫𝐓𝐚𝐫𝐠𝐞𝐭 —————
def HackerTarget(domain):

    subdomains = set()

    print(f"\n{C.INFO} {C.C}SUBDOMAINS FIND WITH HackerTarget\n")

    try:
        response = M.requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}")

        if response and 'text' in response.headers.get('Content-Type', ''):
            subdomains.update([line.split(",")[0] for line in response.text.splitlines()])

            print(f"{C.P}   |\n   ╰{C.CC} Total ┈{C.OG}➢ {C.PN}{len(subdomains)} {C.G}subdomains\n")

        return subdomains

    except M.requests.exceptions.RequestException as e:
        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")
        return set()


# ————— 𝐑𝐚𝐩𝐢𝐝𝐃𝐍𝐒 —————
def RapidDNS(domain):

    subdomains = set()

    print(f"\n{C.INFO} {C.C}SUBDOMAINS FIND WITH RapidDNS\n")

    try:
        response = M.requests.get(f"https://rapiddns.io/subdomain/{domain}?full=1")

        if response:
            soup = M.BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('td'):
                text = link.get_text(strip=True)

                if text.endswith(f".{domain}"):
                    subdomains.add(text)

            print(f"{C.P}   |\n   ╰{C.CC} Total ┈{C.OG}➢ {C.PN}{len(subdomains)} {C.G}subdomains\n")

        return subdomains

    except M.requests.exceptions.RequestException as e:
        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")
        return set()


# ————— 𝐀𝐧𝐮𝐛𝐢𝐬𝐃𝐁 —————
def AnubisDB(domain):

    subdomains = set()

    print(f"\n{C.INFO} {C.C}SUBDOMAINS FIND WITH AnubisDB\n")

    try:
        response = M.requests.get(f"https://anubisdb.com/anubis/subdomains/{domain}")

        if response:
            subdomains.update(response.json())
            print(f"{C.P}   |\n   ╰{C.CC} Total ┈{C.OG}➢ {C.PN}{len(subdomains)} {C.G}subdomains\n")

        return subdomains

    except M.requests.exceptions.RequestException as e:
        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")
        return set()


# ————— 𝐀𝐥𝐢𝐞𝐧𝐕𝐚𝐮𝐥𝐭 —————
def AlienVault(domain):

    subdomains = set()

    print(f"\n{C.INFO} {C.C}SUBDOMAINS FIND WITH AlienVault\n")

    try:
        response = M.requests.get(f"https://otx.alienvault.com/otxapi/indicators/domain/url_list/{domain}?limit=500")

        if response:
            for entry in response.json().get("url_list", []):
                hostname = entry.get("hostname")

                if hostname:
                    subdomains.add(hostname)

            print(f"{C.P}   |\n   ╰{C.CC} Total ┈{C.OG}➢ {C.PN}{len(subdomains)} {C.G}subdomains\n")

        return subdomains

    except M.requests.exceptions.RequestException as e:

        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")

        return set()


# ————— 𝐂𝐞𝐫𝐭𝐒𝐩𝐨𝐭𝐭𝐞𝐫 —————
def CertSpotter(domain):

    subdomains = set()

    print(f"\n{C.INFO} {C.C}SUBDOMAINS FIND WITH CertSpotter\n")

    try:
        response = M.requests.get(f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names")

        if response:
            for cert in response.json():
                subdomains.update(cert.get('dns_names', []))

            print(f"{C.P}   |\n   ╰{C.CC} Total ┈{C.OG}➢ {C.PN}{len(subdomains)} {C.G}subdomains\n")

        return subdomains

    except M.requests.exceptions.RequestException as e:
        print(f"\n{C.ERROR} Please Check Your Internet Connect & Try Again\n")
        return set()


# ————— 𝐒𝐔𝐁_𝐃𝐎𝐌𝐀𝐈𝐍_𝐅𝐈𝐍𝐃𝐄𝐑 —————
def SUB_DOMAIN_FINDER(domain):

    print(f"\n{C.INFO}{C.C} Need Internet Connection...{C.G}\n\n"
         f"\n{C.X}{C.C} Be Patience, SubFinder Takes Time...\n"
    )

    base = domain.rsplit('.', 1)[0]

    Output_Path = out_dir(f"{base}_subdomains.txt")

    all_subdomains = set()

    all_subdomains.update(CrtSH(domain))
    all_subdomains.update(HackerTarget(domain))
    all_subdomains.update(RapidDNS(domain))
    all_subdomains.update(AnubisDB(domain))
    all_subdomains.update(AlienVault(domain))
    all_subdomains.update(CertSpotter(domain))

    print(f"{C.CC}{'_' * 61}\n\n"
        f"\n{C.INFO} {C.C}FINAL UNIQUE SUBDOMAINS\n")

    with open(Output_Path, "w") as f:
        for subdomain in all_subdomains:

            print(f'{C.G}{subdomain}')

            f.write(f"{subdomain}\n")

    exit(
        f"\n\n{C.S}{C.C} SubDomains {C.E} {C.OG}︻デ═一 {C.PN}{len(all_subdomains)}\n"
        f"{C.P}       |\n       ╰{C.CC} OUTPUT ┈{C.OG}➢ {C.Y}{Output_Path} {C.G}✔\n"
    )