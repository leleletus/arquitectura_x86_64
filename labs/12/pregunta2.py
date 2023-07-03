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

#contrasenas=[] #mi lista vacia donde se guardaran todas las posibles contraseñas

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


def contrasena_correcta():
    #global contrasenas
    #combinations_with_replacement(Aabecedario,3) si el orden no importara
    correcto=0
    arreglo = list(product(abecedario, repeat=3))
    for i in range(len(arreglo)):
        if( arreglo[i][0] == vocales[0] or arreglo[i][0] ==vocales[1] or arreglo[i][0] ==vocales[2] or arreglo[i][0] ==vocales[3] or arreglo[i][0] ==vocales[4]): # and en caso de juntarlos
            if( (arreglo[i][1]) == (vocales[0] or (arreglo[i][1]) ==vocales[1] or (arreglo[i][1]) ==vocales[2] or (arreglo[i][1]) ==vocales[3] or (arreglo[i][1]) ==vocales[4])):
                string_contrasena = "".join(arreglo[i]) #unimos los 3 caracteres
                if(comparar_con_password_correcto(string_contrasena)):  #comparo las contraseñas
                    correcto = string_contrasena
                    break

    return correcto
    



if __name__ == "__main__":
    inicio_serial = time.perf_counter() #tomamos el tiempo inicial cuando se ejecuta esto ( como un flag)
    contrasena_correcta()
    fin_serial = time.perf_counter() #tomamos el tiempo en el que acaba (flag o marca 2)
    print(f"Tiempo de ejecucion serial: {fin_serial - inicio_serial} segundos") 

    inicio_paralelo = time.perf_counter()
    p1 = Pool(processes=cpu_count()) #haciendo que todos
    resultado_paralelo = p1.map_async(contrasena_correcta).get()
    p1.close() #para no agregar mas
    p1.join() #espera que acabe
    fin_paralelo = time.perf_counter()
    print(f"Tiempo de ejecucion paralelo: {fin_paralelo - inicio_paralelo} segundos")
    pass
