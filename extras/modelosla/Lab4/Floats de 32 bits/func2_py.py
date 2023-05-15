import ctypes
import numpy as np
import time
import statistics
import matplotlib.pyplot as plt

def func_python(arr,N):
    suma = 0
    mul = 1
    for i in range(0,N,2):
        suma = suma + arr[i]
        mul = mul * arr[i+1]

    #print(suma)
    #print(mul)    

if __name__ == '__main__':
    N = 2048
    time_list_py = []
    time_abs_py = []
    time_list_c = []
    time_abs_c = []
    time_list_asm = []
    time_abs_asm = []
    veces = range(N)

    suma_c = np.arange(0.0,1.0).astype(np.float32) 
    mul_c = np.arange(1.0,2.0).astype(np.float32)
    suma_asm = np.arange(0.0,1.0).astype(np.float32) 
    mul_asm = np.arange(1.0,2.0).astype(np.float32)  
    arr2 = np.arange(4.0,N+4.0).astype(np.float32)    
    #print(arr2)   

     
    #print("Suma y multiplicacion con float32 en python :")
    for i in range(N): 
      for j in range(100):
          inicio_py = time.perf_counter() 
          func_python(arr2,N) 
          fin_py = time.perf_counter()
          tiempo_py = fin_py - inicio_py 
          time_list_py.append(tiempo_py)
      time_abs_py.append(statistics.median(time_list_py))
    

    lib = ctypes.CDLL('./funciones.so')
    lib.func2_c.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32),np.ctypeslib.ndpointer(dtype=np.float32),np.ctypeslib.ndpointer(dtype=np.float32),ctypes.c_int]

    #print("Suma y multiplicacion con float32 en c :")
    for a in range(N): 
      for b in range(100):
          inicio_c = time.perf_counter() 
          lib.func2_c(arr2,suma_c,mul_c, N)
          fin_c = time.perf_counter()
          tiempo_c = fin_c - inicio_c 
          time_list_c.append(tiempo_c)
      time_abs_c.append(statistics.median(time_list_c))
    #print(suma_c[0])
    #print(mul_c[0])

    lib.func2_asm.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32),np.ctypeslib.ndpointer(dtype=np.float32),np.ctypeslib.ndpointer(dtype=np.float32),ctypes.c_int]

    #print("Suma y multiplicacion con float32 en asm :")
    for m in range(N): 
      for n in range(100):
          inicio_asm = time.perf_counter() 
          lib.func2_asm(arr2,suma_asm,mul_asm, N)
          fin_asm = time.perf_counter()
          tiempo_asm = fin_asm - inicio_asm
          time_list_asm.append(tiempo_asm)
      time_abs_asm.append(statistics.median(time_list_asm))
    #print(suma_asm[0])
    #print(mul_asm[0])

    plt.plot (veces,time_abs_asm,'r-+' )
    plt.xlabel("tiempo")
    plt.xlabel("N")
    plt.grid
    plt.savefig("grafico.png",dpi = 500)

 