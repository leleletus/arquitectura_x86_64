#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import datetime
from threading import Thread
import socket
import struct
import time

servidores_ntp = [
	"0.uk.pool.ntp.org",
	"1.es.pool.ntp.org",
	"0.br.pool.ntp.org",
	"2.cl.pool.ntp.org",
	"2.co.pool.ntp.org",
	"0.hk.pool.ntp.org",
	"0.sg.pool.ntp.org",
	"0.jp.pool.ntp.org",
	"0.au.pool.ntp.org",
	"0.nz.pool.ntp.org",
	"0.za.pool.ntp.org",
	"0.fr.pool.ntp.org",
	"0.in.pool.ntp.org",
	"0.tw.pool.ntp.org"
]

"""
Función: get_ntp_time
Descripción: Imprime la hora actual en un país determinado
Entrada: Cualquiera de las URLs definidas en la lista servidores_ntp
Salida: Ninguna, solo imprime la hora 
"""
def get_ntp_time(host):
	timezone_dict = {'uk': ['UK', 6 * 3600], 'es': ['España', 7 * 3600], 'br': ['Brazil', 2 * 3600],
	                 'cl': ['Chile', 1 * 3600], 'co': ['Colombia', 0], 'hk': ['Hong Kong', 13 * 3600],
	                 'sg': ['Singapur', 13 * 3600], 'jp': ['Japón', 14 * 3600], 'au': ['Australia', 15 * 3600],
	                 'nz': ['Nueva Zelanda', 17 * 3600], 'za': ['Sudáfrica', 7 * 3600], 'fr': ['Francia', 7 * 3600],
	                 'in': ['India', 10.5 * 3600], 'tw': ['Taiwan', 13 * 3600]}
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
	print(f"Hora en {timezone_dict[key][0]}: {datetime.datetime.fromtimestamp(t + timezone_dict[key][1])}")

#Pregunta a:
def horas_serie (servidores_ntp):
    for i in range(len(servidores_ntp)):
        get_ntp_time(servidores_ntp[i])

#Pregunta b:
def horas_paralelo(elemento_lista):
    get_ntp_time(elemento_lista)    

if __name__ == '__main__':

	# Escriba aquí su código para la parte a
    a1 = time.perf_counter()
    horas_serie(servidores_ntp)
    a2 = time.perf_counter()

    t_serie = a2 - a1
    
    print("     ")
    print(f"Tiempo de ejecucion en serie : {t_serie:0.2f} segundos ")
    print("     ")

	# Escriba aquí su código para la parte b (puede hacerlo en un archivo separado también, ambas opciones son válidas)
    a3 = time.perf_counter()
    t1 = Thread(target=horas_paralelo, args=(servidores_ntp[0],))
    t2 = Thread(target=horas_paralelo, args=(servidores_ntp[1],))
    t3 = Thread(target=horas_paralelo, args=(servidores_ntp[2],))
    t4 = Thread(target=horas_paralelo, args=(servidores_ntp[3],))
    t5 = Thread(target=horas_paralelo, args=(servidores_ntp[4],))
    t6 = Thread(target=horas_paralelo, args=(servidores_ntp[5],))
    t7 = Thread(target=horas_paralelo, args=(servidores_ntp[6],))
    t8 = Thread(target=horas_paralelo, args=(servidores_ntp[7],))
    t9 = Thread(target=horas_paralelo, args=(servidores_ntp[8],))
    t10 = Thread(target=horas_paralelo, args=(servidores_ntp[9],))
    t11 = Thread(target=horas_paralelo, args=(servidores_ntp[10],))
    t12 = Thread(target=horas_paralelo, args=(servidores_ntp[11],))
    t13 = Thread(target=horas_paralelo, args=(servidores_ntp[12],))
    t14 = Thread(target=horas_paralelo, args=(servidores_ntp[13],))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start() 
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start() 
    t12.start()
    t13.start() 
    t14.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    a4 = time.perf_counter()

    t_paralelo = a4 - a3

    print("     ")
    print(f"Tiempo de ejecucion en paralelo : {t_paralelo:0.2f} segundos ")