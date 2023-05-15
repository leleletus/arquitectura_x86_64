import socket
import time
import statistics
import random
import asyncio

nombre_archivo = "players.csv"

SOCK_BUFFER = 1024

countriesWC=["Qatar","Ecuador","Senegal","Netherlands","England","Iran","United States",
             "Wales","Argentina","Saudi Arabia","Mexico","Poland","France","Denmark",
             "Tunisia","Australia","Spain","Germany","Japan","Costa Rica","Belgium",
             "Canada","Morocco","Croatia","Brazil","Serbia","Switzerland","Cameroon",
             "Portugal","Ghana","Uruguay","Korea"]

lista_qatar = []
lista_ecuador = [] 
lista_senegal = []  
lista_netherlands = []

lista_england = []
lista_iran = [] 
lista_US = []  
lista_wales = []

lista_argentina = []
lista_arabia = [] 
lista_mexico = []  
lista_poland = []

lista_france = []
lista_denmark = [] 
lista_tunisia = []  
lista_australia = []

lista_spain = []
lista_germany = [] 
lista_japan = []  
lista_CR = []

lista_belgium = []
lista_canada = [] 
lista_morocco = []  
lista_croatia = []

lista_brazil = []
lista_serbia = [] 
lista_suiza = []  
lista_cameroon = []

lista_portugal = []
lista_ghana = [] 
lista_uruguay = []  
lista_korea = []

listas = [lista_qatar, lista_ecuador, lista_senegal, lista_netherlands,
          lista_england, lista_iran, lista_US, lista_wales,
          lista_argentina, lista_arabia, lista_mexico,  lista_poland,
          lista_france, lista_denmark, lista_tunisia,  lista_australia,
          lista_spain, lista_germany, lista_japan, lista_CR, 
          lista_belgium, lista_canada, lista_morocco, lista_croatia,
          lista_brazil, lista_serbia, lista_suiza,  lista_cameroon,
          lista_portugal, lista_ghana, lista_uruguay,  lista_korea ]

f = open (nombre_archivo,'r')
contenido = f.read()
f. close()

data = contenido.split("\n") 

#Pregunta B:
def lista_jugadores (pais, lista):

   last_season = ["2021", "2020", "2019", "2018", "2017",
                  "2018", "2017", "2016","2015","2014", "2013"]

   indice = 0 #Variable para indicar los valores de la columna "last_season"
   centinela = 0 #Variable para verificar si la lista de jugadores es 5 

   while (centinela == 0):

     for i in range(23693):
        dato = data[i+1].split(",")
        if (dato[6] == pais) and (dato[1] == last_season[indice]):
            lista.append(dato[3])
        if (len(lista) == 5):
           break    
      
     if (len(lista) < 5):
          indice = indice + 1
                  

     if (len(lista) >= 5):
          centinela = 1    


#Pregunta C:
def partido (tipo_de_partido, equipo1, equipo2):

    suma1 = 0 #Variable para registrar el valor de mercado del equipo1
    cantidad1 = 0 #Variable para contar la cantidad de valores del equipo1
    suma2 = 0 #Variable para registrar el valor de mercado del equipo2
    cantidad2 = 0 #Variable para contar la cantidad de valores del equipo2

    if (tipo_de_partido == "fase de grupos"):

        for i in range(23693):
          dato = data[i+1].split(",")

          if (dato[6] == equipo1):
              if (dato[13] == "" or dato[13] ==  ' '):
                 suma1 = suma1 + 0

              else:  
                 suma1 = suma1 + float(dato[13])
                 cantidad1 = cantidad1 + 1
    

          if (dato[6] == equipo2):

              if (dato[13] == "" or dato[13] ==  ' '):
                 suma2 = suma2 + 0

              else:  
                 suma2 = suma2 + float(dato[13])
                 cantidad2 = cantidad2 + 1
    

        prom1 = suma1/cantidad1
        prom2 = suma2/cantidad2

        #print(prom1)
        #print(prom2)

        #Ganador se define quien tenga el mayor valor de mercado promedio
        if (prom1 > prom2): 
            ganador = equipo1

        else :
            ganador = equipo2

    if (tipo_de_partido == "fase de eliminacion"):

        equipos = [equipo1, equipo2]
        ganador = random.choice(equipos) #Ganador se define de manera aleatoria     

    return ganador            
            
