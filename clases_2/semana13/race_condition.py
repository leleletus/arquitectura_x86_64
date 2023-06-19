import time
import concurrent.futures #para usar ThreadPoolExecutor o processpoolexcecutor


class FakeDatabase: #definimos la clase 
    def __init__(self): #metodo init que se llama automaticamente cuando se crea una instancia de la clase
        self.value = 0
    
    def update(self, name): #metodo update 
        print(f"Thread {name}, iniciando actualizacion")
        local_copy = self.value #guardo valor de value 
        local_copy += 1 #le sumo 1
        time.sleep(0.1) #espero, me hago el flojo
        self.value = local_copy #actualizo el valor de value
        print(f"Thread {name} terminando actualizacion") 


if __name__ == '__main__':
    workers = 5
    tasks = workers * 2
    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")

    #ThreadPoolExecutor y executor desde python 3.2 para no usar start y join
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor: #with para que cierre cuando no se use
        #pide el max workers, de no ponerse predetieminado es none y determinara autimaticamente los hilos en funcion a los procesadores
        #podemos usar thread_name_prefix para darle un name
        #es una subclase de Executor que utiliza un grupo de hilos para ejecutar llamadas de forma asíncrona
        for index in range(tasks): #envio las 10 tareas al ejecutor para que las haga y submit
            executor.submit(db.update, index) #cada tare a hace un update de fakedatabase y pasamos index como arg
            #submit toma una funcion y luego el parametro para la funcion , exceutor ejecuta un hilo separado 

    print(f"Valor final de la base de datos: {db.value}")


#pasan por: has not sufficiently protected data accesses to prevent threads from interfering with each other.

