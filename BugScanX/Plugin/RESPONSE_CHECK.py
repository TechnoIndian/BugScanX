from ..C_M import CM; C = CM()
from ..OUTPUT import out_dir
from ..Logger import logger


# ————— CHECK RESPONSE —————
def CHECK_RESPONSE(USER_INPUT, isTime):

    print(f"\n{C.X}{C.C} Host/Domain/IP to Header Response...\n")

    def CHECK_RESPONSE_STATUS(URL):

        try:
            RS = C.requests.get(URL, timeout=1)

            return {
                "Host": URL,
                "Response-Status": f"HTTP/{RS.raw.version // 10}.{RS.raw.version % 10} {RS.status_code} {RS.reason}",
                **{key: RS.headers.get(key, "N/A") for key in [
                    "Date", "Connection", "Server", "CF-Cache-Status", "Via", 
                    "CF-RAY", "Report-To", "NEL", "alt-svc"
                ]}
            }

        except C.requests.RequestException as e:
            return None

    entries = []

    for input in USER_INPUT:

        if input.endswith('.txt'):

            with open(input) as file:
                entries.extend([entry.strip() for entry in file if entry.strip()])

        else:
            entries.append(input)


    Output_Path = out_dir("response.txt")

    Total_HOST = len(entries)

    Current_Host = 0

    Start_Time = C.time.time()

    with open(Output_Path, 'w') as outfile:
        with C.ThreadPoolExecutor(max_workers=10) as executor:

            SCAN_HOST = {
                executor.submit(CHECK_RESPONSE_STATUS, f'https://{entry}'): entry
                for entry in entries
            }

            Scanned_HOST = 0

            for HOST in C.as_completed(SCAN_HOST):
                Scanned_HOST += 1
                result = HOST.result()

                if result:
                    Current_Host += 1

                    print(f'\n')

                    for key, value in result.items():
                        print(f"{C.Y}{key} : {C.G}{value}")

                        outfile.write(f"{key} : {value}\n")

                    outfile.write("\n")

                progress_line = (
                    f"{C.R}PC - {C.P}{(Scanned_HOST / Total_HOST) * 100:.2f}% {C.R}"
                    f"- SN -{C.P}{Scanned_HOST}/{C.Y}{Total_HOST} {C.R}"
                    f"- RS - {C.G}{Current_Host} {C.P}<{isTime(C.time.time() - Start_Time)}> {C.R}"
                )

                logger(progress_line)

    exit(f"\n\n{C.X}{C.C} Results Saved {C.OG}︻デ═一 {C.Y}{Output_Path} {C.G}✔\n")