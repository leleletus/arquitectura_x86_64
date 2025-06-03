import time
from statistics import mean
import numpy as np
import math
from multiprocessing import Pool, cpu_count


def f_multiprocess(vec_a,vec_b,n,temp): #calculamos la diferencia
    
    temp[n]= (vec_b[n] - vec_a[n])**2
    return temp[n]



if __name__ == '__main__':

    tamano=4096
    max=1000
    #genero vectores con mnumeros enteros de tamaño n de maximo de 0 a 99
    vec_a = np.random.randint(max, size=(tamano,)) 
    vec_b = np.random.randint(max, size=(tamano,))

    #print(vec_a)

    tiempo = list()
    for i in range (5): #repetimos unas 5 veces para mayor exactitud en los tiempos
        inicio_multiprocess = time.perf_counter()

        temp=[0] * tamano
        resultado = [0] * tamano
        p1 = Pool(processes=8)
        
        resultado= p1.starmap(f_multiprocess,((vec_a, vec_b, n,temp) for n in range(tamano)))
        p1.close() #para no agregar mas
        p1.join() #espera que acabe

        resultado_paralelo = math.sqrt(sum(resultado))

        fin_multiprocess = time.perf_counter()
        tiempo.append(fin_multiprocess -inicio_multiprocess )

    print(f"Tiempo de ejecucion multiproceso: {mean(tiempo)} segundos")