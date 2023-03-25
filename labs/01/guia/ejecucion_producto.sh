#!/bin/bash
input1=$1 #pasamos el primer argumento a la variable
input2=$2

#Compilación en C ##deben ir pegados los = !!!!!
CC=gcc 
EXEC=producto
SRC=producto.c
$CC $SRC -o $EXEC #podemos hacerlo directo o llamando "variables" gcc producto.c -o producto

#Ejecución en C
Ejecucion=./$EXEC
$Ejecucion $input1 $input2 #ejecuta el compilado con los argumentos dados

#Compilación y ejecución en Python3
EXECPy=python3
SRCPy=producto.py
$EXECPy $SRCPy $input1 $input2 #ejecutamos el python