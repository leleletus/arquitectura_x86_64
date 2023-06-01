
import socket
#echo server y echo client es hola mundos de telecos

#puertos
#web 80
#smtp = correo = 25
#socket ip + puerto

SOCK_BUFFER =1024

if __name__ == '__main__':
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#adress family internet, usar ipv4
	#socks stream , se garantiza que todos los bytes lleguen y en el orden
	sock.connect(("127.0.0.1", 5000)) #nos conectamos al servidor y su puerto
	#127 al interior de la pc
	print("\x1b[32mConectado a servidor\x1b[0m") #agregarle color al texto 32 verde 31 rojo

	message = "Hello server" #mensaje a enviar
	sock.sendall(message.encode()) #garantiza sendall que envie todos los bytes

	data_received = sock.recv(1024) #espera a recibir datos, amximo 1024 bytes del servidor
	print(f"Received: {data_received.decode()} ") #imprimo lo recibido, decode decodigico

	sock.close() #

