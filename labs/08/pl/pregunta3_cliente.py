import socket
import time

#socket ip + puerto

SOCK_BUFFER =1024 #el valor maximo 1024 bytes esperando a recibir

if __name__ == '__main__':

    while True:

        #dentro pongo familia y tipo de socket para hace stream de datos
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #afinet usa host y port v4
        #adress family internet, usar ipv4
	    #socks stream , se garantiza que todos los bytes lleguen y en el orden
        server_address = ('localhost',5000) #socket con su respectivo ip y puerto a asociar el cliente

        #print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}") #imprimo la info

        try:
            sock.connect(server_address) #nos conectamos al servidor con su respectivo puerto
            print("Conectado a servidor.")

            while True:
                try:
                    msg= sock.recv(SOCK_BUFFER).decode('utf-8') #espera a recibir datos, maximo 1024 bytes del servidor
                    if msg:
                        print(f"Recibí: {msg}")
                        text_client=input("> ").encode('utf-8')
                        sock.sendall(text_client) #garantiza que todo se envie
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
                    break


       
