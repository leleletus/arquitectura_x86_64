
'''
Cree un primer thread en el archivo servidor.py el cual, luego de establecer conexión con un cliente, leerá el 
archivo PartesDeElectrónica.csv
La cabecera de este archivo es: [ID, Nombre, Número de parte, Cantidades, Peso, Costo unitario]
Este archivo contiene los datos de varios componentes electrónicos que se quieren comprar en un proveedor de China.

El segundo Thread del servidor, en intervalos de 1 segundo, le enviará al cliente la cadena de caracteres de una fila 
(datos de un componente electrónico), así consecutivamente hasta completar de leer el archivo.
'''

import socket
import time
import threading

SOCK_BUFFER = 1024 #Cantidad máxima de bytes que puede recibir el socket

# Creamos el primer thread que se encargará de establecer conexión con un cliente
# y de leer el archivo PartesDeElectrónica.csv:


 # Necesitamos de una bandera para indicar al thread 2 que ya se tiene contenido recibido, esta debe
# ser una variable global, y la inicializamos en False
contenido_recibido = False

def thread1():
    global contenido_recibido
    # Creamos un socket para el servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Asociamos el socket a la dirección IP y puerto del servidor
    server_socket.bind(('localhost', 5080))
    # Ponemos al servidor a escuchar conexiones entrantes
    server_socket.listen(1)
    # Usamos variables globales para poder interconectar los threads, en este caso, definiremos
    # las variables de la conexión entrante del cliente (conn y client_address) y el contenido:
    global conn, client_address, contenido
    # Aceptamos la conexión entrante
    conn, client_address = server_socket.accept()
    # Abrimos el archivo PartesDeElectrónica.csv, leemos su contenido y lo guardamos en una variable
    # y además cambiamos el valor de la bandera a True para indicar que ya se recibió el contenido del archivo
    with open('PartesDeElectrónica.csv', 'r') as file:
        contenido = file.readlines()
        contenido_recibido = True

# Creamos el segundo thread que se encargará de enviarle al cliente el contenido del archivo en intervalos periódicos de 1 segundo
# hasta que se acabe el contenido del archivo, que es cuando se cerrará la conexión:

def thread2():
    # Usamos variables globales para poder interconectar los threads, en este caso, definiremos
    # las variables de la conexión entrante del cliente (conn y client_address) y el contenido:
    global conn, client_address, contenido, contenido_recibido

    if not contenido_recibido:
        time.sleep(1) # Esperamos 1 segundo para que el thread 1 reciba el contenido del archivo
    else :
        # Enviamos el contenido del archivo al cliente en intervalos de 1 segundo
        for i in contenido:
            conn.sendall(i.encode('utf-8'))
            time.sleep(1)
        # Cerramos la conexión
        conn.close()
    

def main():
    # Creamos los threads
    thread_content = threading.Thread(target=thread1) # Thread en el que establecemos conexión con el cliente
    # y leemos el archivo que deseamos procesar
    thread_send = threading.Thread(target=thread2) # Thread en el cual le enviamos al cliente el contenido del archivo
    # línea por línea en intervalos de 1 segundo hasta que este se acabe
    # Iniciamos los threads y los sincronizamos con el thread principal
    thread_content.start() #inicia nuevo hilo
    thread_content.join()#espera a que termine
    thread_send.start()
    thread_send.join()


if __name__ == '__main__':
    # La condición if __name__ == '__main__' asegura que el código dentro de este bloque solo se ejecute si el archivo
    # es ejecutado directamente por el intérprete, no si es importado como módulo.
    main()