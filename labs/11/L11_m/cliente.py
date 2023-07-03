

'''
Primero, se creará un thread que se encargue de recibir los datos del servidor (servidor.py) correspondientes
a una cadena de caracteres de una fila del archivo PartesDeElectrónica.csv.

Luego, se creará un segundo thread que se encargue de procesar los datos de cada fila recibida. 
Debe calcular lo siguiente:

- Cálculo del costo total (CT = Precio unitario * cantidades)
- Clasificación del componente por costo total:
    - CT < 25: Costo bajo
    - 25 <= CT <= 49.9: Costo regular
    - 50 <= CT <= 74.9: Costo alto
    - CT >= 75: Costo elevado
- Conteo de componentes que tengan costo elevado, conteo de componentes con peso mayor a 100g
y con costo elevado, y conteo de componentes con costo bajo (conteos actualizados por cada componente que se procese).

Asimismo, el segundo thread imprimirá en terminal los resultados de cada fila de la siguiente forma:
------------------Nombre: XXXX------------------
Costo total: XXXX
Clasificación por costo: XXXX
Número de componentes con costo elevado: XXXX
Número de componentes con costo elevado y con peso mayor a 100g: XXXX
Número de componentes con costo bajo: XXXX

solo debe imprimir en terminal si y solo si se tiene un nuevo dato a imprimir
'''

import socket
import time
import threading

SOCK_BUFFER = 1024 #Cantidad máxima de bytes que puede recibir el socket

# Creamos el primer thread que se encargará de recibir los datos del servidor (servidor.py) correspondientes

def thread_rx():
    # Creamos un socket para el cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Nos conectamos al servidor
    client_socket.connect(('localhost', 5080))
    # Usamos variables globales para poder interconectar los threads, en este caso, definiremos
    # la variables correspondiente a un string de datos recibidos a través del socket (linea):
    global linea
    # Recibimos el contenido del cliente, que está enviando la data correspondiente a una línea del archivo
    # PartesDeElectrónica.csv de manera periódica
    while True:
        linea = client_socket.recv(SOCK_BUFFER).decode('utf-8')
        # Si la línea recibida es vacía, significa que el cliente ya terminó de enviar el archivo
        if not linea:
            break

# Creamos el segundo thread que se encargará de procesar los datos de cada fila recibida, y de imprimir los resultados
# de la clasificación como se pide en el enunciado

def thread_processing():
    # Usamos variables globales para poder interconectar los threads, en este caso, definiremos
    # las variables correspondientes a un string de datos recibidos a través del socket (linea), el costo total (costo_total),
    # la clasificación por costo (clasificacion), el conteo de componentes con costo elevado (conteo_elevado),
    # el conteo de componentes con costo elevado y con peso mayor a 100g (conteo_elevado_peso) y el conteo de componentes
    # con costo bajo (conteo_bajo):
    global linea, costo_total, clasificacion, conteo_elevado, conteo_elevado_peso, conteo_bajo
    # Inicializamos las variables
    costo_total = 0
    clasificacion = ''
    conteo_elevado = 0
    conteo_elevado_peso = 0
    conteo_bajo = 0
    # Recibimos el contenido del cliente, que está enviando la data correspondiente a una línea del archivo
    # PartesDeElectrónica.csv de manera periódica
    while True:
        # Si la línea recibida es vacía, significa que el cliente ya terminó de enviar el archivo
        if not linea:
            break
        # Procesamos la línea recibida
        # Separamos los datos de la línea recibida
        datos = linea.split(',')
        # Obtenemos el costo total
        costo_total = int(datos[2]) * int(datos[3])
        # Obtenemos la clasificación por costo
        if costo_total < 25:
            clasificacion = 'Costo bajo'
        elif costo_total <= 49.9:
            clasificacion = 'Costo regular'
        elif costo_total <= 74.9:
            clasificacion = 'Costo alto'
        else:
            clasificacion = 'Costo elevado'
        # Obtenemos el conteo de componentes con costo elevado
        if clasificacion == 'Costo elevado':
            conteo_elevado += 1
        # Obtenemos el conteo de componentes con costo elevado y con peso mayor a 100g
        if clasificacion == 'Costo elevado' and int(datos[4]) > 100:
            conteo_elevado_peso += 1
        # Obtenemos el conteo de componentes con costo bajo
        if clasificacion == 'Costo bajo':
            conteo_bajo += 1
        # Imprimimos los resultados
        print('------------------Nombre: ' + datos[0] + '------------------')
        print('Costo total: ' + str(costo_total))
        print(' Clasificación por costo: ' + clasificacion)
        print(' Número de componentes con costo elevado: ' + str(conteo_elevado))
        print(' Número de componentes con costo elevado y con peso mayor a 100g: ' + str(conteo_elevado_peso))
        print(' Número de componentes con costo bajo: ' + str(conteo_bajo))


def main():
    # Creamos los threads
    thread_receiver = threading.Thread(target=thread_rx)
    thread_classifier = threading.Thread(target=thread_processing)
    # Iniciamos los threads y los sincronizamos con el thread principal
    thread_receiver.start()
    thread_receiver.join()
    thread_classifier.start()
    thread_classifier.join()

if __name__ == '__main__':
    # La condición if __name__ == '__main__' asegura que el código dentro de este bloque solo se ejecute si el archivo
    # es ejecutado directamente por el intérprete, no si es importado como módulo.
    main()