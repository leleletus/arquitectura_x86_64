import socket
import time

SOCK_BUFFER = 1024

if __name__=="__main__":

    intentos = 0

    usuario ="roger"
    contraseña = "20172212"

    #Creamos el objeto de socket para el servidor
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Conectandonos al servidor {server_address[0]}, en el puerto {server_address[1]}")
    sock.bind(server_address)

    #Escuchamos conexiones
    sock.listen(5)

    #Empezamos bucle de servidor
    while (intentos <= 3):
        print("Esperando usuario y contraseña")
        
        conn, client_address = sock.accept()
        print(f"Recibi conexion de cliente {client_address}")

        try:
            data = conn.recv(SOCK_BUFFER)
            data_conv = data.decode('utf-8')

            if (data_conv == usuario+"_"+contraseña):
                print(f"{data_conv}") 
                print("Datos validados")
                conn.sendall(data)
            else:
                print("datos incorrectos")
                intentos = intentos + 1
                if (intentos == 4):
                    print("Numero de intentos terminados")
                else:    
                    print(f"Intento {intentos}")

        except Exception as e:
            print(f"Sucedio algo: {e}")
        finally:
            #print("cliente cerro la sesion")
            conn.close()