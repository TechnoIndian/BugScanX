from ..C_M import CM; C = CM()
from ..Logger import logger
from ..OUTPUT import out_dir

C_Line = f"{C.R}{'_' * 61}"


# ————— Bug Scaner —————
def BugScaner(HOSTS, isIP, isIP_Add, isCIDR, isROW, isRequest, isTime, isTimeOut, PORTS=False, Output_Path=False, Threads=False, isHTTPS=False, Method='HEAD'):

    print(isROW('IP Address', 'Status', 'Server', 'Port', 'Host', C.R))

    print('--------------- -------  ----------------      ------  ------------------------------')

    Total_HOST = len(HOSTS) * len(PORTS)

    Scanned_HOST = Respond_HOST = 0

    Start_Time = C.time.time()

    isCloudFlare, isCloudFront = {}, {}

    Other_Responds = []

    CF_Path = out_dir("CF.txt")

    Output_Path = out_dir("other_respond.txt")

    with C.ThreadPoolExecutor(max_workers=Threads) as executor:

        futures = {
            executor.submit(isRequest, HOST, PORT, isTimeOut, Method, isHTTPS): (HOST, PORT)
            for HOST in HOSTS
            for PORT in PORTS
        }

        for future in C.as_completed(futures):
            Scanned_HOST += 1
            RESULT = future.result()

            if RESULT:
                Respond_HOST += 1

                IP, STATUS, SERVER, PORT, HOST, LOCATION = RESULT

                print(isROW(IP[0], STATUS, SERVER, PORT, HOST, LOCATION))
                
                if 'cloudflare' in SERVER:
                    isCloudFlare.setdefault(HOST, []).extend(IP)
                elif 'CloudFront' in SERVER:
                    isCloudFront.setdefault(HOST, []).extend(IP)
                else:
                    Other_Responds.append((IP[0], STATUS, SERVER, HOST))

            progress_line = (
                f"{C.R}PC - {C.P}{(Scanned_HOST / Total_HOST) * 100:.2f}% {C.R}"
                f"- SN -{C.P}{Scanned_HOST}/{C.Y}{Total_HOST} {C.R}"
                f"- RS - {C.G}{Respond_HOST} {C.P}<{isTime(C.time.time() - Start_Time)}> {C.R}"
                f"- {C.B}{futures[future][0]}{C.R}"
            )

            logger(progress_line)

    if Other_Responds:
        print(f'\n\n{C.X}{C.C} Other Respond HOSTS Saved: {C.G}︻デ═一 {C.Y}{Output_Path} {C.G}✔')
        
    print(f'\n{C_Line}\n')

    with open(Output_Path, 'w') as file:
        for Response in Other_Responds:
            IP, STATUS, SERVER, HOST = Response
            plain_STATUS = STATUS.replace(C.P, '').strip()

            if isIP_Add(HOST):
                file.write(f"{IP} | {SERVER} | {plain_STATUS}\n")
            else:
                file.write(f"{IP} | {SERVER} | {plain_STATUS} | {HOST}\n")

    def OUTPUT_LOGS(HOST_IP, Server_Name, Color):

        if HOST_IP:
            print(f"\n{Color}# {Server_Name}\n")

            Output_Logs = [f"\n# {Server_Name}\n"]

            for HOST, IPs in HOST_IP.items():
                if not isCIDR and not isIP_Add(HOST):
                    print(f"{HOST}")

                    Output_Logs.append(HOST)
                
            if not isCIDR:
                Output_Logs.extend('\r')

                Total_IP = sorted(
                    set(
                        IP for IPs in HOST_IP.values()
                        for IP in IPs
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

    if isCloudFlare or isCloudFront:
        print(f"\n{C.X}{C.C} CF Result Saved  {C.G}︻デ═一 {C.Y}{CF_Path}\n"
             f"\n{C_Line}\n")