
#include <stdio.h>
#include <stdlib.h>

//L(entrada) arreglo de numeros a comparar
//N (entrada) el numero a analizar
//tam (entrada) cuantos numeros hay en el arreglo n
//arreglo_output(salida) vector que sale
//cantidad (salida) un entero de los numeros que salen
void funcion_c(int *L, int tam, int N, int *arreglo_output, int *cantidad) {
    *cantidad = 0; // inicializamos en 0
    for (int i = 0; i < tam; i++) { //iteramos en toda la extencion del arreglo
        if (L[i] % N == 0) { //pregunto si el numero en el arreglo es divisible (modulo 0)
            (*cantidad)++; 
            arreglo_output[i] = 1;
        } else if (N % L[i] == 0) {//pregunto si el numero es divisiple por uno de l
            (*cantidad)++;
            arreglo_output[i] = 1;
        } else { //en caso que no cumpla ninguno anterior
            arreglo_output[i] = 0; 
        }
    }
}

void main() {
    int L[] = {4, 10, 8, 35, 19, -5, 2, 32}; //arreglo de prueba
    int N = 4; //numero a evaluar sus div y mul
    int tam = sizeof(L) / sizeof(L[0]);
    int arreglo_output[tam]; // tendra el mismo tamaño que el de entrada
    int cantidad; //para saber la cantidad


    printf("Utilizando la funcion en c:\n");
    funcion_c(L, tam, N, arreglo_output, &cantidad); //llamamos a la funcion
    printf("arreglo_output = ["); //imprimimos el output
    for (int i = 0; i < tam; i++) {
        printf("%d", arreglo_output[i]);
        if (i < tam - 1) {
            printf(", ");
        }
    }
    printf("]\n");
    printf("cantidad = %d\n", cantidad); //imprimimos cantidad


}
