
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) { //siempre igual si recibiremos argumentos
    // Verificar si se ingresó un argumento
    if (argc != 2) { //verificamos si ingreso 1 (el name (siempre fijo y primero + argumento))
        printf("Ingrese solo 1 numero\n" );
        return 0; //acabamos
    }

    // Convertir el argumento a un entero
    int n = atoi(argv[1]); //guardamos el argumento ingresado como numero entero (ascii to integer)
    int es_primo = 1; //1 es verdadero y 0 falso

    // Verificar si el número es primo
    if (n <= 1) {
        es_primo = 0; // numeros como el 1 o menores no son primos
    } else {
        for (int i = 2; i * i <= n; i++) { //desde el 2 puede ser primo
            if (n % i == 0) { //calculamos el cuadrado desde 2 hasta el numero y verificamos si tiene division perfecta
                es_primo = 0; //si lo tiene quiere decir que tiene un divisor aparte del 0 y si mismo
                break; //apenas encontramos 1 divisor sabemos que no sera primo y se acaba
            }
        }
    }

    // Imprimir el resultado
    if (es_primo) {
        printf("El número %d es primo\n", n);
    } else {
        printf("El número %d no es primo\n", n);
    }

    return 0;
}
