import time
import numpy as np
from itertools import repeat
from multiprocessing import Pool, cpu_count


N = 5000
M = 5000

def mult_vector_vector(x, y):
    suma = 0

    for i in range(len(y)):
        suma += x[i] * y[i]
    
    return suma


def main(mat_M, vector_A, pool_size):
    args = zip(mat_M, repeat(vector_A))
    p = Pool(processes=pool_size)
    resultado = p.starmap(mult_vector_vector, args)
    p.close()
    p.join()

    return resultado


if __name__ == '__main__':
    resultado = list()

    mat_M = np.random.randint(100, size=(M,N))
    vector_A = np.random.randint(100, size=(M,))

    pool_sizes = [2, 4, 8, 16, 32]
    tiempos = list()
    
    for pool_size in pool_sizes:
        tiempos_parciales = list()
        for i in range(4):
            print(f"Procesando iteracion {i + 1} con numero de procesos: {pool_size}")
            inicio = time.perf_counter()
            main(mat_M, vector_A, pool_size)
            fin = time.perf_counter()
            tiempos_parciales.append(fin - inicio)
        tiempos_parciales.sort()
        tiempo = tiempos_parciales[len(tiempos_parciales) // 2]
        tiempos.append((pool_size, tiempo))

    for item in tiempos:
        print(f"Tiempo de ejecucion con {item[0]} procesos: {item[1]} segundos")
