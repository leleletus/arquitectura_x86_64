import time
from threading import Thread


res_parcial = list()

def potencia(n: int, div: int = 1):
    global res_parcial

    res = 1
    for _ in range(1, (n // div) + 1):
        res *= n
    
    res_parcial.append(res)


if __name__ == '__main__':
    t1 = Thread(target=potencia, args=(100_000, 2))
    t2 = Thread(target=potencia, args=(100_000, 2))
    inicio = time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    resultado = res_parcial[0] * res_parcial[1]
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")
    