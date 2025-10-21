from .CLI import parse_arguments
from .ANSI_COLORS import ANSI; C = ANSI()
from .MODULES import IMPORT; M = IMPORT()

# ————— 𝐢𝐦𝐩𝐨𝐫𝐭 𝐏𝐥𝐮𝐠𝐢𝐧 —————
from BugScanX.Plugin.PING import PING
from BugScanX.Plugin.Split_TXT import Split_TXT
from BugScanX.Plugin.BUG_SCAN import BugScaner
from BugScanX.Plugin.CIDR_TO_IP import CIDR_TO_IP
from BugScanX.Plugin.TLS_CHECK import CHECK_TLS
from BugScanX.Plugin.PORT_SCAN import PORT_SCAN
from BugScanX.Plugin.HOST_TO_IP import HOST_TO_IP
from BugScanX.Plugin.IP_LOOKUP import REVERSE_IP_LOOKUP
from BugScanX.Plugin.SUBFINDER import SUB_DOMAIN_FINDER
from BugScanX.Plugin.RESPONSE_CHECK import CHECK_RESPONSE


def CLEAR():
    M.os.system('cls' if M.os.name == 'nt' else 'clear')

# ————— 𝐈𝐧𝐬𝐭𝐚𝐥𝐥 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐌𝐨𝐝𝐮𝐥𝐞 —————

required_modules = ['requests', 'ping3', 'tabulate', 'bs4']

for module in required_modules:

    try:
        __import__(module)
    except ImportError:
        print(f"{C.S}{C.P} Installing {C.E}{C.C} {module} module...{C.G}\n")

        try:
            M.subprocess.check_call([M.sys.executable, "-m", "pip", "install", module])

            print(f"\n{C.X}{C.C} {module} Installed Successfully.{C.G} ✔\n")

            CLEAR()

        except (M.subprocess.CalledProcessError, Exception):
            exit(f"\n{C.ERROR} No Internet Connection. ✘\n"
                f"\n{C.INFO}{C.CC} Internet Connection is Required to Install {C.CC}'{C.G}pip install {module}{C.CC}' ✘\n")


CLEAR()

Date = M.datetime.now().strftime('%d/%m/%y')

# 𝐋𝐨𝐠𝐨 🙏

b64 = """eJzVlc9LAkEUx8/Ov9DlMXgNzDICL2UGSWBgQoEHWWwxqVGw5hB4kJK8VBQWnSI6B3XoIkT0DxT0J5R26pJ/QjOzM7Mz61bUrbe6P+b7eW/eezOrAMJGCmNkpDA+lUwk47E4GVy0r9n3FpbdjVKNuEqfIKltdR8nebe0Vq1BprpacdhoTLshFIkA9QyBaZRGfbNESxnSuRjIEeT0o0YC3MnyCTNNKEAXBClaXio51RUVLJz/OSRmt9i4mghWgMCpHBWDOnXOQxDhsUMIat/6LcVeD9lJ8tSeRKdmpmnpfsn6GljOKDYOLrIV91OkUZAHFUl468wwEc4ohaM0Sv1BASClUTtd1T61ZZC9qQTKTU5nqEg4Y2ziFKzN56msCzIAj2WHZ89MMxvBJ4FAVCRXxggdgKSmqlSzYyOwhYspsVH/kHm4yu1rDtR+i4SL+oUYdFo78Hp4+X513msdw6CzdwQf3bv+brt3evTWbcLLwxk83zzeP3UW+Ik/81cH9ZonoZ/GV8L3n7+4/cLHQpHVg0mSdYjLa5K9adhq3t1wy3WHaKIRcF9czs7lAv5aTDtb7r/vV+B3ud/cN/8Y+s0DUX1DVZ0g0/X1LUFUOFDdHNJzC8X83Ox8drGYyaYzM1JHnz8nFUI="""

print(M.zlib.decompress(M.base64.b64decode(b64)).decode('utf-8').rstrip('\n') + f'{C.B}{Date}{C.CC}\n' + "————————|——————————————————|—————————————————|——————————————|————")


# ————— 𝐢𝐬𝐈𝐏_𝐂𝐈𝐃𝐑 —————
def isIP_CIDR(CIDR):

    try:
        IP_Range = M.ipaddress.ip_network(CIDR, strict=False)

        return [str(IP) for IP in IP_Range]

    except ValueError as e:
        print(f'\n{C.ERROR} Invalid CIDR / HOST / FILE PATH : {e} ✘\n')

        print(f'\n{C.INFO}{C.C} CIDR {C.G}127.0.0.0/24 {C.CC}OR {C.C}Multi CIDR {C.G}127.0.0.0/24 104.0.0.0/24\n')

        return []


