import time #para poder usar el tiempo 

CUENTA = 50_000_000 #establecemos nuestra variable global de unos 50M
# se puede usar el guion bajo en los numeros para separar los miles y sea mas facil leer el numero

#creamos nuestra funcion cuenta
def cuenta(n: int):  #esperamos que la variable n que se le pase a la funcion sea un int (entero)
    while n > 0: #terminamos a contar cuando llegue a 0
        n -= 1 #va contando de forma regresiva


if __name__ == '__main__': #para que el interprete solo lo corra cuando lo ejecutamos como programa y no al usarlo como libreria para usar las funciones
    inicio = time.perf_counter() #tomamos el tiempo inicial cuando se ejecuta esto ( como un flag)
    cuenta(CUENTA) #ejecutamos nuestra funcion
    fin = time.perf_counter() #tomamos el tiempo en el que acaba (flag o marca 2)

    print(f"Tiempo de ejecucion: {fin - inicio} segundos") #vemos cuando se tardo viendo la resta de ambos flags


#problemas de este sincrono secuencial si pongo varias cuentas:
# I/O-bound pasas mas tiempo esperando un input/putput que ejecutando codigo

"""Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer.
Speeding it up involves overlapping the times spent waiting for these devices. """