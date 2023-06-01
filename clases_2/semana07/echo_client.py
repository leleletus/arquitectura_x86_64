import socket

#socket ip + puerto

SOCK_BUFFER =1024 #el valor maximo 1024 bytes esperando a recibir

if __name__ == '__main__':
    #dentro pongo familia y tipo de socket para hace stream de datos
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #afinet usa host y port v4
    #adress family internet, usar ipv4
	#socks stream , se garantiza que todos los bytes lleguen y en el orden
    server_address = ('localhost',5000) #socket con su respectivo ip y puerto a asociar el cliente

    print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}") #imprimo la info

    sock.connect(server_address) #nos conectamos al servidor con su respectivo puerto

    try:
        data = "Hola mundo!".encode('utf-8') #este string lo pasamos a caracteres (mensaje a enviar)
        sock.sendall(data) #garantiza que todo se envie

        msg= sock.recv(SOCK_BUFFER) #espera a recibir datos, maximo 1024 bytes del servidor
        print(f"Recibi {msg.decode('utf-8')}")  #imprimo lo recibido, decode decodifico

    finally:
        print("Cerrando socket")
        sock.close() #cerramos