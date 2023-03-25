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

chmod a-rwx hola.c #primero el grupo y luego +-= los permisos 
chmod a-rwx hola
ls -l

#necesita leerlo para generar el ejecutable el gcc
# sin leer elk usuiorio no puede verlo
#sin editar es que no puede modificarlo incluyendo comandos como echo
#sin ejecutar no podra correrlo como escribir ni comandos como bash oc .\ o el tree mkdir
