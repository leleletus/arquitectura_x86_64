import socket
import pickle

#el cvliuente le manda una lista de notas al server y el server calcula y devuelve
def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("127.0.0.1", 5000))
	print("\x1b[32mConectado a servidor\x1b[0m")

	mis_notas = [10, 20, 15, 11] #el cvliuente le manda una lista de notas al server y el server calcula y devuelve
	serialized_data = pickle.dumps(mis_notas) #pickle recibe cualquier variable y te la transforma a bytes
	sock.sendall(serialized_data) #una vez en bytes lo envia

	data_received = sock.recv(1024) #recibimos la respuesta
	deserialized_data = pickle.loads(data_received) #inversa de dumps de bytes a numeros
	print(f"Promedio: {deserialized_data} ") #imprimimos resultado

	sock.close() #cerramos

if __name__ == "__main__":
	main()