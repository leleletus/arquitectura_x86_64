

#include <stdio.h>
#include <stdlib.h>
extern int funcion_asm(float *L, int N, int *output, int terms);

int funcion_c(float *L, int N, int *output,int terms){
    int cantidad=0; //cuantos multiplos y/o divisores tiene
    float temp;
    
    for (int i=0; i<terms; i++){
        if( ((int)(L[i]) % (N)) == 0  ||  ((N) % (int)L[i] == 0)){
            cantidad+=1;
            output[i]=1;
        }else{
            output[i]=0;
        }

        //printf("%d ",output[i]);
    }

    return cantidad;
}
