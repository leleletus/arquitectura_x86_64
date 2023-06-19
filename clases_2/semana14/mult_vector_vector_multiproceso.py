import time
import numpy as np
from itertools import repeat
from multiprocessing import Pool, cpu_count

#si deseo usar los 5mil paralelos serian como 5mil process al mismo tiempo pero no es viable
#no tengo tantos nucleos asi que se pelearian entre ellos por tiemnpo en cpu
#no tendria suficiente memoria para tener tantos

#para eso usaria itertools (pull de processor) thread pull excecutor era cantidad fija de hilos
#ayuda para que un proceso acabe hace la siguiente, ayuda a que no pase lo de arriba, solo corren cantidad fija de procesos

#si tengo n a= [1,2,3,4] y b = [5,6,7,8] quiero unirlos, entonces necesito una tupla
# iuna forma seria c= [(a[0],b[0]),(a[1],b[1]), ...]
#otra forma con un list comprenhension   cremaos c=list() luego   c =[(a[i],b[i]) for i in range(leng(a))]
#otra forma es con zip      creamos c=list() y luego   c= zip(a,b)
#otra forma d=9       e= [(a[i],d) for i in range(len(a)) ]      #asi tenemos a con nueve 
#usando el itertools           e=zip(a,repeat(d))     asi tendriamos lo mismo de arriba pero mas facil


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
    args = zip(mat_M, repeat(vector_A))
    p = Pool(processes=cpu_count())
    resultado = p.starmap(mult_vector_vector, args)
    p.close()
    p.join()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion multiproceso: {fin - inicio} segundos")

