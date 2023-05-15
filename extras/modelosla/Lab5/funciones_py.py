import numpy as np
import ctypes
import time
import statistics
import matplotlib.pyplot as plt

def matvecRMRV(A,x,b,N):
  tmp = 0.0
  for i in range(N):
    tmp = 0.0
    for j in range(N):
      tmp = tmp + A[i*N + j]*x[j]

    b[i] = tmp

def matvecRMCV(A,x,b,N):
  tmp = 0.0
  for j in range(N):
    for i in range(N):
       b[i] = b[i] + A[i*N + j]*x[j]    

if __name__ == "__main__":
  n = 1024
  N = [256, 512, 1024, 2048]
  mediana_RMRV_py=[]
  mediana_RMRV_c=[]
  mediana_RMRV_asm=[]
  mediana_RMCV_py=[]
  mediana_RMCV_c=[]
  mediana_RMCV_asm=[]
  SpeedUP_py = []
  SpeedUP_c = []
  SpeedUP_asm = []

  lib = ctypes.CDLL('./funciones.so')
  lib.matvecRMRV_c.argtypes=[np.ctypeslib.ndpointer(dtype=np.float64),np.ctypeslib.ndpointer(dtype=np.float64),np.ctypeslib.ndpointer(dtype=np.float64),ctypes.c_int]
  lib.matvecRMCV_c.argtypes=[np.ctypeslib.ndpointer(dtype=np.float64),np.ctypeslib.ndpointer(dtype=np.float64),np.ctypeslib.ndpointer(dtype=np.float64),ctypes.c_int]
  lib.matvecRMRV_asm.argtypes=[np.ctypeslib.ndpointer(dtype=np.float64),np.ctypeslib.ndpointer(dtype=np.float64),np.ctypeslib.ndpointer(dtype=np.float64),ctypes.c_int] 
  lib.matvecRMCV_asm.argtypes=[np.ctypeslib.ndpointer(dtype=np.float64),np.ctypeslib.ndpointer(dtype=np.float64),np.ctypeslib.ndpointer(dtype=np.float64),ctypes.c_int]   

  
  #Calculo de error relativo
  A1 = np.random.rand(n,n)
  Y1 = A1.flatten()
  x1 = np.random.rand(n,1)
  bref1 = np.dot(A1,x1)
  # zeros_like te da un arreglo con las mismas dimensiones que el argumento, pero lleno de zeros
  bRMRV = np.zeros_like(bref1)
  matvecRMRV(Y1,x1,bRMRV,n)
  # error relativo   
  print(f"El error relativo de la funcion matvecRMRV es {np.linalg.norm(bref1-bRMRV)/np.linalg.norm(bref1)}")  

  A2 = np.random.rand(n,n)
  Y2 = A2.flatten()
  x2 = np.random.rand(n,1)
  bref2 = np.dot(A2,x2)
  # zeros_like te da un arreglo con las mismas dimensiones que el argumento, pero lleno de zeros
  bRMCV = np.zeros_like(bref2)
  matvecRMCV(Y2,x2,bRMCV,n)
  # error relativo
  print(f"El error relativo de la funcion matvecRMCV es {np.linalg.norm(bref2-bRMCV)/np.linalg.norm(bref2)}")

  for m in N:
       trmrv_py = []
       trmrv_c= []
       trmrv_asm = []
       trmcv_py = []
       trmcv_c= []
       trmcv_asm = []
       
       for i in range(10):
          A_py = np.random.rand(m,m)
          x_py = np.random.rand(m,1)
          A_c = np.random.rand(m,m)
          x_c = np.random.rand(m,1)
          A_asm = np.random.rand(m,m)
          x_asm = np.random.rand(m,1)
          # entradas RM
          Arm_py = A_py.flatten()
          Arm_c = A_c.flatten()
          Arm_asm = A_asm.flatten()
          # referencia
          bref_py = np.dot(A_py,x_py)
          bref_c = np.dot(A_c,x_c)
          bref_asm = np.dot(A_asm,x_asm)
          # salidas
          bRMRV_py = np.zeros_like(bref_py)
          bRMRV_c = np.zeros_like(bref_c)
          bRMRV_asm = np.zeros_like(bref_asm)
          bRMCV_py = np.zeros_like(bref_py)
          bRMCV_c = np.zeros_like(bref_c)
          bRMCV_asm = np.zeros_like(bref_asm)

          s1 = time.perf_counter()
          matvecRMRV(Arm_py,x_py, bRMRV_py,m)
          e1 = time.perf_counter()
          tiempo_RMRV_py = e1 - s1
          trmrv_py.append(tiempo_RMRV_py)

          s2 = time.perf_counter()
          lib.matvecRMRV_c(Arm_c,x_c,bRMRV_c,m)
          e2 = time.perf_counter()
          tiempo_RMRV_c = e2 - s2
          trmrv_c.append(tiempo_RMRV_c)

          s3 = time.perf_counter()
          lib.matvecRMRV_asm(Arm_asm,x_asm,bRMRV_asm,m)
          e3 = time.perf_counter()
          tiempo_RMRV_asm = e3 - s3
          trmrv_asm.append(tiempo_RMRV_asm)

          s4 = time.perf_counter()
          matvecRMCV(Arm_py,x_py, bRMRV_py,m)
          e4 = time.perf_counter()
          tiempo_RMCV_py = e4 - s4
          trmcv_py.append(tiempo_RMCV_py)

          s5 = time.perf_counter()
          lib.matvecRMCV_c(Arm_c,x_c,bRMRV_c,m)
          e5 = time.perf_counter()
          tiempo_RMCV_c = e5 - s5
          trmcv_c.append(tiempo_RMCV_c)

          s6 = time.perf_counter()
          lib.matvecRMCV_asm(Arm_asm,x_asm,bRMRV_asm,m)
          e6 = time.perf_counter()
          tiempo_RMCV_asm = e6 - s6
          trmcv_asm.append(tiempo_RMCV_asm)

       mediana_RMRV_py.append(statistics.median(trmrv_py))
       mediana_RMRV_c.append(statistics.median(trmrv_c))
       mediana_RMRV_asm.append(statistics.median(trmrv_asm))
       mediana_RMCV_py.append(statistics.median(trmcv_py))
       mediana_RMCV_c.append(statistics.median(trmcv_c))
       mediana_RMCV_asm.append(statistics.median(trmcv_asm))

       #SpeedUP_py.append(statistics.median(trmcv_py)/statistics.median(trmrv_py))
       #SpeedUP_c.append(statistics.median(trmcv_c)/statistics.median(trmrv_c))

plt.plot(N,mediana_RMRV_py, 'r-o', label='RowMajor-RowView-py')
plt.plot(N, mediana_RMRV_c, 'g-o', label='RowMajor-RowView-c')
plt.plot(N, mediana_RMRV_asm, 'b-o', label='RowMajor-RowView-asm')
plt.plot(N,mediana_RMCV_py, 'r-o', label='RowMajor-RowView-py')
plt.plot(N, mediana_RMCV_c, 'g-o', label='RowMajor-RowView-c')
plt.plot(N,mediana_RMRV_py, 'r-o', label='RowMajor-RowView-py')
plt.plot(N, SpeedUP_py, 'r-o')
plt.plot(N, SpeedUP_c, 'g-o')
plt.xlabel('N')
plt.ylabel('tiempo promedio')
#plt.ylabel('SpeedUP')
plt.savefig("grafico.png",dpi = 500)