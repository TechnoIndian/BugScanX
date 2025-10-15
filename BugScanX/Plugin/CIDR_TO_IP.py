from ..C_M import CM; C = CM()
from ..OUTPUT import out_dir


# ————— CIDR TO IP —————
def CIDR_TO_IP(CIDR):

    try:
        IP_Range = C.ipaddress.ip_network(CIDR, strict=False)

        IP_List = [str(IP) for IP in IP_Range]

        Base_IP = str(IP_Range.network_address)

        OUTPUT = out_dir(f"{Base_IP}_IPs.txt")

        with open(OUTPUT, 'w', encoding='utf-8') as f:
            for IPs in IP_List:
                f.write(IPs + "\n")

        exit(f"\n{C.X} {C.C} {CIDR} To IPs {C.R}= {C.PN}{len(IP_List)} {C.OG}➸❥ {C.Y}'{OUTPUT}' {C.G}✔\n")

    except ValueError as e:
        print(f"\n{C.ERROR} ✘ Invalid CIDR : {e}\n")
        exit(f"\n{C.ERROR} Example: 127.0.0.0/24\n")