# ————— Colour Module —————
class CM:
    def __init__(self):

        # ————— Libraries Import —————
        self.re = __import__('re')
        self.os = __import__('os')
        self.ssl = __import__('ssl')
        self.sys = __import__('sys')
        self.zlib = __import__('zlib')
        self.time = __import__('time')
        self.zipfile = __import__('zipfile')
        self.socket = __import__('socket')
        self.base64 = __import__('base64')
        self.requests = __import__('requests')
        self.argparse = __import__('argparse')
        self.threading = __import__('threading')
        self.ipaddress = __import__('ipaddress')
        self.subprocess = __import__('subprocess')

        # ————— Extra Libraries —————
        self.ping = __import__('ping3').ping
        self.tabulate = __import__('tabulate').tabulate
        self.datetime = __import__('datetime').datetime
        self.BeautifulSoup = __import__('bs4').BeautifulSoup
        self.as_completed = __import__('concurrent.futures').futures.as_completed
        self.ThreadPoolExecutor = __import__('concurrent.futures').futures.ThreadPoolExecutor


        # =====🔸ANSI COLORS🔸=====

        self.R  = '\033[0m' # RESET
        self.RD = '\033[1m\033[91m' # RED
        self.Y  = '\033[1m\033[33m' # YELLOW
        self.BY = '\033[1m\033[93m' # BRIGHT YELLOW
        self.C  = '\033[1m\033[36m' # CYAN
        self.BC = '\033[1m\033[96m' # BRIGHT CYAN
        self.G  = '\033[1m\033[32m' # GREEN
        self.BG = '\033[1m\033[92m' # BRIGHT GREEN
        self.GR = '\033[1m\033[90m' # GRAY
        self.B  = '\033[1m\033[34m' # BLUE
        self.BB = '\033[1m\033[94m' # BRIGHT BLUE
        self.P  = '\033[1m\033[35m' # PURPLE
        self.BP = '\033[1m\033[95m' # BRIGHT PURPLE
        self.PN = '\033[1m\033[38;5;213m' # PINK
        self.OG = '\033[1m\033[38;5;202m' # ORANGE

        # =====🔹TAG🔹=====

        self.S = f'{self.BB}['
        self.E = f'{self.BB}]'
        self.X = f'{self.BB}[ {self.P}* {self.BB}]'
        self.INFO = f'{self.BB}[ {self.Y}INFO {self.BB}]'
        self.ERROR = f'{self.BB}[ {self.RD}Error ! {self.BB}]{self.RD}'