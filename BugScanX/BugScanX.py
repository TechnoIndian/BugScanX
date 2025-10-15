from .C_M import CM; C = CM()
from .CLI import parse_arguments

# ————— import Plugin —————
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


EXCLUDE_LOCATION = 'https://jio.com/BalanceExhaust'


def CLEAR():
    C.os.system('cls' if C.os.name == 'nt' else 'clear')


# ————— Install Required Module —————

required_modules = ['requests', 'ping3', 'tabulate', 'bs4']

for module in required_modules:

    try:
        __import__(module)
    except ImportError:
        print(f"{C.S}{C.P} Installing {C.E}{C.C} {module} module...{C.G}\n")

        try:
            C.subprocess.check_call([C.sys.executable, "-m", "pip", "install", module])

            print(f"\n{C.X}{C.C} {module} Installed Successfully.{C.G} ✔\n")

            CLEAR()

        except (C.subprocess.CalledProcessError, Exception):
            exit(f"\n{C.ERROR} No Internet Connection. ✘\n"
                f"\n{C.INFO}{C.RD} Internet Connection is Required to Install {C.RD}'{C.G}pip install {module}{C.RD}' ✘\n")


CLEAR()

Date = C.datetime.now().strftime('%d/%m/%y')

# Logo 🙏

b64 = """eJzVlc9LAkEUx8/Ov9DlMXgNzDICL2UGSWBgQoEHWWwxqVGw5hB4kJK8VBQWnSI6B3XoIkT0DxT0J5R26pJ/QjOzM7Mz61bUrbe6P+b7eW/eezOrAMJGCmNkpDA+lUwk47E4GVy0r9n3FpbdjVKNuEqfIKltdR8nebe0Vq1BprpacdhoTLshFIkA9QyBaZRGfbNESxnSuRjIEeT0o0YC3MnyCTNNKEAXBClaXio51RUVLJz/OSRmt9i4mghWgMCpHBWDOnXOQxDhsUMIat/6LcVeD9lJ8tSeRKdmpmnpfsn6GljOKDYOLrIV91OkUZAHFUl468wwEc4ohaM0Sv1BASClUTtd1T61ZZC9qQTKTU5nqEg4Y2ziFKzN56msCzIAj2WHZ89MMxvBJ4FAVCRXxggdgKSmqlSzYyOwhYspsVH/kHm4yu1rDtR+i4SL+oUYdFo78Hp4+X513msdw6CzdwQf3bv+brt3evTWbcLLwxk83zzeP3UW+Ik/81cH9ZonoZ/GV8L3n7+4/cLHQpHVg0mSdYjLa5K9adhq3t1wy3WHaKIRcF9czs7lAv5aTDtb7r/vV+B3ud/cN/8Y+s0DUX1DVZ0g0/X1LUFUOFDdHNJzC8X83Ox8drGYyaYzM1JHnz8nFUI="""

print(C.zlib.decompress(C.base64.b64decode(b64)).decode('utf-8').rstrip('\n') + f'{C.B}{Date}{C.R}\n' + "————————|——————————————————|—————————————————|——————————————|————")


# ————— GENERATE CIDR —————
def isIP_CIDR(CIDR):

    try:
        IP_Range = C.ipaddress.ip_network(CIDR, strict=False)

        return [str(IP) for IP in IP_Range]

    except ValueError as e:
        print(f'\n{C.ERROR} Invalid CIDR : {e} ✘\n')

        print(f'\n{C.INFO}{C.C} CIDR {C.G}127.0.0.0/24 {C.R}OR {C.C}Multi CIDR {C.G}127.0.0.0/24 104.0.0.0/24\n')

        return []


# ————— HOST FILE —————
def isHOST_FILE(file_path):

    HOSTS = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            
            lines = [line.strip() for line in file.readlines() if line.strip()]

            lines = list(dict.fromkeys(lines))

            for line in lines:
                if '/' in line:
                    HOSTS.extend(isIP_CIDR(line))
                else:
                    HOSTS.append(line)

    except (OSError, ValueError) as e:
        exit(f'\n{C.ERROR} {e}\n')

    return HOSTS


