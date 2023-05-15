import socket
#echo server y echo client es hola mundos de telecos

#puertos
#web 80
#smtp = correo = 25
#socket ip + puerto

SOCK_BUFFER =1024

if __name__ == '__main__':
    #dentro pongo familia y tipo de socket para hace stream de datos
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #afinet usa host y port v4
    server_address = ('localhost',5000)

    print(f"Iniciando servidor en la direccion {server_address[0]} y puerto {server_address[1]}")

    #unimos el server addres a nuestro server
    sock.bind(server_address)

    #esperamos
    sock.listen(5)

    while True:
        print("espeando conexiones...")
        try:
            conn, client_address = sock.accept()
            try:
                print(f"Conexion establecidad con {client_address}")

                while True:
                    data= conn.recv(SOCK_BUFFER) #tipo byte no string
                    if data:
                        print(f"Recibi \"{data}\" de {client_address}")
                        conn.sendall(data)
                    else:
                        break
            except ConnectionResetError:
                print("Conexion cerrada por el ciente abruptamente")
                      
            finally: #no importa que paso antes, al final usa esto
                print("El ciente ha cerrdado la conexion")
                conn.close()
        except KeyboardInterrupt:
            print("el usuario ha terminado el programa")
            break

#packete keepalive ara que se mantenga conectado