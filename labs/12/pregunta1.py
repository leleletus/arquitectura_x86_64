import time
import numpy as np
from multiprocessing import Pool, cpu_count
import sys

N=10_000 #cantidad
sys.set_int_max_str_digits(0) #para que alcance en entero un valor tan grande

def f(x: int):
    global N
    calculo=0
    for i in range (1,N+1):
        calculo+= i*x**i
        #print(i,calculo) #para verificar su correcto funcionamiento
    return calculo



if __name__ == '__main__':

    #parte serial
    inicio_serial = time.perf_counter() #tomamos el tiempo inicial cuando se ejecuta esto ( como un flag)
    resultado_serial=f(2023) #para compararlo luego
    fin_serial = time.perf_counter() #tomamos el tiempo en el que acaba (flag o marca 2)
    print(f"Tiempo de ejecucion serial: {fin_serial - inicio_serial} segundos") #vemos cuando se tardo viendo la resta de ambos flags
    #Tiempo de ejecucion serial: 2.1717678000000888 segundos
    
    
    inicio_paralelo = time.perf_counter()
    p1 = Pool(processes=4) #haciendo que solo haya 4 procesos
    resultado_paralelo = p1.map_async(f,(2023, )).get()
    p1.close() #para no agregar mas
    p1.join() #espera que acabe
    fin_paralelo = time.perf_counter() 
    print(f"Tiempo de ejecucion paralelo: {fin_paralelo - inicio_paralelo} segundos") #vemos cuando se tardo viendo la resta de ambos flags
    #Tiempo de ejecucion paralelo: 2.1953747000006842 segundo
    print(f"Speedup:{((fin_serial - inicio_serial)-(fin_paralelo - inicio_paralelo))/((fin_serial - inicio_serial))} ") #calculo del speedup

    assert resultado_serial == int(resultado_paralelo[0])


