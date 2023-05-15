import time
from multiprocessing import Process
import numpy as np
import random

#Pregunta a:
def arreglo_aleatorio():
    #row = random.randint(1,9)
    row = 4
    col = 3
    
    arreglo = np.random.rand(row,col).astype(np.float32)

    return arreglo    

#Pregunta b:
def punto_medio(arr1,arr2):
    x = (arr1[0] + arr2[0])/2  
    y = (arr1[1] + arr2[1])/2 
    z = (arr1[2] + arr2[2])/2

    punto_medio = [x,y,z]  

    return punto_medio

#Pregunta c:
def punto_medio_total():

    matriz = []
    puntos = []
    referencia = []
    indice = 0
    row = 16
    col = 3
    centinela = 0

    arr = np.random.rand(row,col).astype(np.float32)
    

    print(arr)


    for i in range(int(row/2)):
        arr1 = arr[indice]
        arr2 = arr[indice+1]
        punto = punto_medio(arr1,arr2) 
        puntos.append(punto) 
        indice = indice + 2  

    while (centinela == 0):
      indice = 0
      row = len(puntos)
      for i in range(int(row/2)):  
         arr1 = puntos[indice]
         arr2 = puntos[indice+1]
         punto = punto_medio(arr1,arr2)
         referencia.append(punto)
         indice = indice + 2 

      matriz = referencia.copy()

      if (len(matriz) <= 1):
         centinela = 1
      else:
         puntos.clear()
         puntos = referencia.copy()

         referencia.clear()    
    
    print("    ")
    print(matriz)  

#Pregunta d:
def punto_medio_total_d(arr): 

    matriz = []
    puntos = []
    referencia = [] 
    indice = 0
    centinela = 0


    cantidad = len(arr)
    print(f"Tamaño del arreglo original : {cantidad}")
    for i in range(int(cantidad/2)):
        arr1 = arr[indice]
        arr2 = arr[indice+1]
        punto = punto_medio(arr1,arr2) 
        puntos.append(punto) 
        indice = indice + 2  

    while (centinela == 0):
      indice = 0
      cantidad = len(puntos)
      for i in range(int(cantidad/2)):  
         arr1 = puntos[indice]
         arr2 = puntos[indice+1]
         punto = punto_medio(arr1,arr2)
         referencia.append(punto)
         indice = indice + 2 

      matriz = referencia.copy()

      if (len(matriz) <= 1):
         centinela = 1
      else:
         puntos.clear()
         puntos = referencia.copy()

         referencia.clear()    
    
    print(matriz)      
                 
if __name__ == '__main__':

    arreglo = arreglo_aleatorio()
    print("Arreglo aleatorio :")
    print(arreglo)
    print("     ")

    arr1 = [0.3,0.0,0.4]
    arr2 = [0.1,0.2,0.3]
    
    p_medio = punto_medio(arr1,arr2)
    print(f"El punto medio es : {p_medio}")

    print("    ")
    punto_medio_total()

    print("    ")
    punto_medio_total_d(arreglo)


    ejem1 = np.random.rand(32,3).astype(np.float32)
    ejem2 = np.random.rand(128,3).astype(np.float32)
    ejem3 = np.random.rand(1024,3).astype(np.float32)
    ejem4 = np.random.rand(2048,3).astype(np.float32)
    ejem5 = np.random.rand(8192,3).astype(np.float32)
    ejem6 = np.random.rand(16384,3).astype(np.float32)
    ejem7 = np.random.rand(65536,3).astype(np.float32)

    listas = [ejem1, ejem2, ejem3, ejem4,ejem5,ejem6, ejem7]

    print("    ")
    for i in range(len(listas)):
       t1 = Process(target=punto_medio_total_d, args=(listas[i], ))
       inicio = time.perf_counter()
       t1.start()
       t1.join()
       fin = time.perf_counter()
       print(f"Proceso num : {i + 1}")
       print(f"Tiempo de ejecucion: {fin - inicio} segundos")
    


    
 

     