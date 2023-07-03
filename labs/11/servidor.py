import socket
import time
from threading import Thread
import pickle

fila =[]
SOCK_BUFFER = 1024


def leer_dato(): #a sera el thread de leer archivo
    global fila
    #leemos dato
    with open("PartesDeElectrónica.csv", "r") as f: #abrimos en solo lectura ya que solo extraemos datos
        database = f.read() #guardamos en contenido

    fila = database.split("\n")#separamos en filas (cada que encuentre un enter/newline)



def client_handler(client_socket, client_address): #b la funcion del thread para enviar al cliente los datos
    #print(f"Conexion desde {client_address[0]}")
    i=1
    global fila
    try:
        while True:

            if i<len(fila):

                if fila[i]: #asegurarnos de que existe la fila a la que queremos acceder
                    contenido = fila[i].split(";") #separamos para guardar en arreglo
                    serialized_data = pickle.dumps(contenido) #pickle recibe cualquier variable y te la transforma a bytes
                    sock.sendall(serialized_data) #garantiza que todo se envie
                    i+=1 #actualizamos el valor de donde estamos
                    time.sleep(1)  #esperamos 1 segundo de cada envio
            else:
                #print("No hay mas datos")
                break
    except ConnectionResetError:
        print("Cerrando el servidor ...")
    finally:
        #print("Cerrando conexion")
        client_socket.close()


if __name__ == '__main__':


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 5001)
    #print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)

    while True:
        #print("Esperando conexiones...")

        try:
            client_socket, client_address = sock.accept() #se conecta al cliente

            primer_thread  = Thread(target=leer_dato, args=())
            segundo_thread = Thread(target=client_handler, args=(client_socket, client_address))
            primer_thread.start() #me faltan los join que es esperar que acaben al parecer
            segundo_thread.start()

        except KeyboardInterrupt: #en caso ocurrre error al conectarse al cliente
            print("Cerrando el servidor ...")
            break