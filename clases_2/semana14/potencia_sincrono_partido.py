import time
#
def potencia(n: int, div: int = 1) -> int:
    res = 1
    for _ in range(1, (n // div) + 1):
        res *= n
    
    return res


if __name__ == '__main__':
    inicio = time.perf_counter()
    pot1 = potencia(100_000, 2)
    pot2 = potencia(100_000, 2)
    pot = pot1 * pot2
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")