# ————— 𝐈𝐌𝐏𝐎𝐑𝐓 𝐌𝐎𝐃𝐔𝐋𝐄𝐒 —————

class IMPORT:
    def __init__(self):

        # ————— 𝐋𝐢𝐛𝐫𝐚𝐫𝐢𝐞𝐬 𝐈𝐦𝐩𝐨𝐫𝐭 —————
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

        # ————— 𝐄𝐱𝐭𝐫𝐚 𝐋𝐢𝐛𝐫𝐚𝐫𝐢𝐞𝐬 —————
        self.ping = __import__('ping3').ping
        self.tabulate = __import__('tabulate').tabulate
        self.datetime = __import__('datetime').datetime
        self.BeautifulSoup = __import__('bs4').BeautifulSoup
        self.as_completed = __import__('concurrent.futures').futures.as_completed
        self.ThreadPoolExecutor = __import__('concurrent.futures').futures.ThreadPoolExecutor