#include <stdio.h>
#include <stdlib.h>

extern float suma_float (float a, float b); //para que sea externa
// se creo y definio en otro lado (en este caso en el assembly)

int main(){
    float a=10.5;
    float b=100.5465;
    float c;

    c=suma_float(a,b);

    printf("%f\n",c);
    
}