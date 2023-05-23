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
    print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}")


    sock.connect(server_address)

    try:
        data = "Hola mundo!".encode('utf-8') #este string lo pasamos a caracteres
        sock.sendall(data)

        msg= sock.recv(SOCK_BUFFER)
        print(f"Recibi {msg.decode('utf-8')}")

    finally:
        print("Cerrando socket")
        sock.close()