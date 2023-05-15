
//creando un archivo .c
//lo mas recomendado es editarlo directamente
#include <stdio.h> //libreria basica

int main(int argc, char *argv[]){
    printf("Hola mundo\r\n");

    //calculando el tamaño de cada tipo
    printf("El tamaño de un short es: %zu bytes\n", sizeof(short));
    printf("El tamaño de un int es: %zu bytes\n", sizeof(int));
    printf("El tamaño de un float es: %zu bytes\n", sizeof(float));
    printf("El tamaño de un long es: %zu bytes\n", sizeof(long));
    printf("El tamaño de un double es: %zu bytes\n", sizeof(double));
    

    return 0;
}
