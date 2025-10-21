from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()


# ————— 𝐒𝐩𝐥𝐢𝐭 𝐓𝐗𝐓 —————
def Split_TXT(TXT_FILE):

    try:
        with open(TXT_FILE, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        lines = list(dict.fromkeys(lines))

        print(f"{C.INFO} {C.C}The file {C.G}'{TXT_FILE}' {C.C}has {C.PN}{len(lines)} {C.C}lines.\n")

        INPUT = int(input(f"\n{C.S}{C.P} INPUT {C.E}{C.C} Split the file in equal parts, How many parts do you want to split the file into? : {C.Y}"))

        print()
        size = len(lines) // INPUT + (1 if len(lines) % INPUT else 0)

        base = TXT_FILE.rsplit('.', 1)[0]

        for index in range(0, len(lines), size):

            OUTPUT = M.os.path.join(M.os.path.dirname(TXT_FILE), f"{M.os.path.basename(base)}_{index//size + 1}.txt")

            Wrote_Lines = lines[index:index + size]

            with open(OUTPUT, 'w', encoding='utf-8') as f:
                f.write('\n'.join(Wrote_Lines))

                exit(
                    f"\n{C.S}{C.C} Wrote {C.E} {C.OG}︻デ═一 {C.PN}{len(Wrote_Lines)}\n"
                    f"{C.P}    |\n    ╰{C.CC} OUTPUT ┈{C.OG}➢ {C.Y}{OUTPUT} {C.G}✔\n"
                )

        exit(0)

    except FileNotFoundError:
        exit(f"\n{C.ERROR} The File '{TXT_FILE}' not found.\n")
    except Exception as e:
        exit(f"\n{C.ERROR} {e}\n")