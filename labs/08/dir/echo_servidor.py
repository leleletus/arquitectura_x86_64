import socket

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(("127.0.0.1", 5000)) #ahora uso bind no conect, asociarme a un puerto en particular

	sock.listen(1) #escuchar un solo cliente
	
	client_socket, client_address = sock.accept() #esperamos conexion de algun cliente (no avanza hasta)
	print("CLient connected from: ", client_socket, client_address) #una vez conectados

	data = client_socket.recv(1024) #usamos puro client_socket
	print("received data: ", data.decode())
	client_socket.sendall(data)

	client_socket.close()
	sock.close()

if __name__ == "__main__":
	main()