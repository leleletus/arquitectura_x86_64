import time
#calculamos la potencia de un numero 

def potencia(n: int, div: int = 1) -> int:
    res = 1
    for _ in range(1, (n // div) + 1):
        res *= n
    
    return res


if __name__ == '__main__':
    inicio = time.perf_counter()
    pot = potencia(100_000)
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")