#!/bin/bash

#Compilación en C ##deben ir pegados los = !!!!!
gcc producto.c -o producto

#Ejecución en C
./producto $1 $2 #ejecuto con los argumentos ingresados al bash

#Compilación y ejecución en Python3
python3 producto.py $1 $2
