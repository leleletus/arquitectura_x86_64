import numpy as np
import ctypes
import time
import stadistics
import matplotlib.pyplot as plt

def norma2(vevtor,N):
    for i in range(N):
        s=vector[i]*vector[i]
    return s


if __name__ == '__main__': #si el nombre es main sera funcion principal
    #es lo mismo poner fef main y luego main

    #Al llamar a la libreria que genera c:
    lib=ctypes.CDLL('./libreria_norma_2.so')
    #debo declarar los argumentos de entrada
    lib.cFloatNormTwo.argtypes=[np.ctypeslib.ndpinter(dtype=np.float32)]
    lib.asmFloatNormTwo.argtypes=[np-ctypeslib.ndpinter(dtype=np.float32)]
    #debo declarar el argumento de salida
    lib.cFloatNormTwo.restype=ctypes.c_float
    lib.asmFloatNormTwo.restype=ctypes.c_float


    N=2
    v1= np.random.rand(N).astype(np.float32) #ojo, debe ser el mismo formato de 32 bits
    #print( type(v1[0]) )
    print(f"{v1} <- Resultado")

    print(norma_2_python(v1,N))
    print()
    print()
    print()


    iterraciones=30
    N_total = [4,8,16,32,64,128,256,1024,2048,4096]
    lista_N_total_p =[]
    lista_N_total_c =[]
    lista_N_total_asm =[]
    lista_p =[]
    lista_c =[]
    lista_asm =[]
    for m in range (iteraciones):




    lista_N_python.append(stadistics.median(lista_p))
    print(stadistics.median(lista_c))
    print(stadistics.median(lista_asm))


  