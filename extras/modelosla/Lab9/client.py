import socket
from threading import Thread
import time

SOCK_BUFFER = 1024 

#Pregunta 3:
def conexion_servidor(nombre_archivo,contenido):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Conectandonos al servidor {server_address[0]}, en el puerto {server_address[1]}")
    sock.connect(server_address) 
    data = contenido.split("\n")

    try:
        data[0] = data[0].encode('utf-8')
        print(f"Enviado {data[0]}")
        sock.sendall(data[0])
        for i in range(20):
           time.sleep(1) 
           datos = data[i+1].split(",")
           print(datos)

    finally:
        sock.close()

#Pregunta 4:
def calculo_IMC(nombre_archivo,contenido):

    obesidad = 0
    hombres_sobrepeso = 0
    mujeres_peso_bajo = 0
 
    data = contenido.split("\n")
    
    for i in range(20):
        datos = data[i+1].split(",")
        imc = float(datos[3])/(float(datos[4])*float(datos[4])) 

        if ( 0<imc<18.49):
            clasificacion = "Peso bajo"

        elif ( 18.5<imc<24.9):
            clasificacion = "Normal"  

        elif ( 25<imc<29.9):
            clasificacion = "Sobrepeso" 

        elif ( 30<imc<34.9):
            clasificacion = "Obesidad leve" 

        elif ( 35<imc<39.9):
            clasificacion = "Obesidad media"

        else:
            clasificacion = "Obesidad morbida"   

        if (clasificacion == "Obesidad leve") or (clasificacion == "Obesidad media") or (clasificacion == "Obesidad morbida"):

            obesidad = obesidad + 1

            print(f"-------------Paciente {i+1}-------------")
            print(f"IMC : {imc}") 
            print(F"Clasificacion por IMC: {clasificacion}")    
            print(f"#Pac. con obesidad act.: {obesidad}")
            print(f"#Pac. hombres mayores a 50 años con sobrepeso act.: {hombres_sobrepeso}")
            print(f"#Pac. mujeres entre 18 y 30 años con peso bajo act.: {mujeres_peso_bajo}")
            print("       ")

        elif (clasificacion == "Sobrepeso" ) and (datos[1] == "H") and (int(datos[2]) >= 50):

            hombres_sobrepeso = hombres_sobrepeso + 1

            print(f"-------------Paciente {i+1}-------------")
            print(f"IMC : {imc}") 
            print(F"Clasificacion por IMC: {clasificacion}")    
            print(f"#Pac. con obesidad act.: {obesidad}")
            print(f"#Pac. hombres mayores a 50 años con sobrepeso act.: {hombres_sobrepeso}")
            print(f"#Pac. mujeres entre 18 y 30 años con peso bajo act.: {mujeres_peso_bajo}")
            print("       ")

        elif (clasificacion == "Peso bajo") and (datos[1] == "M") and ( 18 <= int(datos[2]) <= 30 ):

            mujeres_peso_bajo = mujeres_peso_bajo + 1    

            print(f"-------------Paciente {i+1}-------------")
            print(f"IMC : {imc}") 
            print(F"Clasificacion por IMC: {clasificacion}")    
            print(f"#Pac. con obesidad act.: {obesidad}")
            print(f"#Pac. hombres mayores a 50 años con sobrepeso act.: {hombres_sobrepeso}")
            print(f"#Pac. mujeres entre 18 y 30 años con peso bajo act.: {mujeres_peso_bajo}")
            print("       ")

if __name__=="__main__": 

    nombre_archivo = "DatosPacientes.csv"

    f = open (nombre_archivo,'r')
    contenido = f.read()
    f. close()

    t1 = Thread(target=conexion_servidor, args=(nombre_archivo,contenido))    
    t2 = Thread(target=calculo_IMC, args=(nombre_archivo,contenido))

    t1.start() 
    t1.join()

    t2.start()
    t2.join()  