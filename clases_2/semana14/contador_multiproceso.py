import time
from multiprocessing import Process

CUENTA = 50_000_000

def cuenta(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    #se crean objetos process que ejecutaran la funcion cuenta
    p1 = Process(target=cuenta, args=(CUENTA // 2, ))
    p2 = Process(target=cuenta, args=(CUENTA // 2, ))

    inicio = time.perf_counter()
    p1.start() #se inician los procesos
    p2.start()
    p1.join()
    p2.join() #se espera que finalicen
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")
