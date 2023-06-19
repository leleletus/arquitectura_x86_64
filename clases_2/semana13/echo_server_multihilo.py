import socket
from threading import Thread

SOCK_BUFFER = 1024
num_clientes = 0


def client_handler(conn, client_address):
    global num_clientes
    num_clientes += 1
    print(f"Numero de clientes conectados actualmente: {num_clientes}")
    print(f"Conexion desde {client_address[0]}")
    try:
        while True:
            data = conn.recv(SOCK_BUFFER)
            print(f"Recibi: {data}")
            if data:
                print(f"Enviando: {data}")
                conn.sendall(data)
            else:
                print("No hay mas datos")
                break
    finally:
        print("Cerrando conexion")
        num_clientes -= 1
        conn.close()


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 5001)
    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones...")

        conn, client_address = sock.accept()

        client_thread = Thread(target=client_handler, args=(conn, client_address))
        client_thread.start()



"""se define una función llamada client_handler que toma dos argumentos: conn, que es el objeto de socket para la conexión con el cliente, y client_address, que es la dirección del cliente. Dentro de esta función, se incrementa el contador de clientes y se imprime un mensaje para indicar el número de clientes conectados y la dirección del cliente.

La función luego entra en un bucle while para recibir datos del cliente utilizando el método recv del objeto de socket. Si se reciben datos, se imprimen y luego se envían de vuelta al cliente utilizando el método sendall del objeto de socket. Si no se reciben más datos, el bucle se rompe.

Después de salir del bucle while, el código ejecuta un bloque finally que decrementa el contador de clientes, imprime un mensaje para indicar que se está cerrando la conexión y luego cierra el objeto de socket.

En la parte principal del código, se crea un objeto de socket utilizando socket.socket(socket.AF_INET, socket.SOCK_STREAM) y luego se enlaza a la dirección del servidor especificada. Después de imprimir un mensaje para indicar que el servidor está iniciando, el código llama al método listen del objeto de socket para comenzar a escuchar conexiones.

El código luego entra en un bucle while para aceptar conexiones utilizando el método accept del objeto de socket. Cuando se acepta una conexión, se crea un nuevo hilo utilizando la clase Thread del módulo threading. El hilo se crea con la función client_handler como objetivo y se le pasan el objeto de socket y la dirección del cliente como argumentos. Luego se llama al método start del objeto de hilo para iniciar el hilo.

Este enfoque permite al servidor manejar múltiples conexiones simultáneamente utilizando múltiples hilos. Cada hilo maneja la comunicación con un solo cliente utilizando la función client_handler. Esto permite al servidor recibir y enviar datos a múltiples clientes al mismo tiempo
""" 