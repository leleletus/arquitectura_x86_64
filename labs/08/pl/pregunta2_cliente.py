import socket
import pickle
import random
import numpy as np

#socket ip + puerto

SOCK_BUFFER =1024 #el valor maximo 1024 bytes esperando a recibir

if __name__ == '__main__':


        #dentro pongo familia y tipo de socket para hace stream de datos
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #afinet usa host y port v4
        #adress family internet, usar ipv4
	    #socks stream , se garantiza que todos los bytes lleguen y en el orden
        server_address = ('localhost',5000) #socket con su respectivo ip y puerto a asociar el cliente

        #print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}") #imprimo la info

        sock.connect(server_address) #nos conectamos al servidor con su respectivo puerto

        try:
            
            #geeneramos mariz 1
            limit=9 #escogemos el maximo valor que puede tener un numero de nuestra matriz

            matriz1= np.array([[random.randint(0, limit),random.randint(0, limit)],
                   [random.randint(0, limit),random.randint(0, limit)]])
            
            matriz2= np.array([[random.randint(0, limit),random.randint(0, limit)],
                   [random.randint(0, limit),random.randint(0, limit)]])


            dato= np.concatenate((matriz1, matriz2))

            serialized_data = pickle.dumps(dato) #pickle recibe cualquier variable y te la transforma a bytes
            sock.sendall(serialized_data) #garantiza que todo se envie


            data_received= sock.recv(SOCK_BUFFER) #espera a recibir datos, maximo 1024 bytes del servidor
            deserialized_data = pickle.loads(data_received) #inversa de dumps de bytes a numeros

            print("Producto de Matrices:")
            print(deserialized_data)  #imprimo lo recibido, decode decodifico

        finally:
            #print("Cerrando socket")
            sock.close() #cerramos


       
