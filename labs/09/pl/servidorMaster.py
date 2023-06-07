import socket
import time
import pickle

#socket ip + puerto
SOCK_BUFFER =1024 #el valor maximo 1024 bytes esperando a recibir

if __name__ == '__main__':
    #dentro pongo familia y tipo de socket para hace stream de datos
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #afinet usa host y port v4
    #adress family internet, usar ipv4
	#socks stream , se garantiza que todos los bytes lleguen y en el orden
    server_address = ('localhost',5010) #socket con su respectivo ip y puerto a asociar el servidor

    #print(f"Iniciando servidor en la direccion {server_address[0]} y puerto {server_address[1]}") #imprimo la info

    sock.bind(server_address) #unimos el server addresss a nuestro server

    sock.listen(5)  #empezamos a escuchar por conexion de algun cliente 

    print("Server started and listening on port 5010")

    with open("pregunta1.txt", "r") as f: #abrimos en solo lectura ya que solo extraemos datos
        contenido = f.read() #guardamos en contenido

    filas = contenido.split("\n")#separamos en filas (cada que encuentre un enter/newline)
    i=0 #para saber en que fila se quedo el envio 


    while True: #para que acepte reconexiones
        
        try:
            client_socket, client_address = sock.accept() # se conecta al cliente
            try:
                print(f"Conectado a cliente:  {client_address}")

                while True:
                    
                    if i<len(filas):
                        dato=filas[i].encode('utf-8')
                        try:
                            client_socket.sendall(dato) #se lo enviamos al cliente
                            time.sleep(1) # espera en segundo
                        except BrokenPipeError: #en caso se desconecto el cliente salimos del while para reconectarse
                            i-=1 #en mi codigo se salteaba una linea asi que al restarle se arregla
                            break
                        i+=1 #cambiamos a la siguiente fila

                    else:
                        i=0 # enviamos todo y volvemos a empezar

            except ConnectionResetError:
                print("Cerrando el servidor ...")
                      
            finally: #no importa que paso antes, al final usa esto
                #print("El ciente ha cerrado la conexion")
                client_socket.close()
        except KeyboardInterrupt:
            print("Cerrando el servidor ...")
            break


#packete keepalive hara que se mantenga conectado