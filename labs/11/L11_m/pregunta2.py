

from socket import AF_INET, SOCK_DGRAM
import datetime
import threading
import socket
import struct
import time

servidores_ntp = [
	"0.uk.pool.ntp.org",    # Londres(Reino Unido)
	"1.es.pool.ntp.org",    # Madrid (España)
	"0.us.pool.ntp.org",    # Nueva York(Estados Unidos)
	"0.hk.pool.ntp.org",    # Hong Kong
	"0.jp.pool.ntp.org"     # Tokyo(Japón)
]

"""
Función: get_ntp_time
Descripción: Imprime la  fecha-hora actual en un país determinado
Entrada: Cualquiera de las URLs definidas en la lista servidores_ntp
Salida: Retorna la fecha-hora(timestamp) en formato datetime.datetime, también la imprime
IMPORTANTE: NO modifique esta funcion 
"""
def get_ntp_time(host):
	timezone_dict = {'uk': ['UK', 0 * 3600], 'es': ['España', 1 * 3600],
	                 'hk': ['Hong Kong', 8 * 3600], 'jp': ['Japón', 9 * 3600],
	                 'us': ['Estados Unidos', -5*3600]}
	key = ''
	port = 123
	buf = 1024
	address = (host, port)
	msg = b'\x1b' + 47 * b'\0'

	# reference time (in seconds since 1900-01-01 00:00:00)
	TIME1970 = 2208988800  # 1970-01-01 00:00:00
	# connect to server
	client = socket.socket(AF_INET, SOCK_DGRAM)
	client.sendto(msg, address)
	msg, address = client.recvfrom(buf)
	t = struct.unpack("!12I", msg)[10]
	t -= TIME1970
	client.close()

	for each_key in timezone_dict:
		if each_key in host:
			key = each_key
			break
	print(f"Hora en {timezone_dict[key][0]}: {datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])}")
	return datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])

# Escribimos la función que realiza el cálculo pedido para saber qué país es el que está más próximo a abrir
# su bolsa de valores de manera iterativa y secuencial
def calcular_mas_proximo_iterativo():
	# Obtenemos la hora actual en Perú
	hora_actual = datetime.datetime.now()
	# Inicializamos la variable que almacenará el país más próximo a abrir
	pais_mas_proximo = ''
	# Inicializamos la variable que almacenará la hora más próxima a las 8:00am
	hora_mas_proxima = datetime.datetime(2021, 1, 1, 8, 0, 0)
	# Iteramos sobre los servidores NTP
	for servidor in servidores_ntp:
		# Obtenemos la hora actual en el servidor NTP
		hora_servidor = get_ntp_time(servidor)
		# Calculamos la diferencia entre la hora actual en el servidor NTP y la hora actual en Perú
		diferencia = hora_servidor - hora_actual
		# Si la diferencia es negativa, significa que el servidor NTP está en un país que está más próximo a abrir
		# su bolsa de valores
		if diferencia < datetime.timedelta(0):
			# Si la diferencia es menor que la hora más próxima a las 8:00am, actualizamos la hora más próxima a las 8:00am
			# y el país más próximo a abrir
			if diferencia < hora_mas_proxima:
				hora_mas_proxima = diferencia
				pais_mas_proximo = servidor
	# Imprimimos el país más próximo a abrir
	print(f'El país más próximo a abrir su bolsa de valores es {pais_mas_proximo}')

# Escribimos la función que realiza el cálculo pedido para saber qué país es el que está más próximo a abrir
# su bolsa de valores de manera concurrente utilizando threads para cada uno de los elementos en la lista servidores_ntp
def calcular_mas_proximo_concurrente():
	# Obtenemos la hora actual en Perú
	hora_actual = datetime.datetime.now()
	# Inicializamos la variable que almacenará el país más próximo a abrir
	pais_mas_proximo = ''
	# Inicializamos la variable que almacenará la hora más próxima a las 8:00am
	hora_mas_proxima = datetime.datetime(2021, 1, 1, 8, 0, 0)
	# Inicializamos la lista que almacenará los threads
	threads = []
	# Iteramos sobre los servidores NTP
	for servidor in servidores_ntp:
		# Creamos el thread para el servidor NTP
		thread = threading.Thread(target=get_ntp_time, args=(servidor,))
		# Agregamos el thread a la lista de threads
		threads.append(thread)
	# Inicializamos la lista que almacenará los resultados de los threads
	resultados = []
	# Ejecutamos los threads
	for i in range(len(threads)):
		threads[i].start()
	# Esperamos a que terminen los threads y obtenemos el resultado de cada uno
	for i in range(len(threads)):
		resultado_actual = threads[i].join()
		resultados.append(resultado_actual)
	# Iteramos sobre los resultados de los threads
	for resultado in resultados:
		# Calculamos la diferencia entre la hora actual en el servidor NTP y la hora actual en Perú
		#print(resultado)
		#print(hora_actual)
		if resultado is None:
			continue
		else:
			diferencia = resultado - hora_actual
			# Si la diferencia es negativa, significa que el servidor NTP está en un país que está más próximo a abrir
			# su bolsa de valores
			if diferencia < datetime.timedelta(0):
				# Si la diferencia es menor que la hora más próxima a las 8:00am, actualizamos la hora más próxima a las 8:00am
				# y el país más próximo a abrir
				if diferencia < hora_mas_proxima:
					hora_mas_proxima = diferencia
					pais_mas_proximo = servidor
	# Imprimimos el país más próximo a abrir
	print(f'El país más próximo a abrir su bolsa de valores es {pais_mas_proximo}')
		
if __name__ == '__main__':
	# En la función principal mediremos el tiempo de ejecución de las funciones calcular_mas_proximo_iterativo 
	# y calcular_mas_proximo_concurrente y los compararemos para ver cuál es más eficiente. Usaremos el método
	# de la librería time: time.perfcounter()
	# Inicializamos el contador de tiempo para calcular_mas_proximo_iterativo
	inicio_iterativo = time.perf_counter()
	# Ejecutamos la función calcular_mas_proximo_iterativo
	calcular_mas_proximo_iterativo()
	# Finalizamos el contador de tiempo para calcular_mas_proximo_iterativo
	fin_iterativo = time.perf_counter()
	# Calculamos el tiempo total de ejecución de calcular_mas_proximo_iterativo
	tiempo_total_iterativo = fin_iterativo - inicio_iterativo
	# Inicializamos el contador de tiempo para calcular_mas_proximo_concurrente
	inicio_concurrente = time.perf_counter()
	# Ejecutamos la función calcular_mas_proximo_concurrente
	calcular_mas_proximo_concurrente()
	# Finalizamos el contador de tiempo para calcular_mas_proximo_concurrente
	fin_concurrente = time.perf_counter()
	# Calculamos el tiempo total de ejecución de calcular_mas_proximo_iterativo
	tiempo_total_concurrente = fin_concurrente - inicio_concurrente
	# Imprimimos los tiempos de ejecución de las funciones calcular_mas_proximo_iterativo y calcular_mas_proximo_concurrente
	print(f'El tiempo de ejecución de calcular_mas_proximo_iterativo es {tiempo_total_iterativo} segundos')
	print(f'El tiempo de ejecución de calcular_mas_proximo_concurrente es {tiempo_total_concurrente} segundos')
	# Comparamos estos tiempos e imprimimos en el terminal qué implementación fue más rápida:
	if tiempo_total_iterativo < tiempo_total_concurrente:
		print('La implementación iterativa fue más rápida')
	elif tiempo_total_iterativo > tiempo_total_concurrente:
		print('La implementación concurrente fue más rápida')

