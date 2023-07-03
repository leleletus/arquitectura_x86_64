
"""
Enunciado:
Escriba un programa en Python que imprima si un número es primo o no. El algoritmo sugerido
para saber si un número es primo es el siguiente:
Dado un número n, verificar si es divisible entre [2, sqrt(n)]
Si es divisible entre algún número dentro de ese intervalo, no es primo; caso contrario sí es primo.

a) Escriba una función que reciba como parámetro de entrada el argumento n y retorne True si es primo,
   o False en caso contrario (Implementación serial). Imprima el tiempo de ejecución para n = 2 345 678 911 111 111
b) Escriba una función divida la tarea de la parte en a) en 2 subtareas y permita paralelizar el cálculo de si
   un número es primo o no. Use 2 procesos.

Imprima el tiempo de ejecución de esta función para el mismo valor de n de la parte a). Calcule
el Speedup. Use la función assert() para verificar que el resultado en la implementación serial sea igual a la
implementación en paralelo.

c) Luego, Escriba una función que reciba como parámetro un número X y que encuentre el primer número primo mayor a X.
Para ello, su función debe tener un bucle, y en cada iteración calcular si es que los 2 números siguientes impares 
son primos o no usando multiprocessing con 2 procesos, 1 proceso por cada número impar a comprobar. ((Solo se deben
revisar los siguientes impares porque los pares ya se sabe que no son primos)

Por ejemplo, si X = 24:
Primera iteración: Se chequea si 25 y 27 son primos. Como no lo son, continuamos iterando
Segunda iteración: Se chequear si 29 y 31 son primos. Como 29 es primo, aquí se detiene el bucle.

Para corroborar en cada iteración si es que alguno de sus números impares es primo o no
puede usar su función de la parte a o de la parte b, eso es opcional. Lo importante en esta
pregunta es usar multiprocessing por cada número impar a verificar en cada iteración.
Su función debe imprimir el texto: “El siguiente número primo encontrado es P” donde P es el
número que Ud ha encontrado.
"""

import time
import math
from multiprocessing import Process, cpu_count

def es_primo_serial(n):
    if n == 1:
        # No consideramos a 1 como un número primo
        return False
    elif n == 2:
        # 2 es el único número primo par
        return True
    else:
        # Empezamos a iterar en el rango [2, sqrt(n)] para verificar si n es divisible entre algún número
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                # Si n es divisible entre algún número dentro del rango, entonces no es primo
                return False # Retornamos False para indicar que n no es primo y terminamos la función
        return True # Si n no es divisible entre ningún número dentro del rango, entonces es primo
    
def es_primo_paralelo_process(n,process_id):
    """
    Esta función contendrá el mismo algoritmo que la función es_primo_serial(n), pero será ejecutada en un proceso que
    tendrá como argumento de entrada no solo el número n sino también un id que puede tomar el valor de '1' o '2'
    Ambos procesos verificarán si el número es par (estará fuera del condicional controlado por el process_id)
    Si es que el número no es par, trabajaremos de la siguiente manera diferencia para cada proceso:
        - El proceso con id '1' verificará si n es divisible entre los números impares dentro del rango [3, floor(sqrt(n)/2)]
        - El proceso con id '2' verificará si n es divisible entre los números impares dentro del rango [floor(sqrt(n)/2) + 2, sqrt(n)]
    """
    if n == 1:
        # No consideramos a 1 como un número primo
        return False
    elif n == 2:
        # 2 es el único número primo par
        return True
    else:
        # Verificamos si n es par
        if n % 2 == 0:
            # Si n es par, entonces no es primo
            return False
        else:
            # Si n es impar, entonces verificamos si es primo
            if process_id == 1:
                # Verificamos si n es divisible entre los números impares dentro del rango [3, floor(sqrt(n)/2)]
                for i in range(3, math.floor(math.sqrt(n) / 2) + 1, 2):
                    if n % i == 0:
                        # Si n es divisible entre algún número dentro del rango, entonces no es primo
                        return False
                return True
            elif process_id == 2:
                # Verificamos si n es divisible entre los números impares dentro del rango [floor(sqrt(n)/2) + 2, sqrt(n)]
                for i in range(math.floor(math.sqrt(n) / 2) + 2, math.floor(math.sqrt(n)) + 1, 2):
                    if n % i == 0:
                        # Si n es divisible entre algún número dentro del rango, entonces no es primo
                        return False
                return True
            else:
                # Si el process_id no es '1' ni '2', entonces no se ejecutará el proceso
                print("Error: process_id debe ser '1' o '2'")
                return False

