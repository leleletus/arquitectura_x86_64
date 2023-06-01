import socket
import pickle
import numpy as np

#socket ip + puerto

SOCK_BUFFER =1024 #el valor maximo 1024 bytes esperando a recibir

if __name__ == '__main__':
    #dentro pongo familia y tipo de socket para hace stream de datos
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #afinet usa host y port v4
    #adress family internet, usar ipv4
	#socks stream , se garantiza que todos los bytes lleguen y en el orden
    server_address = ('localhost',5000) #socket con su respectivo ip y puerto a asociar el servidor

    #print(f"Iniciando servidor en la direccion {server_address[0]} y puerto {server_address[1]}") #imprimo la info

    sock.bind(server_address) #unimos el server addres a nuestro server

    sock.listen(5)  #empezamos a escuchar por conexion de algun cliente 

    print("Esperando conexiones...")

    while True:
        
        try:
            client_socket, client_address = sock.accept()
            try:
                print(f"Conexion entrante de  {client_address}")

                while True:
                    data= client_socket.recv(SOCK_BUFFER) #recibimos del cliente dato tipo caracter, no string de 1024 bytes
                    if data:
                        #print(f"Recibi \"{data.decode('utf-8')}\" de {client_address}") #mostramos lo recibido y de quien
                        matrices_unidas = pickle.loads(data) #paso bytes anuymeros
                        matriz1,matriz2 = np.split(matrices_unidas, [2])
                        resultado= np.dot(matriz1,matriz2) #calculamos lo pedido
                        
                        serialized_data = pickle.dumps(resultado)
                        client_socket.sendall(serialized_data) #se lo enviamos al cliente

                    else:
                        break
            except ConnectionResetError:
                print("Cerrando el servidor ...")
                      
            finally: #no importa que paso antes, al final usa esto
                #print("El ciente ha cerrado la conexion")
                client_socket.close()
        except KeyboardInterrupt:
            print("Cerrando el servidor ...")
            break

#packete keepalive hara que se mantenga conectado