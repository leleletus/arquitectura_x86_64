import time
import statistics
import matplotlib.pyplot as plt

archivo = "data_encoders.txt"

if __name__=="__main__":

       a = 0 #Variable para detectar la cantidad de reinicios

       #Contadores para hallar cuántos reinicios se registran en cada rueda
       contador1 = 0
       contador2 = 0
       contador3 = 0
       contador4 = 0
       contador5 = 0
       contador6 = 0

       t1 = time.perf_counter() 
       f = open(archivo,'r')
       contenido = f.read()
       f.close()
       t2 = time.perf_counter() 
       
       tiempo_lectura = t2 - t1

       print(f"El tiempo para leer el archivo fue de: {tiempo_lectura} msec")
       print("-----------------------------------------------------------------")

       datos = contenido.split("\n")
       
       #Rueda 1:
       for i in range(31920):
          valor_1 = datos[i+1+a].split(",")
          valor_2 = datos[i+2+a].split(",")
          a = 0

          diferencia = (int(valor_2[0]) - int(valor_1[0]))
          
          if (abs(diferencia) > 2500): #Valor referencial para determinar el numero de reinicios

             contador1 = contador1 + 1
             a = a + 1
       
       #Rueda 2:
       for i in range(31920):
          valor_1 = datos[i+1+a].split(",")
          valor_2 = datos[i+2+a].split(",")
          a = 0

          diferencia = (int(valor_2[1]) - int(valor_1[1]))
          
          if (abs(diferencia) > 2500): #Valor referencial para determinar el numero de reinicios

             contador2 = contador2 + 1
             a = a + 1    
       
       #Rueda 3:
       for i in range(31920):
          valor_1 = datos[i+1+a].split(",")
          valor_2 = datos[i+2+a].split(",")
          a = 0

          diferencia = (int(valor_2[2]) - int(valor_1[2]))
          
          if (abs(diferencia) > 2500): #Valor referencial para determinar el numero de reinicios

             contador3 = contador3 + 1
             a = a + 1   

       #Rueda 4:
       for i in range(31920):
          valor_1 = datos[i+1+a].split(",")
          valor_2 = datos[i+2+a].split(",")
          a = 0

          diferencia = (int(valor_2[3]) - int(valor_1[3]))
          
          if (abs(diferencia) > 2500): #Valor referencial para determinar el numero de reinicios

             contador4 = contador4 + 1
             a = a + 1    

       #Rueda 5:
       for i in range(31920):
          valor_1 = datos[i+1+a].split(",")
          valor_2 = datos[i+2+a].split(",")
          a = 0

          diferencia = (int(valor_2[4]) - int(valor_1[4]))
          
          if (abs(diferencia) > 2500): #Valor referencial para determinar el numero de reinicios

             contador5 = contador5 + 1
             a = a + 1 

       #Rueda 6:
       for i in range(31920):
          valor_1 = datos[i+1+a].split(",")
          valor_2 = datos[i+2+a].split(",")
          a = 0

          diferencia = (int(valor_2[5]) - int(valor_1[5]))
          
          if (abs(diferencia) > 2500): #Valor referencial para determinar el numero de reinicios

             contador6 = contador6 + 1
             a = a + 1                      

       print(f"El encoder de la rueda 1 ha presentado: {contador1} reinicios") 
       print(f"El encoder de la rueda 2 ha presentado: {contador2} reinicios")  
       print(f"El encoder de la rueda 3 ha presentado: {contador3} reinicios") 
       print(f"El encoder de la rueda 4 ha presentado: {contador4} reinicios")
       print(f"El encoder de la rueda 5 ha presentado: {contador5} reinicios")
       print(f"El encoder de la rueda 6 ha presentado: {contador6} reinicios")
       print("-----------------------------------------------------------------")
       
       t3 = time.perf_counter() 
       b = open("data_encoders.csv",'w')
       lineas = b.write(contenido)
       f.close()
       t4 = time.perf_counter() 
       
       tiempo_escritura = t4 - t3

       print(f"El tiempo para escribir el archivo fue de: {tiempo_escritura} msec")

 