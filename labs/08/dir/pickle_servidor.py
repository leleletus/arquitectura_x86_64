import socket
import pickle
def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(("127.0.0.1", 5000))

	sock.listen(1)
	client_socket, client_address = sock.accept()
	#print("CLient connected from: ", client_socket, client_address)

	data = client_socket.recv(1024)
	notas = pickle.loads(data) #paso bytes anuymeros
	print("received data: ", notas) #Imprimo las notas recibidas
	promedio = sum(notas) / len(notas)
	client_socket.sendall(pickle.dumps(promedio)) #envio (pero en bytes los numeros)

	client_socket.close() #cierro
	sock.close()

if __name__ == "__main__":
	main()