#Pregunta D:
async def grupos_async():

    ganador_partidos = []
    ganadores_grupos = []
    
    for i in range(0,31,4):

       centinela = 0 #Variable para identificar los  2 primeros puestos de cada grupo

       ganador1 = partido("fase de grupos",countriesWC[i],countriesWC[i+1])
       ganador2 = partido("fase de grupos",countriesWC[i],countriesWC[i+2])
       ganador3 = partido("fase de grupos",countriesWC[i],countriesWC[i+3])
       ganador4 = partido("fase de grupos",countriesWC[i+1],countriesWC[i+2])
       ganador5 = partido("fase de grupos",countriesWC[i+1],countriesWC[i+3])
       ganador6 = partido("fase de grupos",countriesWC[i+2],countriesWC[i+3])
       await asyncio.sleep(0.15)
 
       ganador_partidos = [ganador1, ganador2, ganador3, ganador4, ganador5, ganador6]
     
       ganador = max(set(ganador_partidos), key = ganador_partidos.count)

       ganadores_grupos.append(ganador)
    
       while (centinela == 0):
           ganador_partidos.remove(ganador)
           if ganador in ganador_partidos:
               centinela = 0

           else:
               centinela = 1           
    
       ganador = max(set(ganador_partidos), key = ganador_partidos.count)

       ganadores_grupos.append(ganador)

    return ganadores_grupos

#Pregunta E:
def grupos_sync():

    ganador_partidos = []
    ganadores_grupos = []
    
    for i in range(0,31,4):

       centinela = 0 #Variable para identificar los  2 primeros puestos de cada grupo

       ganador1 = partido("fase de grupos",countriesWC[i],countriesWC[i+1])
       time.sleep(0.15)
       ganador2 = partido("fase de grupos",countriesWC[i],countriesWC[i+2])
       time.sleep(0.15)
       ganador3 = partido("fase de grupos",countriesWC[i],countriesWC[i+3])
       time.sleep(0.15)
       ganador4 = partido("fase de grupos",countriesWC[i+1],countriesWC[i+2])
       time.sleep(0.15)
       ganador5 = partido("fase de grupos",countriesWC[i+1],countriesWC[i+3])
       time.sleep(0.15)
       ganador6 = partido("fase de grupos",countriesWC[i+2],countriesWC[i+3])
       time.sleep(0.15)
 
       ganador_partidos = [ganador1, ganador2, ganador3, ganador4, ganador5, ganador6]

       ganador = max(set(ganador_partidos), key = ganador_partidos.count)

       ganadores_grupos.append(ganador)
    
       while (centinela == 0):
           ganador_partidos.remove(ganador)
           if ganador in ganador_partidos:
               centinela = 0

           else:
               centinela = 1            
    
       ganador = max(set(ganador_partidos), key = ganador_partidos.count)

       ganadores_grupos.append(ganador)

    return ganadores_grupos

