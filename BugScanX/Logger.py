from .ANSI_COLORS import ANSI; C = ANSI()
from .MODULES import IMPORT; M = IMPORT()


# ————— 𝐥𝐨𝐠𝐠𝐞𝐫 𝐏𝐫𝐨𝐠𝐫𝐞𝐬𝐬 𝐋𝐢𝐧𝐞 —————
def logger(progress_line):
    columns, _ = M.os.get_terminal_size()

    if len(progress_line) > columns:
        progress_line = progress_line[:columns - 3] + '...'

    M.sys.stdout.write(f'{C.CL}{C.CC}{progress_line}{C.CC}\r')
    M.sys.stdout.flush()