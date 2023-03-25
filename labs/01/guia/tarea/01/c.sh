#!/bin/bash

#Compilación en C ##deben ir pegados los = !!!!!
echo "Tiempo en c"
time gcc a.c -o a && ./a $1 $2

#Compilación y ejecución en Python3
echo "Tiempo en python3"
time python3 b.py $1 $2