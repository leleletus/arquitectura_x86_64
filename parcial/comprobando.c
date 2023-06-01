
#include <stdio.h>
#include <stdlib.h>
#include "libreria.c"

extern int funcion_c(float *L, int N, int *output,int terms);

int main(void){

    float L[] = {4, 10, 8, 35.3, 19, -5, 2, 32};
    int N=4;

    
    int nterms=sizeof(L)/sizeof(L[0]);
    int *output = (int*)malloc(nterms * sizeof(int));
    

    int cantidad;
    cantidad=funcion_c(L,N,output,nterms);
    printf("%d\n",cantidad);

    for (int i=0;i<nterms;i++){
        printf("%d ",output[i]);
    }

    return 0;
}


