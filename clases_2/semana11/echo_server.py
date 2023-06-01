import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':
    # Creamos el objeto de socket para el servidor
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 5001)
    print(f"Iniciando el servidor en la direccion {server_address[0]} y puerto {server_address[1]}")
    sock.bind(server_address)

    # Escuchamos conexiones
    sock.listen(1)

    # Empezamos bucle de servidor
    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        try:
            print(f"Conexion establecida con {client_address}")

            while True:
                data = conn.recv(SOCK_BUFFER)
                if data:
                    # data_conv = data.decode('utf-8')
                    print(f"Recibi {data} de {client_address}")
                    conn.sendall(data)
                else:
                    break
        except ConnectionResetError:
            print("Conexion cerrada por el cliente abruptamente")
        finally:
            print("El cliente ha cerrado la conexion")
            conn.close()
