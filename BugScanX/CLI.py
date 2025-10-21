from .ANSI_COLORS import ANSI; C = ANSI()
from .MODULES import IMPORT; M = IMPORT()

from .ANSI_COLORS import ANSI; C = ANSI()
from .MODULES import IMPORT; M = IMPORT()


# ————— 𝐩𝐚𝐫𝐬𝐞 𝐚𝐫𝐠𝐮𝐦𝐞𝐧𝐭𝐬 —————
def parse_arguments():
    print()
    class CustomArgumentParser(M.argparse.ArgumentParser):

        def format_help(self):
            help_text = super().format_help()
            help_text = help_text.replace(f'{C.Y}➢', f'\n{" " * 22}{C.Y}➢')

            return help_text

        def error(self, message):
            exit(
                f'\nerror: {message}\n'
                f'{next((action.help for action in self._actions if action.option_strings and action.option_strings[0] in message), "")}\n'
            )

    args = M.sys.argv[1:]

    if any(arg.startswith('-') for arg in args):
        parser = CustomArgumentParser(description=f'{C.C}BugScanX Script')
    else:
        parser = M.argparse.ArgumentParser(description=f'{C.C}BugScanX Script')

    group = parser.add_mutually_exclusive_group(required=False)

    parser.add_argument(
        'file',
        nargs='*',
        type=str,
        help=f'{C.Y}➢ {C.C}File Path {C.Y}/sdcard/scan.txt {C.CC}OR {C.C}Multi File {C.Y}/sdcard/scan1.txt /sdcard/scan2.txt\n'
              f'{C.Y}➢ {C.C}CIDR {C.G}127.0.0.0/24 {C.CC}OR {C.C}Multi CIDR {C.G}127.0.0.0/24 104.0.0.0/24{C.C}\n'
              f'{C.Y}➢ {C.C}HOST / IP {C.G}www.google.com OR 1.1.1.1 {C.CC}OR {C.C}Multi CIDR / HOST {C.G}www.google.com www.cloudflare.com 1.1.1.2 1.1.1.0/30{C.C}'
    )

    group.add_argument(
        '-g',
        dest='GENERATE_IP',
        help=f'\n{C.Y}➸ {C.G}CIDR To IP ( Input CIDR {C.G}127.0.0.0/24 ){C.C}'
    )

    group.add_argument(
        '-ip',
        dest='IP',
        help=f'\n{C.Y}➸ {C.G}Host/Domain to IPv4 & IPv6 IP Convert{C.C}'
    )

    group.add_argument(
        '-op',
        dest='OpenPort',
        help=f'\n{C.Y}➸ {C.G}Open Port Check ( Input Host/Domain/IP ){C.C}'
    )

    group.add_argument(
        '-ping',
        help=f'\n{C.Y}➸ {C.G}Ping Check ( Input Host/Domain/IP ){C.C}'
    )

    group.add_argument(
        '-r',
        dest='REVERSE_IP',
        help=f'\n{C.Y}➸ {C.G}Reverse IP LookUp ( Input IP Address ){C.C}'
    )

    group.add_argument(
        '-s',
        dest='SUBFINDER',
        help=f'\n{C.Y}➸ {C.G}SUB DOMAINS FINDER ( Input DOMAIN ){C.C}'
    )

    group.add_argument(
        '-tls',
        dest='TLS',
        help=f'\n{C.Y}➸ {C.G}TLS Connection Check ( Input Your Domain ){C.C}'
    )

    group.add_argument(
        '-txt',
        dest='Splits_TXT',
        help=f'\n{C.Y}➸ {C.G}Split TXT File{C.C}'
    )

    additional = parser.add_argument_group(f'{C.OG}[ * ] Additional Flags{C.C}')

    additional.add_argument(
        '-https',
        action='store_true',
        help=f'\n{C.Y}➸ {C.G}https Mode ( Default is http ){C.C}'
    )

    additional.add_argument(
        '-m',
        dest='methods',
        default='HEAD',
        help=f'\n{C.Y}➸ {C.G}Input Methods ( GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE ), Default is HEAD{C.C}'
    )

    additional.add_argument(
        '-o',
        dest='output',
        help=f'\n{C.Y}➸ {C.G} Disabled, Because currently forwarded to Default [ Default {C.Y}/sdcard/ {C.CC}& {C.Y}$HOME {C.G}]{C.C}'
    )

    additional.add_argument(
        '-p',
        dest='PORT',
        nargs='+',
        default=['80'],
        help=f'\n{C.Y}➸ {C.C}Input Port  {C.OG}➸{C.G} 80 {C.CC}OR {C.C}Multi Port {C.OG}➸{C.G} 80 443 53 ( Default is 80 ){C.C}'
    )

    additional.add_argument(
        '-rr',
        '--RESPONSE',
        action='store_true',
        help=f'\n{C.Y}➸ {C.G}Header Response ( Try with -f Flag ){C.C}'
    )

    additional.add_argument(
        '-t',
        dest='timeout',
        default=3,
        type=int,
        help=f'\n{C.Y}➸ {C.G}Input Timeout ( Default is 3 Second ){C.C}'
    )

    additional.add_argument(
        '-T',
        dest='threads',
        default=64,
        type=int,
        help=f'\n{C.Y}➸ {C.G}Input Threads ( Default is 64 ){C.CC}'
    )

    if not args:
        exit(parser.print_usage())
    
    print(f"\n{C.S}{C.Y} Input Path {C.E} {C.OG}➸❥{C.Y}", *args, f"\n\n{C.CC}{'_' * 61}\n")

    return parser.parse_args()