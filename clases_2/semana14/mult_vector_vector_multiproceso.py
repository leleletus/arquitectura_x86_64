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


if __name__ == '__main__':#
    resultado = list()

    mat_M = np.random.randint(100, size=(M,N))
    vector_A = np.random.randint(100, size=(M,))

    inicio = time.perf_counter()
    args = zip(mat_M, repeat(vector_A))
    p = Pool(processes=cpu_count()) #devuelve el numero de nucleos (en mi caso 32)
    #crea objeto ppoll que controla yb grupo de procesos de trabajo al que se pueden
    #enviar trabajos. el parametro processes especifica el numero de procesos de trabajo que se usaran
    #si este es None , utiliza el numero devuelto por os.cpu_count()

    resultado = p.starmap(mult_vector_vector, args) #metodo de Pool que permite
    #"aplicar una funcion a multiples argumentos en paralelo"
    #starmap toma como argumentos una función y un iterable de iterables,
    #  donde cada iterable interno contiene los argumentos para una llamada
    #  a la función. El resultado es un iterable que contiene el resultado
    #  de aplicar la función a cada conjunto de argumentos
    #se está aplicando la función mult_vector_vector a cada conjunto de 
    # argumentos en args en paralelo y almacenando el resultado en la variable resultado
    p.close()
    p.join()

    #p.close() le indica al objeto Pool que no acepte más trabajosp.
    # join() le indica al objeto Pool que espere hasta que todos los trabajos
    #  hayan finalizado y luego salga, limpiando efectivamente el grupo de procesos
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion multiproceso: {fin - inicio} segundos")

#compartir datos entre diferentes procesos, puedes utilizar un objeto Manager del módulo multiprocessing. Un objeto Manager permite crear y administrar objetos compartidos entre procesos, como listas, diccionarios y valores.

#Para utilizar un objeto Manager, primero debes crear una instancia del mismo utilizando Manager(). Luego puedes utilizar los métodos del objeto Manager para crear objetos compartidos, como list(), dict() y Value().

#Por ejemplo, para crear una lista compartida entre procesos, puedes hacer lo siguiente:

#from multiprocessing import Manager

#manager = Manager()
#shared_list = manager.list()
#Luego puedes pasar la lista compartida como argumento a los procesos y modificarla dentro de ellos. Los cambios realizados en la lista compartida serán visibles para todos los procesos que tengan acceso a ella.

