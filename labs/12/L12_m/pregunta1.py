

'''
Enunciado:

Dado el polinomio:
f(x) = x + 2x^2 + 3x^3 + 4x^4 + ... + 10000x^10000
Calcular el valor de f(2023). Para ello:
    - Escriba una función f cuyo parámetro de entrada sea X y retorne el valor de f(x). Este cálculo
    debe hacerse en serie, es decir no use multiprocessing. Calcule el tiempo de ejecución para f(2023)
    - Escriba la versión en paralelo de f, de tal manera de que el cálculo de f(x) sea paralelo en 4 procesos
    y el cálculo se haga más rápido. Calcule el Speed up respecto a la parte a)

Nota:
Al final de su archivo en Python, debe verificar que el resultado de la parte a) sea igual a la parte b).
Para ello agregue la siguiente línea al final de su programa:
assert resultado_serial == resultado_paralelo

Dónde resultado_serial y resultado_paralelo son las variables de su programa que contienen los
resultados de las partes a) y b). Si los resultados son iguales, la sentencia assert permitirá que su
programa termine exitosamente; caso contrario le generará un error, y eso será evidencia de que sus
resultados no coinciden.
'''

import time # Importamos el módulo time para medir el tiempo de ejecución
from multiprocessing import Pool, cpu_count # Importamos el módulo Pool para crear un pool de procesos y cpu_count para 
# obtener la cantidad de procesadores disponibles, para mapear múltiples outputs, usaremos el método starmap

def f_serial(x):
    suma = 0 # Inicializamos la variable de la suma en 0
    for i in range(1, 10001): # Iteramos desde 1 hasta 10000
        # Sumamos a la variable de la suma el producto de i por x elevado a la i
        suma += i * (x ** i)
    return suma

def f_parallel(x, i, resultado):
    # Calculamos el producto de i por x elevado a la i y lo guardamos en la posición i - 1 del arreglo resultado
    # debido a la construcción del iterador, que va de 1 a 100001
    resultado[i - 1] = i * (x ** i)
    return resultado[i - 1]

if __name__ == '__main__':

    x = 2023 # Valor de x
    tic_serial = time.perf_counter() # Iniciamos el contador de tiempo para medir el tiempo de ejecución de la implementación serial
    resultado_serial = f_serial(x) # Calculamos el resultado en serie
    toc_serial = time.perf_counter() # Iniciamos el contador de tiempo para medir el tiempo de ejecución de la implementación serial
    #print(f"Resultado en serie: {resultado_serial}") #for debugging purposes
    print(f"Tiempo de ejecucion en serie: {toc_serial - tic_serial} segundos")
    
    tic_parallel = time.perf_counter() # Iniciamos el contador de tiempo
    # Inicializamos el arreglo resultado
    resultado = [0] * 10000 # Inicializamos el arreglo resultado con 10000 ceros
    # Creamos un pool de procesos con la cantidad de procesadores disponibles
    p = Pool(processes=cpu_count())
    # Creamos una lista de tuplas con los argumentos para cada proceso
    args = [(x, i, resultado) for i in range(1, 10001)] # usamos una list comprehension para crear la lista de tuplas
    # que contiene los argumentos para cada proceso
    # Mapeamos los resultados de la función f_parallel a la lista de tuplas
    resultado = p.starmap(f_parallel, args)
    p.close() # Cerramos el pool
    p.join() # Esperamos a que los procesos terminen
    resultado_paralelo  = sum(resultado) # Sumamos los resultados de cada proceso
    toc_parallel = time.perf_counter() # Finalizamos el contador de tiempo

    #print(f"Resultado en paralelo: {resultado_paralelo}") #for debugging purposes
    print(f"Tiempo de ejecucion en paralelo: {toc_parallel - tic_parallel} segundos")

    # Verificamos que los resultados sean iguales
    assert resultado_serial == resultado_paralelo

    # Calculamos el speed up
    speed_up = (toc_serial - tic_serial) / (toc_parallel - tic_parallel)
    print(f"Speed up: {speed_up}")