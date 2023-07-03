

'''
Enunciado:
Usted entra con su laptop a una cafetería a la que solía ir con frecuencia y se da cuenta que le
han cambiado la contraseña a su WiFi. Así que decide intentar adivinar la nueva contraseña del WiFi.

Usted escucha una conversación de la mesa del costado en la que pudo notar que la
contraseña tiene 3 letras, y sabe en base a experiencias pasadas de que siempre las dos
primeras letras son vocales. En base a esta información, se le pide:

- En la plantilla dada para el laboratorio, escriba una función que retorne la contraseña correcta.
  El método que debe seguir es el método de fuerza bruta: Va a iterar sobre todas las combinaciones
  posibles en base a la información que tiene (3 letras, y las 2 primeras son vocales). Calcule el tiempo de ejecución.

- Usando multiprocessing, escriba una función que paralelice el método de fuerza bruta usado en la parte a). Para ello,
  va a crear 5 procesos, donde cada proceso toma como parámetro de entrada una de las 5 vocales y la asume como la primera 
  letra de la contraseña.
'''

import time
from werkzeug.security import check_password_hash
from multiprocessing import Pool

"""
Esta es la contraseña que usted tiene que adivinar. Está encriptada para que no pueda saber cuál es la respuesta correcta a priori.
Lo que tiene que hacer es generar combinaciones de 3 letras y llamar a la función comparar_con_password_correcto(línea 24 de la plantilla)
"""
contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'


# Arreglo con las letras del abecedario. Puede serle de ayuda, no es obligatorio que lo use
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vocales = ['a', 'e', 'i', 'o', 'u']

"""
Función que sirve para comparar su palabra(cadena de 3 caracteres) con la contraseña correcta.
Entrada: Su cadena de 3 caracteres
Salida: True(verdadero) si es que coincide con la contraseña correcta, caso contrario retorna False(falso)
"""
def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

"""
Función que sirve para generar todas las combinaciones posibles de 3 letras en base a las letras del abecedario (implementación serial)
Entrada: No tiene
Salida: No tiene
"""
def generar_combinaciones_serial():
	# Iteramos sobre todas las letras del abecedario
	for letra1 in vocales:
		for letra2 in vocales:
			for letra3 in abecedario:
				# Generamos la palabra
				palabra = letra1 + letra2 + letra3 # generamos la contraseña de tres letras, de tal manera que las dos
				# primeras letras sean vocales (y con ello solo tengamos que iterar sobre las 5 vocales en los bucles externos)
				# y la tercera letra sea cualquier letra del abecedario
				# Comparamos con la contraseña correcta
				if comparar_con_password_correcto(palabra):
					print(f'La contraseña es: {palabra}')
					return # Terminamos la ejecución de la función si es que encontramos la contraseña correcta
				
# Necesitamos una bandera global que nos permita avisar entre los distintos procesos si es que ya encontramos la contraseña correcta
# para que no continúen ejecutándose si es que esto ya se dio, y realmente la implementación paralela sea más rápida que la serial
contrasena_encontrada = False
"""
Función que sirve para implementar de manera paralelizada el método de fuerza bruta para encontrar la contraseña correcta
Esta función es la que usaremos como target en cada uno de los 5 procesos que crearemos en el hilo principal. Cada uno de estos
tomará como argumento de entrada una de las 5 vocales y la asumirá como la primera letra de la contraseña, por lo que solo
Entrada: vocal (string) - vocal que asumiremos como la primera letra de la contraseña
Salida: No tiene
"""
def generar_combinaciones_parallel(vocal):
	# Iteramos sobre todas las letras del abecedario
	global contrasena_encontrada
	if not contrasena_encontrada:
		for letra2 in vocales:
			for letra3 in abecedario:
				# Generamos la palabra
				palabra = vocal + letra2 + letra3 # generamos la contraseña de tres letras, de tal manera que las dos
				# primeras letras sean vocales y la primera sea la vocal que es input de la función target del proceso en ejecución
				# (y con ello solo tengamos que iterar sobre las 5 vocales en el bucle externo) y la tercera letra sea cualquier 
				# letra del abecedario
				# Comparamos con la contraseña correcta
				if comparar_con_password_correcto(palabra):
					print(f'La contraseña es: {palabra}')
					contrasena_encontrada = True
					return # Terminamos la ejecución de la función si es que encontramos la contraseña correcta
	else:
		return

if __name__ == "__main__":
	#Empezamos por ejecutar el método serial y medir su tiempo de ejecución
	tic_serial = time.perf_counter()
	generar_combinaciones_serial()
	toc_serial = time.perf_counter()
	print(f'El tiempo de ejecución del método serial es: {toc_serial - tic_serial} segundos')

	# Ahora ejecutamos el método paralelizado y medimos su tiempo de ejecución:
	# Empezamos por generar los 5 procesos usando una list comprehension para crear los iterables
	# que le pasaremos a la función Pool.map()
	tic_parallel = time.perf_counter()
	p = Pool(5) # Creamos el pool de 5 processes
	p.map(generar_combinaciones_parallel, vocales) # Ejecutamos la función target en cada uno de los procesos, para cada una de las 5 vocales
	# guardadas en la lista 'vocales' usando el método .map() del pool de processes
	# Cerramos el pool de processes y esperamos a que terminen de ejecutarse todos los procesos:
	p.close()
	p.join()
	toc_parallel = time.perf_counter()
	print(f'El tiempo de ejecución del método paralelizado es: {toc_parallel - tic_parallel} segundos')

	# Ahora comparamos los tiempos de ejecución calculando el speedup:
	speedup = (toc_serial - tic_serial) / (toc_parallel - tic_parallel)
	print(f'El speedup obtenido es: {speedup}')
