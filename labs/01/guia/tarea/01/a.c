#include <stdio.h>
#include <stdlib.h>

int main(int argc,char const *argv[]) {

     if(argc !=3){ // analiza si se agregaron 2 argumentos (1+ 2)
        printf("Se ingreso una cantidad incorrecta de valores\n");
        exit(1);// termina el programa con codigo de error
    }

    int a= atoi(argv[1]);
    int b= atoi(argv[2]);

    double suma = 0;
    for (int i = a; i <= b; i++) {//empezamos desde el numero al ultimo
        suma += 1.0 / i; //sumamos las inversas de los numeros
    }
    double mediaArmonica = (b - a + 1) / suma; //sacamos el numero de terminos con final menos inicial +1 menos razon
    //y lo dividimos entre la suma

    printf("La media armonica de los nummeros desde %d hasta %d es: %.2f\n", a, b, mediaArmonica);//vemos solo los 2 primeros decimales
    return 0; // correcta finalizacion
}