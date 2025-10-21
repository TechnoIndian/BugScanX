from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()
from ..Logger import logger


# ————— 𝐏𝐎𝐑𝐓 𝐒𝐂𝐀𝐍 —————
def PORT_SCAN(HOST):

    print(f"\n{C.X}{C.C} Scanning {C.G}{HOST} {C.C}for open ports from 1 to 65535...\n")

    threads = []

    Respond_PORT = 0
    
    Total_PORT = 65535

    def check_port(PORT):

        nonlocal Respond_PORT

        try:
            sock = M.socket.socket(M.socket.AF_INET, M.socket.SOCK_STREAM)
            sock.settimeout(1)

            if sock.connect_ex((HOST, PORT)) == 0:
                Respond_PORT += 1
                M.sys.stdout.write(f"\r{' ' * 100}\r{C.S}{C.C} Port {C.E} {C.G}{PORT} ✔\n")

            sock.close()

        except Exception as e:
            exit(f"\n{C.R} {e} ✘\n")

    for PORT in range(1, Total_PORT + 1):
        thread = M.threading.Thread(target=check_port, args=(PORT,))
        thread.start()
        threads.append(thread)

        Scanned_PORT = PORT - 1 + 1

        progress_line = (
            f"- PC - {(Scanned_PORT / Total_PORT) * 100:.2f}% "
            f"- Port - {Scanned_PORT}/{Total_PORT} "
            f"- RS - {Respond_PORT} ✔"
        )

        logger(progress_line)

    for thread in threads:
        thread.join()

    exit(f"\n\n{C.X}{C.C} Scan Complete, Total Open Ports: {C.PN}{Respond_PORT} {C.G}✔\n")