#Pregunta F:
async def eliminatorias_async():

    A1 = countriesWC[2] #Senegal
    A2 = countriesWC[1] #Ecuador

    B1 = countriesWC[4] #England
    B2 = countriesWC[7] #Wales

    C1 = countriesWC[10] #Mexico
    C2 = countriesWC[8] #Argentina

    D1 = countriesWC[12] #France
    D2 = countriesWC[14] #Tunisia

    E1 = countriesWC[16] #Spain
    E2 = countriesWC[17] #Germany

    F1 = countriesWC[23] #Croatia
    F2 = countriesWC[21] #Canada

    G1 = countriesWC[26] #Switzerland
    G2 = countriesWC[24] #Brazil

    H1 = countriesWC[30] #Uruguay
    H2 = countriesWC[31] #Korea

    #Octavos de final:
    ganador1 = partido("fase de eliminacion",A1,B2)
    ganador2 = partido("fase de eliminacion",C1,D2)

    ganador3 = partido("fase de eliminacion",E1,F2)
    ganador4 = partido("fase de eliminacion",G1,H2)

    ganador5 = partido("fase de eliminacion",D1,C2)
    ganador6 = partido("fase de eliminacion",B1,A2)

    ganador7 = partido("fase de eliminacion",H1,G2)
    ganador8 = partido("fase de eliminacion",F1,E2)
    
    await asyncio.sleep(0.15)
    
    #Cuartos de final:

    ganador1 = partido("fase de eliminacion",ganador1,ganador2)
    ganador2 = partido("fase de eliminacion",ganador3,ganador4)
    
    ganador3 = partido("fase de eliminacion",ganador5,ganador6)
    ganador4 = partido("fase de eliminacion",ganador7,ganador8)
    
    await asyncio.sleep(0.15)

    #Semifinal:
     
    finalista1 = partido("fase de eliminacion",ganador1,ganador2)
    finalista2 = partido("fase de eliminacion",ganador3,ganador4)

    await asyncio.sleep(0.15)

    if (finalista1 == ganador1):
        tercer_lugar1 = ganador2

    else:
        tercer_lugar1 = ganador1  

    if (finalista2 == ganador3):
        tercer_lugar2 = ganador4

    else:
        tercer_lugar2 = ganador3 

    #Tercer lugar:

    tercer_lugar = partido("fase de eliminacion",tercer_lugar1,tercer_lugar2)
    await asyncio.sleep(0.15)  

    #Final:

    primer_lugar = partido("fase de eliminacion",finalista1,finalista2)
    await asyncio.sleep(0.15)
       
    if (primer_lugar == finalista1):
        segundo_lugar = finalista2

    else:
        segundo_lugar = finalista1

    podio_async = [primer_lugar, segundo_lugar, tercer_lugar]

    return podio_async       

#Pregunta G:
def eliminatorias_sync():

    A1 = countriesWC[2] #Senegal
    A2 = countriesWC[1] #Ecuador

    B1 = countriesWC[4] #England
    B2 = countriesWC[7] #Wales

    C1 = countriesWC[10] #Mexico
    C2 = countriesWC[8] #Argentina

    D1 = countriesWC[12] #France
    D2 = countriesWC[14] #Tunisia

    E1 = countriesWC[16] #Spain
    E2 = countriesWC[17] #Germany

    F1 = countriesWC[23] #Croatia
    F2 = countriesWC[21] #Canada

    G1 = countriesWC[26] #Switzerland
    G2 = countriesWC[24] #Brazil

    H1 = countriesWC[30] #Uruguay
    H2 = countriesWC[31] #Korea

    #Octavos de final:
    ganador1 = partido("fase de eliminacion",A1,B2)
    time.sleep(0.15)
    ganador2 = partido("fase de eliminacion",C1,D2)
    time.sleep(0.15)

    ganador3 = partido("fase de eliminacion",E1,F2)
    time.sleep(0.15)
    ganador4 = partido("fase de eliminacion",G1,H2)
    time.sleep(0.15)

    ganador5 = partido("fase de eliminacion",D1,C2)
    time.sleep(0.15)
    ganador6 = partido("fase de eliminacion",B1,A2)
    time.sleep(0.15)

    ganador7 = partido("fase de eliminacion",H1,G2)
    time.sleep(0.15)
    ganador8 = partido("fase de eliminacion",F1,E2)
    time.sleep(0.15)
    
    #Cuartos de final:
    ganador1 = partido("fase de eliminacion",ganador1,ganador2)
    time.sleep(0.15)
    ganador2 = partido("fase de eliminacion",ganador3,ganador4)
    time.sleep(0.15)
    
    ganador3 = partido("fase de eliminacion",ganador5,ganador6)
    time.sleep(0.15)
    ganador4 = partido("fase de eliminacion",ganador7,ganador8)
    time.sleep(0.15)

    #Semifinal:
    finalista1 = partido("fase de eliminacion",ganador1,ganador2)
    time.sleep(0.15)
    finalista2 = partido("fase de eliminacion",ganador3,ganador4)
    time.sleep(0.15)

    if (finalista1 == ganador1):
        tercer_lugar1 = ganador2

    else:
        tercer_lugar1 = ganador1  

    if (finalista2 == ganador3):
        tercer_lugar2 = ganador4

    else:
        tercer_lugar2 = ganador3 

    #Tercer lugar:

    tercer_lugar = partido("fase de eliminacion",tercer_lugar1,tercer_lugar2)
    time.sleep(0.15) 

    #Final:

    primer_lugar = partido("fase de eliminacion",finalista1,finalista2)
    time.sleep(0.15)
       
    if (primer_lugar == finalista1):
        segundo_lugar = finalista2

    else:
        segundo_lugar = finalista1

    podio_sync = [primer_lugar, segundo_lugar, tercer_lugar]

    return podio_sync