siguiente_primo_encontrado = False # Bandera global usada para sincronizar ambos procesos, véase explicación en la función de abajo
def encuentra_proximo_primo_process(X,process_id):
    """
    Esta función recibe como parámetro de entrada el número X y un id de proceso que puede tomar el valor de '1' o '2'
    En ambos procesos se trabajará de manera similar, pero el punto de partida será diferente para encontrar el siguiente
    número primo mayor a X. Ambos procesos verificarán si X es par, y en base a ello tomarán como punto de partida para realizar
    sus iteraciones o bien X+2 y X+4 (si es que este es impar, estos serán los dos siguientes impares), o X+1 y X+3 (si es que
    este es par, estos serán los dos siguientes impares), para los procesos con id '1' y '2' respectivamente.
    Luego, específicamente se trabajará de la siguiente manera diferenciada en cada proceso:
     - El proceso con id '1' empezará a iterar o bien desde X+2 si es que X es impar, o bien desde X+1 si es que X es par; y en cada
       iteración verificará si el número actual de la variable de control del bucle es primo o no usando la función es_primo_serial (para
       evitar abrir más procesos utilizando la implementación paralela, aunque podría ser más eficiente hacer eso, pero no es la meta de
       este inciso). Si es que el número actual es primo, entonces se imprime el texto "El siguiente número primo encontrado es P" donde P
       es el número actual de la variable de control del bucle, y se termina el bucle. Si es que el número actual no es primo, entonces
       se añade 4 a la variable de control del bucle para pasar al siguiente número impar a verificar sin volver a evaluar el número que
       ya ha sido evaluado por el proceso con id '2'.
    - En el proceso con id '2' se trabajará de manera similar, pero se empezará a iterar o bien desde X+4 si es que X es impar, o bien
      desde X+3 si es que X es par, y de la misma manera, si es que se salta a la siguiente iteración porque el número actual no es primo,
      entonces se añadirá 4 a la variable de control del bucle para pasar al siguiente número impar a verificar sin volver a evaluar el
      número que ya ha sido evaluado por el proceso con id '1'.

    Por último, para sincronizar ambos procesos y que no se siga ejecutando el otro si es que uno de ellos ya encontró el número primo
    deseado, se utilizará una bandera global llamada siguiente_primo_encontrado, que será inicializada en False, y que será cambiada a
    True cuando uno de los procesos encuentre el número primo deseado.
    """
    global siguiente_primo_encontrado
    if not siguiente_primo_encontrado:
        if X % 2 == 0:
            # Si X es par, entonces el punto de partida para encontrar el siguiente número primo será X+1
            inicio_process_1 = X + 1
            inicio_process_2 = X + 3
        else:
            # Si X es impar, entonces el punto de partida para encontrar el siguiente número primo será X+2
            inicio_process_1 = X + 2
            inicio_process_2 = X + 4
        if process_id == 1:
            # Empezamos a iterar desde el punto de partida para encontrar el siguiente número primo
            numero_actual = inicio_process_1 # inicializamos la variable que contendrá el número actual de la variable de control del bucle
            while not siguiente_primo_encontrado:
                if es_primo_serial(numero_actual):
                    # Si el número actual es primo, entonces imprimimos el texto y terminamos el bucle
                    print("El siguiente número primo encontrado es", numero_actual)
                    siguiente_primo_encontrado = True
                else:
                    # Si el número actual no es primo, entonces pasamos al siguiente número impar a verificar
                    numero_actual += 4

        elif process_id == 2:
            # Empezamos a iterar desde el punto de partida para encontrar el siguiente número primo
            numero_actual = inicio_process_2 # inicializamos la variable que contendrá el número actual de la variable de control del bucle
            while not siguiente_primo_encontrado:
                if es_primo_serial(numero_actual):
                    # Si el número actual es primo, entonces imprimimos el texto y terminamos el bucle
                    print("El siguiente número primo encontrado es", numero_actual)
                    siguiente_primo_encontrado = True
                else:
                    # Si el número actual no es primo, entonces pasamos al siguiente número impar a verificar
                    numero_actual += 4
    else:
        # Si la bandera global siguiente_primo_encontrado es True, entonces no se ejecutará el proceso
        #print("El siguiente número primo ya ha sido encontrado por otro proceso") #for debugging purposes
        return


if __name__ == "__main__":
    # Para las partes a y b, mediremos el tiempo de ejecución para el siguiente número:
    n = 2345678911111111
    # Ejecución de la implementación serial (parte a):
    tic_parte_a = time.perf_counter()
    es_primo_serial(n)
    toc_parte_a = time.perf_counter()
    tiempo_parte_a = toc_parte_a - tic_parte_a
    print("Tiempo de ejecución de la implementación serial:", tiempo_parte_a, "segundos")

    # Ejecución de la implementación paralela (parte b):
    tic_parte_b = time.perf_counter()
    # Creamos los dos procesos que ejecutarán la función encuentra_proximo_primo_process
    process_1 = Process(target=encuentra_proximo_primo_process, args=(n,1))
    process_2 = Process(target=encuentra_proximo_primo_process, args=(n,2))
    # Iniciamos los dos procesos
    process_1.start()
    process_2.start()
    # Esperamos a que los dos procesos terminen
    process_1.join()
    process_2.join()
    toc_parte_b = time.perf_counter()
    tiempo_parte_b = toc_parte_b - tic_parte_b
    print("Tiempo de ejecución de la implementación paralela:", tiempo_parte_b, "segundos") 

    # Para la parte c, mediremos el tiempo de ejecución para los siguientes números:
    nums_parte_c = (104,205,489,1042)
    # Ejecución de la parte c:
    for n in nums_parte_c:
        tic_parte_c = time.perf_counter()
        # Creamos los dos procesos que ejecutarán la función encuentra_proximo_primo_process
        process_1 = Process(target=encuentra_proximo_primo_process, args=(n,1))
        process_2 = Process(target=encuentra_proximo_primo_process, args=(n,2))
        # Iniciamos los dos procesos
        process_1.start()
        process_2.start()
        # Esperamos a que los dos procesos terminen
        process_1.join()
        process_2.join()
        toc_parte_c = time.perf_counter()
        tiempo_parte_c = toc_parte_c - tic_parte_c
        print("Tiempo de ejecución de la implementación paralela para n =", n, ":", tiempo_parte_c, "segundos")