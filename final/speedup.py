import time
from statistics import mean
import numpy as np
import math
import concurrent.futures
from threading import Thread
from multiprocessing import Pool, cpu_count

def norma_sincrona(vec_a,vec_b,tam):
    resultado=0
    dif_cuad=0
    for i in range(tam):
        dif_cuad+= (vec_b[i] - vec_a[i])**2
        #print(dif_cuad)
    resultado=math.sqrt(dif_cuad)
    #print(resultado)
    return resultado


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



def f_multiprocess(vec_a,vec_b,n,temp): #calculamos la diferencia
    
    temp[n]= (vec_b[n] - vec_a[n])**2
    return temp[n]


if __name__ == '__main__':

    tamano=4096
    max=1000
    tiempo_sincrono=0
    tiempo_multihilo=0
    tiempo_multiprocess=0
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
        tiempo_sincrono=mean(tiempo)
    print(f"Tiempo de ejecucion serial: {tiempo_sincrono} segundos")



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
        tiempo_multihilo=mean(tiempo)

    print(f"Tiempo de ejecucion multihilo: {tiempo_multihilo} segundos")

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
        tiempo_multiprocess=mean(tiempo)

    print(f"Tiempo de ejecucion multiproceso: {tiempo_multiprocess} segundos")


    # Calculamos el speed up
    speed_up1 = (tiempo_sincrono) / (tiempo_multihilo)
    speed_up2 = (tiempo_sincrono) / (tiempo_multiprocess)
    print(f"Speed up sincrono con multihilo: {speed_up1}")
    print(f"Speed up sincrono con multiprocess: {speed_up2}")