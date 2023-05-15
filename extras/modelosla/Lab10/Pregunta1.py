import time
from multiprocessing import Process
from multiprocessing.sharedctypes import Value

#Pregunta a:
def func_serial (x):

    y = 0

    for i in range(10000):
        y = y + (i+1)*pow(x,(i+1))
        
    return y   

#Pregunta b:
def func_paralelo_1 (x,y): 
    y_paralelo = 0

    for i in range(2500):
       y_paralelo = y_paralelo + (i+1)*pow(x,(i+1))  

    y1.value = y_paralelo   


def func_paralelo_2 (x,y): 
    y_paralelo = y

    for i in range(2500,5000):
       y_paralelo = y_paralelo + (i+1)*pow(x,(i+1))  

    y1.value = y_paralelo   


def func_paralelo_3 (x,y): 
    y_paralelo = y

    for i in range(5000,7500):
       y_paralelo = y_paralelo + (i+1)*pow(x,(i+1))  

    y1.value = y_paralelo   

def func_paralelo_4 (x,y): 
    y_paralelo = y

    for i in range(7500,10000):
       y_paralelo = y_paralelo + (i+1)*pow(x,(i+1)) 

    y1.value = y_paralelo                    

if __name__ == '__main__':

    x = 2022 #Variable de entrada para las funciones en serie y paralelo
    y1 = Value('i', 0) #Variable de entrada para la funcion en paralelo
    resultado_paralelo = 0 #Variable de salida para la funcion en paralelo

    inicio_serie = time.perf_counter()
    resultado_serial = func_serial(x)
    fin_serie = time.perf_counter()
    t_serie = fin_serie - inicio_serie
    #print(f"Resultado en serie : {resultado_serial}")    
    
    funciones = [func_paralelo_1,func_paralelo_2,func_paralelo_3,func_paralelo_4]
    
    inicio_paralelo = time.perf_counter()

    for i in range(4):
      t1 = Process(target=funciones[i], args=(x,int(y1.value)))
      t1.start()
      t1.join()

      y1 = Value('i', y1.value)
    
    fin_paralelo = time.perf_counter()
    t_paralelo = fin_paralelo - inicio_paralelo
    resultado_paralelo = y1.value  

    #print(f"Resultado en paralelo : {resultado_paralelo}")
    print(f"Speedup (factor de aceleración) : {t_serie/t_paralelo}")

    assert resultado_serial == resultado_paralelo
   