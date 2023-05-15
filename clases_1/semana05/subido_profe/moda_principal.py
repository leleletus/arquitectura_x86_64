import ctypes
import statistics
import time
import numpy as np

def moda_python(arreglo, N):
    cont_max = 0
    for i in range(N):
        cont_int = 0
        for j in range(N):
            if (arreglo[i] == arreglo[j]):
                cont_int = cont_int + 1
        if (cont_int>cont_max):
            cont_max = cont_int
            moda_value = arreglo[i]
    return moda_value 


if __name__ == '__main__':
    # Llamada a la libreria .so
    lib = ctypes.CDLL('./lib_moda.so')
    # Declarar argumentos de entrada
    lib.moda_c.argtypes = [np.ctypeslib.ndpointer(dtype = np.int32), ctypes.c_int]
    lib.moda_asm_int.argtypes = [np.ctypeslib.ndpointer(dtype = np.int32), ctypes.c_int]
    
    # Declarar la salida
    lib.moda_c.restype = ctypes.c_int
    lib.moda_asm_int.restype = ctypes.c_int
    
    N = 5
    arreglo_entrada = np.random.randint(2,5,N, dtype = np.int32)
    print(arreglo_entrada)
    print(statistics.mode(arreglo_entrada))
    print(moda_python(arreglo_entrada,N))
    print(lib.moda_c(arreglo_entrada, N))
    print(lib.moda_asm_int(arreglo_entrada, N))
