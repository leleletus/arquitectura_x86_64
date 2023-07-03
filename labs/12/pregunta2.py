import time
from werkzeug.security import check_password_hash
from itertools import repeat,combinations,combinations_with_replacement,product
from multiprocessing import Pool, cpu_count
import string

#trabajamos suponinedo todo esta en minusculas
#arreglo de letras desde a a z sin la n
abecedario=list(string.ascii_lowercase)
#arreglo de las vocales
vocales= [abecedario[0],abecedario[4],abecedario[8],abecedario[14],abecedario[20]]


"""#
Esta es la contraseña que usted tiene que adivinar. Está encriptada para que no pueda saber cuál es la respuesta correcta a priori.
Lo que tiene que hacer es generar combinaciones de 3 letras y llamar a la función comparar_con_password_correcto(línea 24 de la plantilla)
"""
contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'

"""
Función que sirve para comparar su palabra(cadena de 3 caracteres) con la contraseña correcta.
Entrada: Su cadena de 3 caracteres
Salida: True(verdadero) si es que coincide con la contraseña correcta, caso contrario retorna False(falso)
"""
def comparar_con_password_correcto(palabra): #aqui compruebo si la contraseña es la correcta
	return check_password_hash(contrasena_correcta, palabra) #retorna true or false


def busca_contrasena_correcta():
    #global contrasenas
    #combinations_with_replacement(Aabecedario,3) si el orden no importara
    for i in vocales:
        for j in vocales:
            for k in abecedario:
                contrasena= i+j+k #al ser todos str se pueden sumar y se concadenan
                if comparar_con_password_correcto(contrasena):
                    correcto = contrasena
                    print(f'La contraseña es: {correcto}')
                    return correcto 
    

def busca_contrasena_correcta_paralelo():
    #global contrasenas
    #combinations_with_replacement(Aabecedario,3) si el orden no importara
    
    # Crear una lista para almacenar las contraseñas encontradas
    contrasenas_encontradas = []
    
    # Crear una función auxiliar para buscar contraseñas que cumplan con la condición del if
    def buscar_contrasenas(vocal1, vocal2):
        for k in abecedario:
            contrasena = vocal1 + vocal2 + k
            if comparar_con_password_correcto(contrasena):
                contrasenas_encontradas.append(contrasena)


if __name__ == "__main__":
    inicio_serial = time.perf_counter() #tomamos el tiempo inicial cuando se ejecuta esto ( como un flag)
    busca_contrasena_correcta()
    fin_serial = time.perf_counter() #tomamos el tiempo en el que acaba (flag o marca 2)
    print(f"Tiempo de ejecucion serial: {fin_serial - inicio_serial} segundos") 

    inicio_paralelo = time.perf_counter()
    p = Pool(processes=5) # Creamos el pool de 5 
    p.map(busca_contrasena_correcta_paralelo, vocales) # Ejecutamos la función target en cada uno de los procesos, para cada una de las 5 vocales
	# guardadas en la lista 'vocales' usando el método .map() del pool de processes
	# Cerramos el pool de processes y esperamos a que terminen de ejecutarse todos los procesos:
    p.close()
    p.join()
    fin_paralelo = time.perf_counter()
    print(f'El tiempo de ejecución del método paralelizado es: {fin_paralelo - inicio_paralelo} segundos')

	# Ahora comparamos los tiempos de ejecución calculando el speedup:
    speedup = (fin_serial - inicio_serial) / (fin_paralelo - inicio_paralelo)
    print(f'El speedup obtenido es: {speedup}')
