#include <stdio.h>
#include <stdlib.h>

int main(int argc,char const *argv[]) {

    int a= atoi(argv[1]);
    int primo=0;

    if(a<=1){
        primo=0; //los primos empiezan desde el 2
    }else{

        for(int i=2;i<=a;i++){ //empezara a ver los divisores del numero

        }
    }

    printf("El numero %d es primo");

    return 0; // correcta finalizacion
}