# ————— Time Management —————
def isTime(elapsed_time):
    days = int(elapsed_time // 86400)
    hours = int((elapsed_time % 86400) // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)

    if elapsed_time < 3600:
        # MM:SS
        return f"{minutes:02}:{seconds:02}"
    elif elapsed_time < 86400:
        # HH:MM:SS
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        # DD:HH:MM:SS
        return f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}"


# ————— IP Address Generate —————
def isIP_Add(HOST):

    try:
        C.ipaddress.ip_address(HOST)

        return True

    except ValueError:

        return False


# ————— Get IP Address —————
def Get_IP_Address(HOST):

    try:
        return C.socket.gethostbyname_ex(HOST)[2]

    except C.socket.gaierror:
        return []


# ————— CHECK HTTP's RESPONSE —————
def isRequest(HOST, PORT, isTimeOut, Method='HEAD', isHTTPS=False):

    if isHTTPS or PORT == "443":
        URL = f"https://{HOST}:{PORT}"
    else:
        URL = f"http://{HOST}:{PORT}"

    try:
        response = C.requests.request(Method, URL, timeout=isTimeOut, allow_redirects=False)

        IP = Get_IP_Address(HOST)

        if EXCLUDE_LOCATION in response.headers.get('LOCATION', ''):
            return None

        SERVER = response.headers.get('Server', '')

        LOCATION = response.headers.get('LOCATION')

        STATUS = f"{C.P}{response.status_code:<6}" if LOCATION and LOCATION.startswith(f"https://{HOST}") else f"{response.status_code:<6}"

        return IP, STATUS, SERVER, PORT, HOST, LOCATION

    except C.requests.exceptions.RequestException:
        return None


# ————— ROW Format —————
def isROW(IP, STATUS, SERVER, PORT, HOST, LOCATION=None, color=C.R):

    if SERVER == '':
        row = C.GR
    elif 'cloudflare' in SERVER:
        row = C.G
    elif 'CloudFront' in SERVER:
        row = C.C
    elif SERVER.startswith('Akamai'):
        row = C.Y
    elif SERVER.startswith('Varnish'):
        row = C.B
    elif SERVER.startswith('BunnyCDN'):
        row = C.OG
    else:
        row = None

    IP_color = Server_color = PORT_color = HOST_color = row or C.R

    isLocation = f' -> {C.G}{LOCATION}' if LOCATION else ''

    return (f'{IP_color}{IP:<16} {STATUS:<6}   {Server_color}{SERVER:<22}{PORT_color}{PORT:<5}   {HOST_color}{HOST}{isLocation}')


# ————— Execute Script —————
def RK_TECHNO_INDIA():

    args = parse_arguments()

    HOSTS = []

    if args.CIDR:
        for CIDR in args.CIDR:
            HOSTS.extend(isIP_CIDR(CIDR))

        isIP = isCIDR = False

    elif args.file:
        for file_path in args.file:
            if not C.os.path.isfile(file_path):
                exit(f"{C.ERROR} File {file_path} not found. ✘\n")

            HOSTS.extend(isHOST_FILE(file_path))

        isIP = any(isIP_Add(HOST) for HOST in HOSTS)
        isCIDR = False

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


    if C.os.name == 'posix':
        C.subprocess.run(['termux-wake-lock'])
        print(f"\n{C.X} {C.C} Acquiring Wake Lock...\n")

    BugScaner(HOSTS, isIP, isIP_Add, isCIDR, isROW, isRequest, isTime, isTimeOut = args.timeout, PORTS = args.PORT, Output_Path = args.output, Threads = args.threads, isHTTPS = args.https, Method = args.methods)

    print(f'\n🚩 {C.R}࿗ {C.OG}Jai Shree Ram {C.R}࿗ 🚩\n     🛕🛕🙏🙏🙏🛕🛕\n')

    if C.os.name == 'posix':
        C.subprocess.run(['termux-wake-unlock'])
        exit(f"\n{C.X} {C.C} Releasing Wake Lock...\n")