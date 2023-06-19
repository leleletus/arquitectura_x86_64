import time
import numpy as np

#para entender como se hizo de manera secuencial

N = 5000
M = 5000

def mult_vector_vector(x, y):
    suma = 0

    for i in range(len(y)):
        suma += x[i] * y[i]
    
    return suma


if __name__ == '__main__':
    resultado = list()

    mat_M = np.random.randint(100, size=(M,N))
    vector_A = np.random.randint(100, size=(M,))

    inicio = time.perf_counter()
    for vector in mat_M:
        res_parcial = mult_vector_vector(vector, vector_A)
        resultado.append(res_parcial)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")

