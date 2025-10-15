from ..C_M import CM; C = CM()


# ————— PING Test —————
def PING(host):
    
    print(f"\n{C.X}{C.C} Ping Checker\n"
         f"\n{C.INFO}{C.C} Need Internet Connection...{C.G}\n")

    param = '-n' if C.os.name == 'nt' else '-c'

    cmd = f'ping {param} 5 {host}'

    if C.subprocess.call(cmd, shell=True) == 0:
        exit(f"\n{C.S}{C.P} Status {C.E}{C.G} {host}{C.C} is reachable. {C.G}✔\n")
    else:
        exit(f"\n{C.S}{C.P} Status {C.E}{C.G} {host}{C.RD} is not reachable. ✘\n"
            f"\n{C.INFO} {C.C} Need Internet Connection...\n")