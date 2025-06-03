import time
from statistics import mean
import numpy as np
import math



def norma_sincrona(vec_a,vec_b,tam):
    resultado=0
    dif_cuad=0
    for i in range(tam):
        dif_cuad+= (vec_b[i] - vec_a[i])**2
        #print(dif_cuad)
    resultado=math.sqrt(dif_cuad)
    #print(resultado)
    return resultado



if __name__ == '__main__':

    tamano=4096
    max=1000
    #genero vectores con mnumeros enteros de tamaño n de maximo de 0 a 99
    vec_a = np.random.randint(max, size=(tamano,)) 
    vec_b = np.random.randint(max, size=(tamano,))

    #print(vec_a)

    tiempo = list()
    for i in range (5): #repetimos unas 5 veces para mayor exactitud en los tiempos
        inicio_serial = time.perf_counter()
        resultado_serial=norma_sincrona(vec_a,vec_b,tamano)
        fin_serial = time.perf_counter()
        tiempo.append(fin_serial -inicio_serial )

    print(f"Tiempo de ejecucion serial: {mean(tiempo)} segundos")