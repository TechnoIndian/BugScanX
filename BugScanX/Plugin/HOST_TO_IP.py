from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()


# ————— 𝐇𝐎𝐒𝐓 𝐓𝐎 𝐈𝐏 —————
def HOST_TO_IP(SNI):

    print(f"\n{C.X}{C.C} HOST/SNI To IPV4 & IPV6 IP Convert\n"
         f"\n{C.INFO} {C.C} Need Internet Connection...\n")

    try:
        Address = M.socket.getaddrinfo(SNI, None)

        IPv4 = {add[4][0] for add in Address if add[0] == M.socket.AF_INET}

        if IPv4:
            print(f"\n{C.X}{C.C} IPv4 IP Address {C.G}\n\n" + '\n'.join(IPv4))

        IPv6 = {add[4][0] for add in Address if add[0] == M.socket.AF_INET6}

        if IPv6:
            print(f"\n{C.X}{C.C} IPv6 IP Address {C.G}\n\n" + '\n'.join(IPv6))
        
        exit('\n')

    except Exception as e:
        exit(f"\n{C.ERROR} {e} ✘\n")