from ..C_M import CM; C = CM()


# ————— Split TXT —————
def Split_TXT(TXT_FILE):

    try:
        with open(TXT_FILE, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        lines = list(dict.fromkeys(lines))

        print(f"{C.INFO} {C.C}The file {C.G}'{TXT_FILE}' {C.C}has {C.PN}{len(lines)} {C.C}lines.\n")

        INPUT = int(input(f"\n{C.S}{C.P} INPUT {C.E}{C.C} Split the file in equal parts, How many parts do you want to split the file into? : {C.Y}"))

        size = len(lines) // INPUT + (1 if len(lines) % INPUT else 0)

        base = TXT_FILE.rsplit('.', 1)[0]

        for index in range(0, len(lines), size):

            OUTPUT = C.os.path.join(C.os.path.dirname(TXT_FILE), f"{C.os.path.basename(base)}_{index//size + 1}.txt")

            Wrote_Lines = lines[index:index + size]

            print(f"\n{C.X} {C.C} Wrote {C.PN}{len(Wrote_Lines)} {C.C}lines to {C.Y}{OUTPUT} {C.G}✔\n")

            with open(OUTPUT, 'w', encoding='utf-8') as f:
                f.write('\n'.join(Wrote_Lines))

        exit(0)

    except FileNotFoundError:
        exit(f"\n{C.ERROR} The File '{TXT_FILE}' not found.\n")
    except Exception as e:
        exit(f"\n{C.ERROR} {e}\n")