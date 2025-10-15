import os


# ————— OUTPUT —————
def out_dir(File_Name):

    if os.name == 'posix':
        OUTPUT_Path = os.path.join(os.getenv("EXTERNAL_STORAGE"), File_Name)
    else:
        OUTPUT_Path = os.path.join(os.path.expanduser("~"), File_Name)

    return OUTPUT_Path