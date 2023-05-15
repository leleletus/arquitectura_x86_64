import socket
import time

SOCK_BUFFER = 1024

if __name__=="__main__":
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Conectandonos al servidor {server_address[0]}, en el puerto {server_address[1]}")
    sock.connect(server_address)

    try:
        msg = f"roger_20172213"
        msg = msg.encode('utf-8')
        print(f"Enviado {msg}")
        sock.sendall(msg)
        amnt_recvd = 0
        amnt_expected = len(msg)
        msg_total_bytes = b''

    finally:
        print("Cerrando socket")
        sock.close()

        #python3 pregunta1_server.py
        #python3 pregunta1_client.py