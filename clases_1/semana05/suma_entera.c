#include <stdio.h>
#include <stdlib.h>

extern int suma_int (int a, int b); //para que sea externa
// se creo y definio en otro lado (en este caso en el assembly)

int main(){
    int a=10;
    int b=100;
    int c;

    c=suma_int(a,b);

    printf("%d\n",c);
    
}