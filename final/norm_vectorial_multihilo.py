import time
from statistics import mean
import numpy as np
import math
import concurrent.futures
from threading import Thread


def dif(vec_a,vec_b,n): #calculamos la diferencia
    global dif_cuad

    for i in range(n):
        dif_cuad[i]+= (vec_b[i] - vec_a[i])

def potencia(n): 
    global pot
    for i in range(n):
        pot[i]=dif_cuad[i]**2

def raiz(n):
    global resp
    temp=0
    for i in range(n):
        temp += pot[i]
    resp = math.sqrt(temp)


if __name__ == '__main__':

    tamano=4096
    max=100
    #genero vectores con mnumeros enteros de tamaño n de maximo de 0 a 99
    vec_a = np.random.randint(max, size=(tamano,)) 
    vec_b = np.random.randint(max, size=(tamano,))

    #print(vec_a)

    tiempo = list()
    for i in range (5): #repetimos unas 5 veces para mayor exactitud en los tiempos
        inicio_multihilo = time.perf_counter()

        dif_cuad=[0]*tamano
        pot=[0]*tamano
        resp=0.0

        thread_1=Thread(target=dif, args=(vec_a,vec_b,tamano))
        thread_2=Thread(target=potencia, args=(tamano,))

        thread_1.start()
        thread_2.start()

        thread_1.join()
        thread_2.join()
    
        thread_3=Thread(target=raiz, args=(tamano,))
        thread_3.start()
        thread_3.join()

        resultado_multihilo=resp

        fin_multihilo = time.perf_counter()
        tiempo.append(fin_multihilo -inicio_multihilo )

    print(f"Tiempo de ejecucion multihilo: {mean(tiempo)} segundos")