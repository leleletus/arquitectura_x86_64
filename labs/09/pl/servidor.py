import socket
import time


#socket ip + puerto

SOCK_BUFFER =1024 #el valor maximo 1024 bytes esperando a recibir

if __name__ == '__main__':

    #while True:

        #dentro pongo familia y tipo de socket para hace stream de datos
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #para ser servidor
        #afinet usa host y port v4
        #adress family internet, usar ipv4
	    #socks stream , se garantiza que todos los bytes lleguen y en el orden
        server_address = ('localhost',5010) #socket con su respectivo ip y puerto a asociar el cliente
        server_address2 = ('localhost',5015) #para ser servidor

        sock2.bind(server_address2) #unimos el server address a nuestro server
        sock2.listen(5)  #empezamos a escuchar por conexion de algun cliente 
        print("Server started and listening on port 5015")

        try:
            #primero nos conectamos a nuestro cliente para que no ande recibiendo datos del master antes de establecer conexion
            client_socket2, client_address2 = sock2.accept() # se conecta al cliente
            print(f"Conectado a cliente:  {client_address2}")

            sock.connect(server_address) #nos conectamos al servidor con su respectivo puerto
            print("Conectado a servidor.")


            while True:

                try:
                    dato= sock.recv(SOCK_BUFFER).decode('utf-8') #espera a recibir datos, maximo 1024 bytes del servidor
                    if dato:
                        cant=len(dato)
                        print(f">>HOLA SOY EL SERVIDOR Y HE RECIBIDO DE MASTER {cant} bytes: \"{dato}\"")

                        #enviando al cliente solo los bytes
                        client_socket2.sendall(str(cant).encode('utf-8')) #casteo a string, y lo codigico a utf para enviar
                    else:
                        break
                except KeyboardInterrupt: #cuando finalicemos con el teclado
                    print("Cerrando conexión")
                    sock.close() #cerramos
                    break

                
            


        except ConnectionRefusedError:
                
                try:
                    print(f"\x1b[31mEl servidor no responde\x1b[0m")
                    time.sleep(3) # espera en segundos
                except KeyboardInterrupt: #cuando finalicemos con el teclado
                    print("Cerrando conexión")
                    sock.close() #cerramos
                    #break


       
