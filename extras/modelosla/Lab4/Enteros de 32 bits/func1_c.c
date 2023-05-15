#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern void func1_asm(int *arr, int *suma, int *mul ,int N );
void func1_c(int *arr, int *suma, int *mul ,int N ){
   int acumulador = 0;
   int acumulador2 = 1;
   for(int i = 0; i < N; i=i+2){
       acumulador= acumulador + arr[i];
       acumulador2 = acumulador2*arr[i+1];
   }

   suma[0] = acumulador;
   mul[0] = acumulador2;

}