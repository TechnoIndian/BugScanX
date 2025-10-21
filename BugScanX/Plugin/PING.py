from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()


# ————— 𝐏𝐈𝐍𝐆 𝐓𝐞𝐬𝐭 —————
def PING(host):
    
    print(f"\n{C.X}{C.C} Ping Checker\n"
         f"\n{C.INFO}{C.C} Need Internet Connection...{C.G}\n")

    param = '-n' if M.os.name == 'nt' else '-c'

    cmd = f'ping {param} 5 {host}'

    if M.subprocess.call(cmd, shell=True) == 0:
        exit(f"\n{C.S}{C.P} Status {C.E}{C.G} {host}{C.C} is reachable. {C.G}✔\n")
    else:
        exit(f"\n{C.S}{C.P} Status {C.E}{C.G} {host}{C.R} is not reachable. ✘\n"
            f"\n{C.INFO} {C.C} Need Internet Connection...\n")