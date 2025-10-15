from .C_M import CM; C = CM()


# ————— logger Progress Line —————
def logger(progress_line):

    try:
        columns, _ = C.os.get_terminal_size()
    except OSError:
        columns = 80

    Fix_Line = C.re.sub(r'\033\[[0-9;]*m', '', progress_line)

    if len(Fix_Line) > columns:
        progress_line = progress_line[:columns - 3] + '...'

    C.sys.stdout.write(f'{progress_line}\r')
    C.sys.stdout.flush()