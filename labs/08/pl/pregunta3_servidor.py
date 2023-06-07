import socket

def ingresar_dato(mensaje: str) -> str: #string a string
    data = input(mensaje) #lo guarda mediante imput
    return data #returnoa el string


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

    sock.bind(server_address) #unimos el server addresss a nuestro server

    sock.listen(5)  #empezamos a escuchar por conexion de algun cliente 
    print("Server started and listening on port 5000")

    #print("Esperando conexiones...") #para saber que aun no se conecta nadie

    while True:
        
        try:
            client_socket, client_address = sock.accept()
            try:
                print(f"Conectado a cliente:  {client_address}")

                while True:
                    
                    text_serv=input("> ").encode('utf-8') #para que ingrese texto primero y encode para enviar
                    client_socket.sendall(text_serv) #se lo enviamos al cliente


                    data= client_socket.recv(SOCK_BUFFER) #espera a recibir del cliente undato tipo caracter, no string de 1024 bytes
                    if data:
                        print(f"Recibido: {data.decode('utf-8')}") #mostramos lo recibido y de quien
                    else:
                        break
            except ConnectionResetError:
                print("Cerrando el servidor ...")
                client_socket.close()
                      
            finally: #no importa que paso antes, al final usa esto
                #print("El ciente ha cerrado la conexion")
                client_socket.close()
        except KeyboardInterrupt:
            print("Cerrando el servidor ...")
            break

#packete keepalive hara que se mantenga conectado