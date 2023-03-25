#!/bin/sh

# crea programa en c
echo "#include <stdio.h>
#include <stdlib.h>
int main(void){
    printf(\"Hola amigos del curso de arqui\n\");
    return 0;
}
" >> hola.c # el \" para que se muestre en el echo

#ejecuta compila y ejecuta en c
gcc hola.c -o hola && ./hola
#para ver permisos
