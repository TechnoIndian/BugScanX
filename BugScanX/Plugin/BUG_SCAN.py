from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()
from ..Logger import logger
from ..OUTPUT import out_dir


C_Line = f"{C.CC}{'_' * 61}"

EXCLUDE_LOCATION = 'https://jio.com/BalanceExhaust' # 𝐈𝐒𝐏 ( 𝐉𝐈𝐎 )

Date_Time = M.datetime.now().strftime(" ➢ [ %y-%m-%d ➢ %I:%M %p ]")


# ————— 𝐂𝐡𝐞𝐜𝐤 𝐕𝐚𝐢𝐥𝐝 𝐈𝐏 𝐀𝐝𝐝𝐫𝐞𝐬𝐬 —————
def isIP_Add(HOST):

    try:
        M.ipaddress.ip_address(HOST) # 𝐈𝐏𝐯𝟔 & 𝐈𝐏𝐯𝟒

        return True

    except ValueError:

        return False


# ————— 𝐢𝐬𝐈𝐏𝐯𝟔 —————
def isIPv6(HOST):

    try:
        M.ipaddress.IPv6Address(HOST)  # 𝐈𝐏𝐯𝟔

        return True

    except ValueError:

        return False


# ————— 𝐢𝐬𝐈𝐏𝐯𝟒 𝐂𝐇𝐄𝐂𝐊 —————
def isIPv4_IP(HOST):

    IPv4 = []

    # ————— 𝐆𝐞𝐭 𝐈𝐏𝐯𝟒 𝐈𝐏 —————
    try:
        def get_IPv4():
            try:
                IPv4.extend(M.socket.gethostbyname_ex(HOST)[2])
            except (M.socket.gaierror, M.socket.herror, OSError):
                pass

        Threads = M.threading.Thread(target=get_IPv4)
        Threads.daemon = True
        Threads.start()
        Threads.join(3)
    except Exception as e:
        pass

    return IPv4


# ————— 𝐆𝐄𝐓 𝐋𝐎𝐂𝐀𝐋 𝐈𝐏 —————
def isLOCAL_IP(version=4):

    # ————— 𝐈𝐏𝐯𝟔 & 𝐈𝐏𝐯𝟒 —————
    try:
        IP = M.socket.AF_INET6 if version == 6 else M.socket.AF_INET

        addr = ("2606:4700:4700::1111", 80) if version == 6 else ("1.1.1.1", 80)

        with M.socket.socket(IP, M.socket.SOCK_DGRAM) as sock:
            sock.connect(addr)

            return sock.getsockname()[0]

    except Exception:
        return None


# ————— 𝐂𝐇𝐄𝐂𝐊 𝐇𝐓𝐓𝐏'𝐬 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 —————
def isRequest(HOST, PORT, isTimeOut, Method='HEAD', isHTTPS=False):

    if isIP_Add(HOST):
        IP = [HOST]
    else:
        IP = isIPv4_IP(HOST)

    if not IP:
        return None

    PROTOCOL = 'https' if isHTTPS or PORT == "443" else 'http'

    if isIPv6(HOST):
        URL = f"{PROTOCOL}://[{HOST}]:{PORT}"
    else:
        URL = f"{PROTOCOL}://{HOST}:{PORT}"

    try:
        response = M.requests.request(Method, URL, timeout=isTimeOut, allow_redirects=False)

        if EXCLUDE_LOCATION in response.headers.get('LOCATION', ''):
            return None

        STATUS = response.status_code

        SERVER = response.headers.get('Server', '')

        LOCATION = response.headers.get('LOCATION')

        if LOCATION:
            if LOCATION.startswith(f"https://{HOST}"):
                STATUS = f"{C.P}{STATUS:<3}"

        # ————— 𝐆𝐄𝐓 𝐋𝐎𝐂𝐀𝐋 𝐈𝐏 —————
        Local_IP = {}
        for version in [4, 6]:
            IPvX = isLOCAL_IP(version)
            if IPvX:
                key = "IPv4" if version == 4 else "IPv6"
                Local_IP[key] = IPvX

        return IP, STATUS, SERVER, PORT, HOST, LOCATION, Local_IP

    except M.requests.exceptions.RequestException:
        return None


# ————— 𝐑𝐎𝐖 𝐅𝐨𝐫𝐦𝐚𝐭 —————
def isROW(IP, STATUS, SERVER, PORT, HOST, LOCATION):

    if SERVER == '':
        color = C.GR
    elif 'cloudflare' in SERVER:
        color = C.G
    elif 'CloudFront' in SERVER:
        color = C.C
    elif SERVER.startswith('Akamai'):
        color = C.Y
    elif SERVER.startswith('Varnish'):
        color = C.B
    elif SERVER.startswith('BunnyCDN'):
        color = C.OG
    else:
        color = C.CC

    isLOCATION = f' {C.OG}-> {C.DG}{LOCATION}' if LOCATION else ''

    IPv6_IP = (IP[:10] + '...') if len(IP) > 15 else IP
    return (f"\r{C.CL}{color}{IPv6_IP:<15}   {STATUS:<3}   {color}{SERVER:<22}   {PORT:<4}   {HOST}{isLOCATION}")


