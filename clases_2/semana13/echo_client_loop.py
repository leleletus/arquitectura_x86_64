import socket
import time

#simple ciente loop

SOCK_BUFFER = 4

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)
    print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}")

    sock.connect(server_address )
    try:
        for i in range(10):
            msg = f"Hola Mundo {i+1}!"
            msg = msg.encode('utf-8')
            print(f"logitud del mensaje: {len(msg)} bytes")
            sock.sendall(msg)
            data = sock.recv(SOCK_BUFFER)
            print(f"Recibido: {data.decode('utf-8')}")
            time.sleep(2)
    finally:
        print("Cerrando socket")
        sock.close()





"""Dentro de un bloque try, el código ejecuta un bucle for para enviar 10 mensajes al servidor. Cada mensaje es una cadena que contiene el texto “Hola Mundo” seguido de un número. La cadena se codifica en bytes utilizando el método encode y luego se envía al servidor utilizando el método sendall del objeto de socket.

Después de enviar cada mensaje, el código llama al método recv del objeto de socket para recibir datos del servidor. El tamaño del búfer para recibir datos se especifica utilizando la constante SOCK_BUFFER. Los datos recibidos se decodifican utilizando el método decode y luego se imprimen.

Después de enviar todos los mensajes y recibir todas las respuestas, el código sale del bucle for y ejecuta el bloque finally. Este bloque imprime un mensaje para indicar que se está cerrando el socket y luego llama al método close del objeto de socket para cerrar la conexión"""