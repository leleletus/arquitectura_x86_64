import socket
from threading import Thread
import time

import socket
from threading import Thread
import time

SOCK_BUFFER = 1024

#Pregunta 1:
def conexion_cliente(conn, client_address):

    nombre_archivo = "DatosPacientes.csv"

    f = open (nombre_archivo,'r')
    contenido = f.read()
    f. close()

    try:
        print(f"Conexion de {client_address}")

        while True:
            data = conn.recv(SOCK_BUFFER)
            if data:
                print(f"Recibi {data}")
                #conn.sendall(data)
            else:
                break
    except Exception as e:
        print(f"Excepcion {e}")
    finally:
        conn.close()

#Pregunta 2:
def datos_paciente(nombre_archivo):

    f = open (nombre_archivo,'r')
    contenido = f.read()
    f. close()

    data = contenido.split("\n")
    for a in range(20):
       time.sleep(1)
       datos = data[a+1].split(",")
       print(datos)

if __name__=="__main__":

    nombre_archivo = "DatosPacientes.csv"

    sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 5000)
    print(f"Iniciando servidor en {server_address[0]}, en puerto {server_address[1]}")
    sock.bind(server_address)

    sock.listen(5)


    while True:
        print("Esperando conexiones")

        conn, client_address = sock.accept()
        
        t1 = Thread(target=datos_paciente, args=(nombre_archivo,))
        t1.start()

        t2 = Thread(target=conexion_cliente, args=(conn, server_address))
        t2.start()

        t1.join()
        t2.join()