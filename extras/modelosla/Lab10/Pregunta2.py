import time
import multiprocessing
from multiprocessing.sharedctypes import Value

def func_voltajes(archivo):

   contador_corte_mayo = 0
   contador_sobretension_mayo = 0
   contador_corte_junio = 0
   contador_sobretension_junio = 0

   f = open(archivo,'r')
   contenido = f.read()  
   f.close()
   data = contenido.split("\n")
   
   if (archivo == "bi_data_voltajes_mayo_todos.csv"):
     #Pregunta a:
     for i in range(2801229):
          datos = data[i+1].split(",")
          if ((float(datos[3]) <= 50.0) or (float(datos[4]) <= 50.0) or (float(datos[4]) <= 50.0)):
              contador_corte_mayo = contador_corte_mayo + 1

     corte_mayo.value = contador_corte_mayo        

     #Pregunta b:
     for j in range(2801229):
          datos = data[j+1].split(",")
          if ((float(datos[3]) >= 277.0) or (float(datos[4]) >= 277.0) or (float(datos[4]) >= 277.0)):
              contador_sobretension_mayo = contador_sobretension_mayo + 1   

     sobretension_mayo.value = contador_sobretension_mayo   

   if (archivo == "bi_data_voltajes_junio_todos.csv"):
     #Pregunta a:
     for i in range(1344608):
          datos = data[i+1].split(",")
          if ((float(datos[3]) <= 50.0) or (float(datos[4]) <= 50.0) or (float(datos[4]) <= 50.0)):
              contador_corte_junio = contador_corte_junio + 1
   
     corte_junio.value = contador_corte_junio        

     #Pregunta b:
     for j in range(1344608):
          datos = data[j+1].split(",")
          if ((float(datos[3]) >= 277.0) or (float(datos[4]) >= 277.0) or (float(datos[4]) >= 277.0)):
              contador_sobretension_junio = contador_sobretension_junio + 1   

     sobretension_junio.value = contador_sobretension_junio           

if __name__=="__main__":

    archivo1 = "bi_data_voltajes_mayo_todos.csv"
    archivo2 = "bi_data_voltajes_junio_todos.csv"

    corte_mayo = Value('i', 0)
    sobretension_mayo = Value('i', 0)
    corte_junio = Value('i', 0)
    sobretension_junio = Value('i', 0)  

    t1 = multiprocessing.Process(target=func_voltajes, args=(archivo1,))
    t2 = multiprocessing.Process(target=func_voltajes, args=(archivo2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    if (corte_mayo.value > corte_junio.value):
        print("Mayo es el mes que tiene la mayor cantidad de mediciones donde al menos una de las fases está en corte")
    else:
        print("Junio es el mes que tiene la mayor cantidad de mediciones donde al menos una de las fases está en corte")
    
    if (sobretension_mayo.value > sobretension_junio.value):
        print("Mayo es el mes que tiene la mayor cantidad de mediciones donde al menos una de las fases está en sobretension")
    else:
        print("Junio es el mes que tiene la mayor cantidad de mediciones donde al menos una de las fases está en sobretension")
    