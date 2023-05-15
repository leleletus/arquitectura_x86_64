
#include <stdio.h>
#include <stdlib.h>
#include <math.h> //agregamos -lm para que el compilador incluya la libreria

int calcula_primos(int lim_inf, int lim_sup); // invocamos al inicio las funciones creadas
int calcula_potencias(int lim_inf, int lim_sup, int base);


int main(int argc, char *argv[]) { //pasamos los argumentos ingresados
    if (argc != 4) {// compr0bamos que sean 3 argumentos ingresados + el nombre 
        printf("Debe ingresar 3 argumentos de entrada\n"); // de no ingresarse los 3 argumentos mostrar el mensaje de error
        exit(1);
    } else {
        int lim_inf = atoi(argv[1]); //convertimos los argumentos de ascii a entero y guardamos en variables
        int lim_sup = atoi(argv[2]);
        int opcion = atoi(argv[3]);

        if (opcion == 1) { // de ingresarse como opcion 1 , se calcula los numeros primos en ese rango
            printf("Hay %d numeros primos en este rango\n", calcula_primos(lim_inf, lim_sup)); 
        } else if (opcion >= 2) { // de ingresarse un valor mayor o igual a 2 se calcula la cantidad de potencias en ese rango del numero proporcionado
            printf("Hay %d potencias de %d en este rango\n", calcula_potencias(lim_inf, lim_sup, opcion), opcion);
        }
    }
    return 0; //finalizando correctamente su ejecucion retornamos 0 
}


int calcula_primos(int lim_inf, int lim_sup) { //funcion que calcula la cantida de primos
    int cantidad_primos = 0;
    for (int i = lim_inf; i <= lim_sup; i++) { // contamos desde el limite inferior al superior de 1 en 1
        int valida_primo = 0;
        if (i <= 1) { // si el numero es menor o igual de 1 no es primo ya que los primos son desde el 2 en adelante
            valida_primo = 0;
        } else { //de ser 2 o mayores entonces contamos cuantos son
            for (int j = 2; j <= i; j++) { // por cada valor i que existe en el rango , lo vamos a analizar si es un numero primo o no
                if (i % j == 0) { // comprobamos si es que todos los numeros menores o iguales a el son divisores  
                    valida_primo++;// cada que encontremos un divisor desde el 2 lo agregamos a esta variable
                }// como un primo solo tiene de divisores el mismo y el 1 y como empezamos desde el 2 solo debe tener 1 divisor
            }
        }
        if (valida_primo == 1) {// solo sera primo si es que tiene de divisor a el mismo a parte del 1, por eso si si valor es 1, es primo , si es mayor no seria
            cantidad_primos++; // ya que comprobamos que tenemos un primo vamos aumentando la cantidad de primos encontrados
        }
    }
    return cantidad_primos; //retornamos el valor
}

int calcula_potencias(int lim_inf, int lim_sup, int base) {
    int cantidad_potencias = 0;
    for (int i = 0; i <= lim_sup; i++) {// empezamos el indice desde 0 hasta el rango maximo
    //se podria dividir repetidasveces el numero entre la base para saber el maximo valor del indice pero se decidio a fuerza bruta
        int elevado = pow(base, i);// calculamos la potencia
        if (elevado <= lim_sup && elevado >= lim_inf) { //si la potencia se encuentra dentro del rango
            cantidad_potencias++;//aumenta la cantidad de potencias encontradas
        }
    }
    return cantidad_potencias; //retorna la cantidad encontrada
}
