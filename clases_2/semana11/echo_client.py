import socket
import time
import random


SOCK_BUFFER = 4

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)
    print(f"Conectando al servidor en {server_address[0]} y puerto {server_address[1]}")

    sock.connect(server_address )
    try:
        msg = "Hola Mundo!"
        msg = msg.encode('utf-8')
        print(f"logitud del mensaje: {len(msg)} bytes")
        sock.sendall(msg)
        data = sock.recv(SOCK_BUFFER)
        print(f"Recibido: {data.decode('utf-8')}")
    finally:
        print("Cerrando socket")
        sock.close()