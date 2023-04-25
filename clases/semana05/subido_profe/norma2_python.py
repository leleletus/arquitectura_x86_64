import numpy as np
import ctypes
import time
import statistics
import matplotlib.pyplot as plt

def norma2_python(vector,N):
    s = 0
    for i in range(N):
        s = vector[i]*vector[i] + s
    return np.sqrt(s)

if __name__ == "__main__":
    # Llamar a la librería que genera C
    lib = ctypes.CDLL('./libreria_norma2.so')    
    # Debo declarar los argumentos de entrada
    lib.cFloatNormTwo.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_int]
    lib.asmFloatNormTwo.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_int]
    # Debo declarar el argumento de salida
    lib.cFloatNormTwo.restype = ctypes.c_float
    lib.asmFloatNormTwo.restype = ctypes.c_float
    
    iteraciones = 30
    N_total = [4,8,16,32,64,128,256,512,1024,2048,4096]
    lista_N_python = []
    lista_C_python = []
    lista_ASM_python = []
    for N in N_total:
        lista_p = []
        lista_c = []
        lista_asm = []
        for m in range(iteraciones):
        
            v1 = np.random.rand(N).astype(np.float32)
            tic1 = time.perf_counter()
            norma2_python(v1,N)
            toc1 = time.perf_counter()
            lista_p.append(1e6*(toc1-tic1))
            tic2 = time.perf_counter()
            lib.cFloatNormTwo(v1,N)
            toc2 = time.perf_counter()
            lista_c.append(1e6*(toc2-tic2))
            tic3 = time.perf_counter()
            lib.asmFloatNormTwo(v1,N)
            toc3 = time.perf_counter()
            lista_asm.append(1e6*(toc3-tic3))

        lista_N_python.append(statistics.median(lista_p))
        lista_C_python.append(statistics.median(lista_c))
        lista_ASM_python.append(statistics.median(lista_asm))

    # plt.plot(N_total,lista_N_python,"r")
    # plt.plot(N_total,lista_C_python,"g")
    # plt.plot(N_total,lista_ASM_python,"b")
    # plt.grid()
    # plt.savefig("Prueba_norma2.png",dpi = 400)

    SUP_Py_C = [a//b for a,b in zip(lista_N_python, lista_C_python)]
    SUP_PY_ASM = [a//b for a,b in zip(lista_N_python, lista_ASM_python)]
    plt.plot(N_total,SUP_Py_C, "r")
    plt.plot(N_total,SUP_PY_ASM,"b")
    plt.grid()
    plt.xlabel("Tamaño N")
    plt.ylabel("SpeedUP")
    plt.savefig("SpeedUP",dpi = 400 )