if __name__=="__main__": 

    intentos = 1 #Variable para verificar que se ingreso nombre o mensaje clave en cliente 

    #Lista de jugadores
    lista_jugadores(countriesWC[0],lista_qatar)
    lista_jugadores(countriesWC[1],lista_ecuador)  
    lista_jugadores(countriesWC[2],lista_senegal) 
    lista_jugadores(countriesWC[3],lista_netherlands) 
    lista_jugadores(countriesWC[4],lista_england)
    lista_jugadores(countriesWC[5],lista_iran)  
    lista_jugadores(countriesWC[6],lista_US) 
    lista_jugadores(countriesWC[7],lista_wales) 
    lista_jugadores(countriesWC[8],lista_argentina)
    lista_jugadores(countriesWC[9],lista_arabia)  
    lista_jugadores(countriesWC[10],lista_mexico) 
    lista_jugadores(countriesWC[11],lista_poland)
    lista_jugadores(countriesWC[12],lista_france)
    lista_jugadores(countriesWC[13],lista_denmark)
    lista_jugadores(countriesWC[14],lista_tunisia)
    lista_jugadores(countriesWC[15],lista_australia)
    lista_jugadores(countriesWC[16],lista_spain)
    lista_jugadores(countriesWC[17],lista_germany)
    lista_jugadores(countriesWC[18],lista_japan)
    lista_jugadores(countriesWC[19],lista_CR) 
    lista_jugadores(countriesWC[20],lista_belgium)
    lista_jugadores(countriesWC[21],lista_canada)
    lista_jugadores(countriesWC[22],lista_morocco)
    lista_jugadores(countriesWC[23],lista_croatia)
    lista_jugadores(countriesWC[24],lista_brazil)
    lista_jugadores(countriesWC[25],lista_serbia)
    lista_jugadores(countriesWC[26],lista_suiza)
    lista_jugadores(countriesWC[27],lista_cameroon)  
    lista_jugadores(countriesWC[28],lista_portugal)
    lista_jugadores(countriesWC[29],lista_ghana)
    lista_jugadores(countriesWC[30],lista_uruguay)
    lista_jugadores(countriesWC[31],lista_korea)           

    #Creamos el objeto de socket para el servidor
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Conectandonos al servidor {server_address[0]}, en el puerto {server_address[1]}")
    sock.bind(server_address)

    #Escuchamos conexiones
    sock.listen(5)

    #Empezamos bucle de servidor
    while (intentos == 1):

        print("Ingresar nombre o mensaje clave")
        
        conn, client_address = sock.accept()

        try:
            frase = conn.recv(SOCK_BUFFER)
            data_conv = frase.decode('utf-8')

            #Pregunta H:
            if (data_conv == "Roger"):
                print(f"Mensaje recibido: {data_conv}") 
                print("Procesando data")
                conn.sendall(data)
                print("               ")

            #Pregunta I:
            if (data_conv == "equipos"):
                print(f"Mensaje recibido: {data_conv}")
                for i in range(32):

                   print(f"{countriesWC[i]} :")
                   print(listas[i])
     
                conn.sendall(data)
                print("               ")

            #Pregunta J: 
            if (data_conv == "fase de grupos asincrono"):  
                print(f"Mensaje recibido: {data_conv}")

                t1 = time.perf_counter()
                clasificados_async = asyncio.run(grupos_async())
                t2 = time.perf_counter()

                print(clasificados_async)
                tiempo_D = t2 - t1
                print(f"Tiempo total de ejecucion asincrona: {tiempo_D:0.2f} segundos")
                print("               ")

            #Pregunta K: 
            if (data_conv == "fase de grupos sincrono"):  
                print(f"Mensaje recibido: {data_conv}")

                t3 = time.perf_counter()
                clasificados_sync = grupos_sync()
                t4 = time.perf_counter()

                print(clasificados_sync)
                tiempo_E = t4 - t3
                print(f"Tiempo total de ejecucion sincrona: {tiempo_E:0.2f} segundos")
                print("               ")

            #Pregunta L: 
            if (data_conv == "eliminatorias asincrono"):  
                print(f"Mensaje recibido: {data_conv}")

                t5 = time.perf_counter()
                podio_async = asyncio.run(eliminatorias_async())
                t6 = time.perf_counter()

                print(podio_async)
                tiempo_F = t6 - t5
                print(f"Tiempo total de ejecucion asincrona: {tiempo_F:0.2f} segundos")
                print("               ")

            #Pregunta M: 
            if (data_conv == "eliminatorias sincrono"):  
                print(f"Mensaje recibido: {data_conv}")

                t7 = time.perf_counter()
                podio_sync = eliminatorias_sync()
                t8 = time.perf_counter()
                print(podio_sync)
                tiempo_G = t8 - t7
                print(f"Tiempo total de ejecucion sincrona: {tiempo_G:0.2f} segundos")    
                print("               ")

            #Pregunta N:
            if (data_conv == "reporte"):
                
                #Pregunta D:
                t1 = time.perf_counter()
                clasificados_async = asyncio.run(grupos_async())
                t2 = time.perf_counter()
                tiempo_D = t2 - t1
                
                #Pregunta E:
                t3 = time.perf_counter()
                clasificados_sync = grupos_sync()
                t4 = time.perf_counter()
                tiempo_E = t4 - t3
                
                #Pregunta F:
                t5 = time.perf_counter()
                podio_async = asyncio.run(eliminatorias_async())
                t6 = time.perf_counter()
                tiempo_F = t6 - t5
                
                #Pregunta G:
                t7 = time.perf_counter()
                podio_sync = eliminatorias_sync()
                t8 = time.perf_counter()
                tiempo_G = t8 - t7

                print(f"Mensaje recibido: {data_conv}")
                file = open("reporte.txt","w")
                file.write("Lista obtenida en el ítem d): \n")
                file.write(f"{clasificados_async} \n")
                file.write("-------------------------------\n")  
                file.write("Lista obtenida en el ítem e): \n")
                file.write(f"{clasificados_sync} \n") 
                file.write("-------------------------------\n")
                file.write(f"Tiempo total de ejecucion asincrona en el ítem d): {tiempo_D:0.2f} segundos \n")
                file.write(f"Tiempo total de ejecucion sincrona en el ítem e): {tiempo_E:0.2f} segundos \n")
                file.write("--------------------------------------------------------------------------------\n")
                file.write("Lista obtenida en el ítem f): \n")
                file.write(f"{podio_async} \n")
                file.write("-------------------------------\n")  
                file.write("Lista obtenida en el ítem g): \n")
                file.write(f"{podio_sync} \n") 
                file.write("-------------------------------\n")
                file.write(f"Tiempo total de ejecucion asincrona en el ítem f): {tiempo_F:0.2f} segundos \n")
                file.write(f"Tiempo total de ejecucion sincrona en el ítem g): {tiempo_G:0.2f} segundos \n")
                print("               ") 

            else:
                print(f"Mensaje recibido: {data_conv}")
                print("Datos incorrectos")
                intentos = 0

        except Exception as e:
            print(f"Sucedio algo: {e}")
        finally:
            conn.close()

    

      
         





