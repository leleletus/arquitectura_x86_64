import time
from threading import Thread #importo la clase Trhead del modulpo/libreria threading


#defino mi variable global
CUENTA = 50_000_000 # _ para separar numeros


def cuenta(n: int): # nuestra funcion que espera un parametro de entrada int
    while n > 0: #cuenta regresiva hasta 0
        n -= 1


if __name__ == '__main__': #ejecutamos main solo si lo ejecutamos directamente, no como modulo
    # objeto thread asignado a t1
    #especifico que el "target" es la funcion cuenta
    #los argumentos son : la mitad entera de cuenta
    t1 = Thread(target=cuenta, args=(CUENTA // 2, )) # // para divisicon entera para abajo (trunca)
    t2 = Thread(target=cuenta, args=(CUENTA // 2, )) #las tuplas no se 
    #args pide una tupla 
    # en caso tengamos 1 solo argumento ebemos agregar ", " 
    # es para evitar ambigüedades en la sintaxis de Python, si tenemos 2 o mas no es necesario

    
    inicio = time.perf_counter() #iniciamos flag para medir tiempo
    t1.start() #al llamar start , se inicia un nuvo hilo de ejecucion  que llama a cuenta con su argumento
    t2.start()
    t1.join() # hace esperar  que termine de ejecutarse el hilo, el hilo principal se mantiene esperand
    t2.join() # de no ser por este el principal acaba sin que estos acaben
    fin = time.perf_counter() #marcamos el ultimo flag

    print(f"Tiempo de ejecucion: {fin - inicio} segundos") # vemos el tiempo que demora

    