# ————— 𝐁𝐮𝐠 𝐒𝐜𝐚𝐧𝐞𝐫 —————
def BugScaner(HOSTS, isTime, isTimeOut, PORTS=False, Output_Path=False, Threads=False, isHTTPS=False, Method='HEAD'):

    print(f'{"  IP Address":<14}   {"Status":<3}   {"Server":<20}   {"Port":<7}   {"Host"}')

    print('---------------  ------ ----------              ------  -----------\n')

    Total_HOST = len(HOSTS) * len(PORTS)

    Scanned_HOST = Respond_HOST = 0

    Start_Time = M.time.time()

    isCloudFlare, isCloudFront = {}, {}

    Other_Responds = []

    CF_Path = out_dir("CF.txt")

    Output_Path = out_dir("other_respond.txt")

    
    with M.ThreadPoolExecutor(max_workers=Threads) as executor:

        futures = {}

        for HOST in HOSTS:
            for PORT in PORTS:
                future = executor.submit(isRequest, HOST, PORT, isTimeOut, Method, isHTTPS)
                futures[future] = (HOST, PORT)

        for future in M.as_completed(futures):
            Scanned_HOST += 1
            CURRENT_HOST, _ = futures[future]
            RESULT = future.result()

            if RESULT:
                Respond_HOST += 1

                IP, STATUS, SERVER, PORT, HOST, LOCATION, Local_IP = RESULT

                print(isROW(IP[0], STATUS, SERVER, PORT, HOST, LOCATION))

                if 'cloudflare' in SERVER:
                    isCloudFlare[HOST] = (IP, Local_IP)
                elif 'CloudFront' in SERVER:
                    isCloudFront[HOST] = (IP, Local_IP)
                else:
                    Other_Responds.append((IP[0], STATUS, SERVER, HOST, Local_IP))

            progress_line = (
                f"- PC - {(Scanned_HOST / Total_HOST) * 100:.2f}% "
                f"- SN - {Scanned_HOST}/{Total_HOST} "
                f"- RS - {Respond_HOST} "
                f"- <{isTime(M.time.time() - Start_Time)}> "
                f"- {CURRENT_HOST}"
            )

            logger(progress_line)

    print(f'\n{C_Line}\n')

    # ————— 𝐂𝐥𝐨𝐮𝐝𝐅𝐥𝐚𝐫𝐞 & 𝐂𝐥𝐨𝐮𝐝𝐅𝐫𝐨𝐧𝐭 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 𝐎𝐔𝐓𝐏𝐔𝐓 —————
    def OUTPUT_LOGS(HOST_IP, Server_Name, Color):

        if HOST_IP:
            print(f"\n{Color}# {Server_Name}\n")

            Output_Logs = [
                f"\n# 𝐈𝐧𝐩𝐮𝐭 𝐏𝐚𝐭𝐡 ➢ " + ' '.join(M.sys.argv[1:]) + Date_Time + f"\n\n# {Server_Name}\n"
            ]

            for HOST, (IPs, isLocal_IP) in HOST_IP.items():

                print(f"{HOST} {C.PN}{isLocal_IP}{Color}")

                Output_Logs.append(f"{HOST}\n# 𝐋𝐨𝐜𝐚𝐥 𝐈𝐏 ➢ {isLocal_IP}\n")

            if not isIP_Add(HOST):
                Output_Logs.extend('\r')

                Total_IP = sorted(
                     set(
                        IP for IPs in HOST_IP.values()
                        for IP in IPs[0]
                    )
                )

                Output_Logs.extend(Total_IP)

                print("\n" + "\n".join(Total_IP))

            with open(CF_Path, 'a') as file:
                file.write("\n" + "\n".join(Output_Logs) + "\n")

    if isCloudFlare:
        OUTPUT_LOGS(isCloudFlare, "CloudFlare", C.G)

        print(f'\n{C_Line}\n')

    if isCloudFront:
        OUTPUT_LOGS(isCloudFront, "CloudFront", C.C)

        print(f'\n{C_Line}\n')

    if isCloudFlare or isCloudFront:
        print(
             f"\n{C.S}{C.C} CF OUTPUT {C.E} {C.OG}︻デ═一 {C.Y}{CF_Path} {C.G}✔\n"
             f"\n{C_Line}\n"
        )

    # ————— 𝐎𝐓𝐇𝐄𝐑 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 𝐎𝐔𝐓𝐏𝐔𝐓 —————
    if Other_Responds:

        with open(Output_Path, 'a') as file:

            file.write(f"\n# 𝐈𝐧𝐩𝐮𝐭 𝐏𝐚𝐭𝐡 ➢ " + ' '.join(M.sys.argv[1:]) + f" {Date_Time}\n\n")

            for RESPONSE in Other_Responds:
                IP, STATUS, SERVER, HOST, is_Local_IP = RESPONSE

                if isIP_Add(HOST):
                    file.write(f"{IP} | {STATUS} | {SERVER}\n# 𝐋𝐨𝐜𝐚𝐥 𝐈𝐏 ➢ {is_Local_IP}\n\n")
                else:
                    file.write(f"{IP} | {STATUS} | {SERVER} | {HOST}\n# 𝐋𝐨𝐜𝐚𝐥 𝐈𝐏 ➢ {is_Local_IP}\n\n")

        print(
             f'\n{C.S}{C.C} Other Respond OUTPUT {C.E} {C.OG}︻デ═一 {C.Y}{Output_Path} {C.G}✔\n'
             f'\n{C_Line}\n'
        )