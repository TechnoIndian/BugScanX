from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()
from ..OUTPUT import out_dir
from ..Logger import logger


# ————— 𝐂𝐇𝐄𝐂𝐊 𝐑𝐄𝐒𝐏𝐎𝐍𝐒𝐄 —————
def CHECK_RESPONSE(HOSTS, isTime):

    print(f"\n{C.X}{C.C} CIDR / IP / Host ( Domain & SubDomain ) Header Response...\n")

    def CHECK_RESPONSE_STATUS(URL):

        try:
            RS = M.requests.get(URL, timeout=3)

            return {
                "Host": URL,
                "Response-Status": f"HTTP/{RS.raw.version // 10}.{RS.raw.version % 10} {RS.status_code} {RS.reason}",
                **{key: RS.headers.get(key, "N/A") for key in [
                    "Date", "Connection", "Server", "CF-Cache-Status", "Via", 
                    "CF-RAY", "Report-To", "NEL", "alt-svc"
                ]}
            }

        except M.requests.RequestException as e:
            return None

    Output_Path = out_dir("response.txt")
    
    Total_HOST = len(HOSTS)

    Scanned_HOST = Respond_HOST = 0

    Start_Time = M.time.time()

    with open(Output_Path, 'w') as file:
        
        with M.ThreadPoolExecutor(max_workers=64) as executor:

            isRequest = {}

            for HOST in HOSTS:
                Request = executor.submit(CHECK_RESPONSE_STATUS, f'https://{HOST}')
                isRequest[Request] = HOST

            for isHOST in M.as_completed(isRequest):
                Scanned_HOST += 1
                CURRENT_HOST = isRequest[isHOST]
                result = isHOST.result()

                if result:
                    Respond_HOST += 1
                    
                    print(f"{C.CL}{C.CC}{'_' * 61}\n")

                    for key, value in result.items():
                        print(f"\r{C.CL}{C.Y}{key} : {C.G}{value}")

                        file.write(f"{key} : {value}\n")

                    file.write("\n")

                progress_line = (
                    f"- PC - {(Scanned_HOST / Total_HOST) * 100:.2f}% "
                    f"- SN -{Scanned_HOST}/{Total_HOST} "
                    f"- RS - {Respond_HOST} <{isTime(M.time.time() - Start_Time)}> "
                    f"- {CURRENT_HOST}"
                )

                logger(progress_line)

    exit(
        f"{C.CC}{'_' * 61}\n\n"
        f"\n{C.S}{C.C} OUTPUT {C.E} {C.OG}︻デ═一 {C.Y}{Output_Path} {C.G}✔\n"
    )