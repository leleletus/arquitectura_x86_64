#!/bin/bash

input=$1

CENTINELA=0 #Variable para verificar si se ingreso un argumento en el terminal

start=`date +%s%N` #Variable de inicio para el calculo del tiempo

for((e = 1; e<=input ; e++))
do
  CENTINELA=1

done  


if [[ CENTINELA -eq 0 ]] #Condicional para verificar si se ingreso una variable de entrada en el terminal
then

  echo "[*] Debe ingresar un argumento"

else
  
  mkdir Laboratorio1
  chmod 700 Laboratorio1
  for((i = 1; i<=input ; i++)) #Uso de la sentencia iterativa "for" para la creacion de carpetas segun el argumento de entrada

  do 

    mkdir Laboratorio1/Carpeta"$i"
    mkdir Laboratorio1/Carpeta"$i"/Carpeta"$i".txt
    chmod 700 Laboratorio1/Carpeta"$i"
    echo ''Hola Carpeta"$i"''>> Carpeta"$i".txt #El contenido de las carpetas sera: Hola Carpeta"numero"
                                              
  done     

fi

end=`date +%s%N` #Variable de finalizacion para el calculo del tiempo

tiempo=$(($end-$start)) #Calculo del tiempo de ejecucion en nanosegundos
                        #Pagina de referencia: https://yvoictra.com/2008/01/31/calcular-tiempo-de-ejecucion-de-un-comando-en-bash-shell/

echo "El tiempo en nanosegundos es $tiempo"
