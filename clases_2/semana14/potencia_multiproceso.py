from multiprocessing import Process, Manager
import time

#manager (como variable global)
#las variables globales ya no son compartidas porque cada proceso tiene su propiuo espacio de memoria
#no es como los hilos

#en multihilo usabamos block/logs para que no se acceda mientras uno este haciendo (race condition)





def potencia(n: int, rlist: list[int],  div: int = 1):
    res = 1
    for _ in range(1, (n // div) + 1):
        res *= n
    
    rlist.append(res)
    

if __name__ == '__main__':
    v = 100_000
    manager = Manager() # crea lista compartida 
    return_list = manager.list()
    p1 = Process(target=potencia, args=(v, return_list, 2))
    p2 = Process(target=potencia, args=(v, return_list, 2))

    inicio = time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    resultado = return_list[0] * return_list[1]
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion {fin - inicio} segundos")