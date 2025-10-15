from ..C_M import CM; C = CM()


# ————— CHECK TLS —————
def CHECK_TLS(HOST):
    
    print(f"\n{C.X}{C.C} Check TLS Connection {C.G}{HOST}\n"
         f"\n{C.INFO} {C.C} Need Internet Connection...\n")

    PORT=443

    try:
        sock = C.socket.create_connection((HOST, PORT))

        context = C.ssl.create_default_context()

        ssl_sock = context.wrap_socket(sock, server_hostname=HOST)

        TLS_Version = ssl_sock.version()

        Cipher = ssl_sock.cipher()

        exit(f"\n{C.X}{C.C} Established Connection: {C.G}{HOST}:{PORT}\n\n"
            f"\n{C.X}{C.C} Cipher: {C.G}{Cipher[0]}\n\n"
            f"\n{C.X}{C.C} Protocol: {C.G}{TLS_Version}\n")

        ssl_sock.close()

    except Exception as e:
        exit(f"\n{C.ERROR} {e} ✘\n")