WARNING = False

# ————— 𝐇𝐎𝐒𝐓 𝐅𝐈𝐋𝐄 —————
def isHOST_FILE(file_path):

    HOSTS = []
    
    global WARNING

    try:
        # ————— 𝐈𝐟 𝐅𝐢𝐥𝐞 𝐏𝐚𝐭𝐡 𝐢𝐬 𝐄𝐱𝐢𝐬𝐭 —————
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            lines = list(dict.fromkeys(lines))
            
            for line in lines:
                # ————— 𝐂𝐈𝐃𝐑 𝐢𝐧 𝐅𝐢𝐥𝐞 —————
                if '/' in line:
                    HOSTS.extend(isIP_CIDR(line))
                else:
                    # ————— 𝐈𝐏 & 𝐇𝐎𝐒𝐓 ( 𝐃𝐎𝐌𝐀𝐈𝐍 & 𝐒𝐔𝐁𝐃𝐎𝐌𝐀𝐈𝐍 ) 𝐢𝐧 𝐅𝐢𝐥𝐞 —————
                    HOSTS.append(line)
    
    except (FileNotFoundError, IOError, OSError, ValueError):
        if not WARNING:
            print(
                  f'\n{C.INFO} {C.C} If File Path is Not Exist Then Consider {C.PN}CIDR / IP / HOST ( DOMAIN & SUBDOMAIN )\n'
                  f"\n{C.CC}{'_' * 61}\n"
            )
            
            WARNING = True

        # ————— 𝐂𝐈𝐃𝐑 —————
        if '/' in file_path:
            HOSTS.extend(isIP_CIDR(file_path))
        else:
            # ————— 𝐈𝐏 & 𝐇𝐎𝐒𝐓 ( 𝐃𝐎𝐌𝐀𝐈𝐍 & 𝐒𝐔𝐁𝐃𝐎𝐌𝐀𝐈𝐍 ) —————
            HOSTS.append(file_path)

    except Exception as e:
        exit(f'\n{C.ERROR} {e}\n')
    
    return HOSTS


# ————— 𝐓𝐢𝐦𝐞 𝐌𝐚𝐧𝐚𝐠𝐞𝐦𝐞𝐧𝐭 —————
def isTime(elapsed_time):
    days = int(elapsed_time // 86400)
    hours = int((elapsed_time % 86400) // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)

    if elapsed_time < 3600:
        # 𝐌𝐌:𝐒𝐒
        return f"{minutes:02}:{seconds:02}"
    elif elapsed_time < 86400:
        # 𝐇𝐇:𝐌𝐌:𝐒𝐒
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        # 𝐃𝐃:𝐇𝐇:𝐌𝐌:𝐒𝐒
        return f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}"


# ————— 𝐄𝐱𝐞𝐜𝐮𝐭𝐞 𝐒𝐜𝐫𝐢𝐩𝐭 —————
def RK_TECHNO_INDIA():
    
    args = parse_arguments()

    HOSTS = []


    if args.file:
        for file_path in args.file:
            HOSTS.extend(isHOST_FILE(file_path))


    if args.GENERATE_IP:
        CIDR_TO_IP(args.GENERATE_IP)


    if args.IP:
        HOST_TO_IP(args.IP)


    if args.OpenPort:
        PORT_SCAN(args.OpenPort)


    if args.ping:
        PING(args.ping)


    if args.RESPONSE:
        CHECK_RESPONSE(HOSTS, isTime)


    if args.REVERSE_IP:
        REVERSE_IP_LOOKUP(args.REVERSE_IP)


    if args.SUBFINDER:
        SUB_DOMAIN_FINDER(args.SUBFINDER)


    if args.TLS:
        CHECK_TLS(args.TLS)


    if args.Splits_TXT:
        Split_TXT(args.Splits_TXT)


    if not HOSTS:
        exit(f"\n{C.ERROR} {HOSTS} No Valid HOST To Scan. ✘\n")


    if M.os.name == 'posix':
        M.subprocess.run(['termux-wake-lock'])
        print(f"\n{C.X} {C.C} Acquiring Wake Lock...\n")


    BugScaner(

        HOSTS, isTime,
        isTimeOut = args.timeout,
        PORTS = args.PORT,
        Output_Path = args.output,
        Threads = args.threads,
        isHTTPS = args.https,
        Method = args.methods

    )


    print(f'\n🚩 {C.CC}࿗ {C.OG}Jai Shree Ram {C.CC}࿗ 🚩\n     🛕🛕🙏🙏🙏🛕🛕\n')


    if M.os.name == 'posix':
        M.subprocess.run(['termux-wake-unlock'])
        exit(f"\n{C.X} {C.C} Releasing Wake Lock...\n")