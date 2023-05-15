#include <stdio.h>
#include <stdlib.h>
#include <math.h>
extern void func2_asm(float *arr, float *suma, float *mul ,int N );
void func2_c(float *arr, float *suma, float *mul ,int N ){
   float acumulador = 0.0;
   float acumulador2 = 1.0;
   for(int i = 0; i < N; i=i+2){
       acumulador= acumulador + arr[i];
       acumulador2 = acumulador2*arr[i+1];
   }

   suma[0] = acumulador;
   mul[0] = acumulador2;

}