#include <stdio.h>
#include <stdlib.h>
//SI USAMOS math.h usar -lm en el compilador

int suma(int x, int y);//prototipo de mi funcion

int main(int argc, char **argv){
    int x=10;
    int y=20;
    int z;
    z=suma(x,y);
    printf("Progama de prueba de direcciones de memoria\n");
    printf("--------------------------------------\n"); //el argc es la cantidad de argumentos
    printf("argc esta en %p\n",&argc); //a la variable el & para ver su direccion no su contenido
    printf("argv esta en %p\n",&argv); //con p te da en hexadecimales
    printf("--------------------------------------\n");
    printf("argv apunta ea %p\n",argv); //el argv0 es el nombre del archivo
    printf("argv[0] contiene a %s\n",argv[0]); //s de string para ver cadena de texto
    printf("--------------------------------------\n");
    printf("x esta en %p\n",&x);
    printf("y esta en %p\n",&y);
    printf("z esta en %p\n",&z);
}


int suma(int x,int y){

    return x+y;
}

//
//x esta en 0x7fff0cd1784c
//y esta en 0x7fff0cd17850
//z esta en 0x7fff0cd17854

// en este caso x ocupa 0x7fff0cd178  4c, 4d, 4e, 4f (4 bytes ya que es de 4 int)
// en este caso x ocupa 0x7fff0cd178  50, 51, 52, 53 
// en este caso x ocupa 0x7fff0cd178  54, 55, 56, 57

