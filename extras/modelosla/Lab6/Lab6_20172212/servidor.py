import socket
import time
import statistics

SOCK_BUFFER = 1024

nombre_archivo = "lab6_jueves.csv"

if __name__=="__main__":

    
    horas_lista = []
    mes_lista = []
    distancia_lista = []
    pasajeros = 0 #Variable para determinar la cantidad de pasajeros que pueden hacer uso del servicio
    finalizar = 0 #Variable para verificar que el programa terminó

    #Contadores: meses
    enero = 0
    febrero = 0
    marzo = 0
    abril = 0
    mayo = 0
    junio = 0

    #contadores: pasajeros
    pasajero_1 = 0
    pasajero_2 = 0
    pasajero_3 = 0
    pasajero_4 = 0
    pasajero_5 = 0

    f = open (nombre_archivo,'r')
    contenido = f.read()
    f. close()

    data = contenido.split("\n")
    
    #Pregunta C:
    for i in range(350000):
       dato = data[i+1].split(",")
       horas_lista.append(dato[2])

    hora = max(set(horas_lista), key = horas_lista.count) #Usamos la funcion "max" para devolver el valor que mas se repite en la lista
    print(f"La hora del dia con mas solicitudes : {hora}") 

    #Pregunta D:
    for i in range(350000):
       dato = data[i+1].split(",")
       mes_lista.append(dato[2][2])

       if (dato[2][2] == "1"):
           enero = enero + 1

       if dato[2][2] == "2":
           febrero = febrero + 1

       if dato[2][2] == "3":
            marzo = marzo + 1

       if dato[2][2] == "4":
            abril = abril + 1

       if dato[2][2] == "5":
            mayo = mayo + 1

       if dato[2][2] == "6":
            junio = junio + 1

    print(f"Nro de solicitudes en enero :{enero}") 
    print(f"Nro de solicitudes en febrero :{febrero}")
    print(f"Nro de solicitudes en marzo :{marzo}")
    print(f"Nro de solicitudes en abril :{abril}") 
    print(f"Nro de solicitudes en mayo :{mayo}")
    print(f"Nro de solicitudes en junio :{junio}")
    
    mes_mayor = max(set(mes_lista), key = mes_lista.count) #Usamos la funcion "max" para devolver el valor que mas se repite en la lista
    
    #Condicionales para asignar el mes con mayor numero de solicitudes
    if (mes_mayor == "1"):
       mes = "enero"
    if (mes_mayor == "2"):
       mes = "febrero"
    if (mes_mayor == "3"):
       mes = "marzo"
    if (mes_mayor == "4"):
       mes = "abril"
    if (mes_mayor == "5"):
       mes = "mayo"
    if (mes_mayor == "6"):
       mes = "junio"      

    print(f"El mes con mayor numero de solicitudes : {mes}")

    #Pregunta E: 
    for i in range(350000):
       dato = data[i+1].split(",")

       if (dato[4] == "1"):
           pasajero_1 = pasajero_1 + 1

       if (dato[4] == "2"):
           pasajero_2 = pasajero_2 + 1

       if dato[4] == "3":
            pasajero_3 = pasajero_3 + 1

       if dato[4] == "4":
            pasajero_4 = pasajero_4 + 1

       if dato[4] == "5":
            pasajero_5 = pasajero_5 + 1

    print(f"Cantidad de solicitudes para 1 pasajero :{pasajero_1}") 
    print(f"Cantidad de solicitudes para 2 pasajeros :{pasajero_2}")
    print(f"Cantidad de solicitudes para 3 pasajeros :{pasajero_3}")
    print(f"Cantidad de solicitudes para 4 pasajeros :{pasajero_4}") 
    print(f"Cantidad de solicitudes para 5 pasajeros :{pasajero_5}")
    
    #Condicionales para determinar la cantidad de pasajeros que pueden hacer uso del servicio
    if (pasajero_1 != 0):
         pasajeros = 1
          
    if (pasajero_1 != 0) and (pasajero_2 != 0) :
         pasajeros = 2  

    if (pasajero_1 != 0) and (pasajero_2 != 0) and (pasajero_3 != 0)  :
         pasajeros = 3      

    if (pasajero_1 != 0) and (pasajero_2 != 0) and (pasajero_3 != 0) and (pasajero_4 != 0) :
         pasajeros = 4    

    if (pasajero_1 != 0) and (pasajero_2 != 0) and (pasajero_3 != 0) and (pasajero_4 != 0) and (pasajero_5 != 0):
         pasajeros = 5          

    print(f"Cantidad de pasajeros disponibles : {pasajeros}") 

    #Pregunta F:
    for i in range(350000):
       dato = data[i+1].split(",")
       dato_convert = float(dato[5])
       distancia_lista.append(dato_convert)
    
    media = statistics.mean(distancia_lista)
    mediana = statistics.median(distancia_lista) 
    moda = statistics.mode(distancia_lista) 
    desv_estandar = statistics.pstdev(distancia_lista)

    print(f"Media : {media}")  
    print(f"Mediana : {mediana}")
    print(f"Moda : {moda}")
    print(f"Desviacion estandar : {desv_estandar}")

    #Pregunta G:
    #Creamos el objeto de socket para el servidor
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Conectandonos al servidor {server_address[0]}, en el puerto {server_address[1]}")
    sock.bind(server_address)

    #Escuchamos conexiones
    sock.listen(5)      

    #Empezamos bucle de servidor
    while (finalizar == 0):
        print("Esperando palabra clave")
        
        conn, client_address = sock.accept()
        print(f"Recibi conexion de cliente {client_address}")

        try:
            data = conn.recv(SOCK_BUFFER)
            data_conv = data.decode('utf-8')

            if (data_conv == "hora"):
                print(f"{data_conv}:")

                print(f"La hora del dia con mas solicitudes : {hora}") 
                print("                   ") 
                conn.sendall(data)

            if (data_conv == "mes"):
                print(f"{data_conv}:")

                print(f"Nro de solicitudes en enero :{enero}") 
                print(f"Nro de solicitudes en febrero :{febrero}")
                print(f"Nro de solicitudes en marzo :{marzo}")
                print(f"Nro de solicitudes en abril :{abril}") 
                print(f"Nro de solicitudes en mayo :{mayo}")
                print(f"Nro de solicitudes en junio :{junio}") 
                print(f"El mes con mayor numero de solicitudes : {mes}")
                print("                   ") 
                conn.sendall(data)  

            if (data_conv == "pasajeros"):
                print(f"{data_conv}:")

                print(f"Cantidad de solicitudes para 1 pasajero :{pasajero_1}") 
                print(f"Cantidad de solicitudes para 2 pasajeros :{pasajero_2}")
                print(f"Cantidad de solicitudes para 3 pasajeros :{pasajero_3}")
                print(f"Cantidad de solicitudes para 4 pasajeros :{pasajero_4}") 
                print(f"Cantidad de solicitudes para 5 pasajeros :{pasajero_5}")
                print(f"Cantidad de pasajeros disponibles : {pasajeros}") 
                print("                   ") 
                conn.sendall(data)  

            if (data_conv == "distancia"):
                print(f"{data_conv}:")

                print(f"Media : {media}")  
                print(f"Mediana : {mediana}")
                print(f"Moda : {moda}")
                print(f"Desviacion estandar : {desv_estandar}")
                print("                   ") 
                conn.sendall(data)  

            #Pregunta H:
            if (data_conv == "cerrar sesión"):
                print("Sesion terminada")
                finalizar = 1 #Variable para determinar que la sesión terminó
                #Archivo de texto despues de cerrar sesion
                file = open("lab_06_reporte.txt","w")
                file.write("Hora : \n")
                file.write(f"La hora del dia con mas solicitudes : {hora} \n")
                file.write("-------------------------------\n")
                file.write("Mes : \n") 
                file.write(f"Nro de solicitudes en enero :{enero} \n") 
                file.write(f"Nro de solicitudes en febrero :{febrero} \n")
                file.write(f"Nro de solicitudes en marzo :{marzo} \n")
                file.write(f"Nro de solicitudes en abril :{abril} \n") 
                file.write(f"Nro de solicitudes en mayo :{mayo} \n")
                file.write(f"Nro de solicitudes en junio :{junio} \n") 
                file.write(f"El mes con mayor numero de solicitudes : {mes} \n")
                file.write("-------------------------------\n")
                file.write("Pasajeros : \n") 
                file.write(f"Cantidad de solicitudes para 1 pasajero :{pasajero_1}\n") 
                file.write(f"Cantidad de solicitudes para 2 pasajeros :{pasajero_2}\n")
                file.write(f"Cantidad de solicitudes para 3 pasajeros :{pasajero_3}\n")
                file.write(f"Cantidad de solicitudes para 4 pasajeros :{pasajero_4}\n") 
                file.write(f"Cantidad de solicitudes para 5 pasajeros :{pasajero_5}\n")
                file.write(f"Cantidad de pasajeros disponibles : {pasajeros}\n") 
                file.write("-------------------------------\n")
                file.write("Distancia :\n")
                file.write(f"Media : {media}\n")  
                file.write(f"Mediana : {mediana}\n")
                file.write(f"Moda : {moda}\n")
                file.write(f"Desviacion estandar : {desv_estandar}\n")
                file.close()
            else:
                print("Ingresar una palabra clave")

        except Exception as e:
            print(f"Sucedio algo: {e}")
        finally:
            #print("cliente cerro la sesion")
            conn.close()
