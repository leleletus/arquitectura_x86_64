#!/bin/sh

# a) el parametro que recibe que debe ser el codigo lo muestra
echo "Diego Josué Vera Moreno $1" 


#b) creamos los directorios
mkdir Pregunta1
mkdir Pregunta2
#cambiamos los permisos a rwx a todos
chmod 777 Pregunta1
chmod 777 Pregunta2


#c) copiamos todos los archivos de la pregunta 1 y 2
cp pregunta1.c Pregunta1 #copiamos el c al directorio
cp pregunta2.py Pregunta2 #copiamos tambien el py


#para generar el codigo del programa2.py en el directorio Pregunta 2 se usaria: 
#echo "aqui iria todo el codigo " >> Pregunta2/pregunta2.py
#solo que cada que se usen comillas dentro del codigo de python
#se deberia agregar \ antes de estas para que echo sepa que queremos
#escribir el caracter comilas


#d) generar el ejecutable de la pregunta 1 en el directorio Pregunta1
gcc pregunta1.c -lm -o Pregunta1/pregunta1  # -lm para usar la libreria math.h

#e) ejecutamos el programa con 1 100 4 en c con time
time ./Pregunta1/pregunta1 1 100 4

#f)ejecutamos el programa en python con 1 100 4 con time
time python3 Pregunta2/pregunta2.py 1 100 4

# se agrego los condicionales a los mismos archivos a menos que se deba
#en bash agregar que seria 
#if $# != 3; then echo "Debe ingresar 3 argumentos de entrada"