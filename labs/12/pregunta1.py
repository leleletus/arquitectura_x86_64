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

def f_multiprocess(x, i, resultado): #x para saber su valor a remplazar, i para saber los numeros a multipliccar y resultado para guardar en el arreglo
    # Calculamos el producto de i por x elevado a la i y lo guardamos en la posición i - 1 del arreglo resultado
    # ya que termino 1 es el array[0] aunque i=1
    resultado[i - 1] = i * (x ** i)
    return resultado[i - 1]

if __name__ == '__main__':
    x=2023
    
    #parte serial
    inicio_serial = time.perf_counter() #tomamos el tiempo inicial cuando se ejecuta esto ( como un flag)
    resultado_serial=f(x) #para compararlo luego
    fin_serial = time.perf_counter() #tomamos el tiempo en el que acaba (flag o marca 2)
    print(f"Tiempo de ejecucion serial: {fin_serial - inicio_serial} segundos") #vemos cuando se tardo viendo la resta de ambos flags
    #Tiempo de ejecucion serial: 2.1717678000000888 segundos
    
    
    inicio_paralelo = time.perf_counter()
    p1 = Pool(processes=4) #haciendo que solo haya 4 procesos como se indico
    #de poder usar todos seria cpu_count()
    resultado = [0] * N #rellenamos de 0 para que tenga esa cantidad de elementos
    #usamos startmap por ser varios argumentos 
    #si resultado [0, 0] = [0]*2 y args = [(2023, i, resultado) for i in range(1, 10)] #[(2023, 1, [0, 0]), (2023, 2, [0, 0]), ..etc
    #resultado= p1.starmap(f_multiprocess,args) #seria asisi lo separamos
    resultado= p1.starmap(f_multiprocess,((x, i, resultado) for i in range(1, N+1)))
    p1.close() #para no agregar mas
    p1.join() #espera que acabe
    resultado_paralelo = sum(resultado)
    fin_paralelo = time.perf_counter() 
    print(f"Tiempo de ejecucion paralelo: {fin_paralelo - inicio_paralelo} segundos") #vemos cuando se tardo viendo la resta de ambos flags
    #Tiempo de ejecucion paralelo: 2.1953747000006842 segundo
    print(f"Speedup:{((fin_serial - inicio_serial)-(fin_paralelo - inicio_paralelo))/((fin_serial - inicio_serial))} ") #calculo del speedup

    assert resultado_serial == resultado_paralelo

    # Calculamos el speed up
    speed_up = (fin_serial - inicio_serial) / (fin_paralelo - inicio_paralelo)
    print(f"Speed up: {speed_up}")


