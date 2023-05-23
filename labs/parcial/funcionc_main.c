

#include <stdio.h>
#include <stdlib.h>
extern int funcion_asm(float *L, int N, int *output, int terms);
int funcion_c(float *L, int N, int *output, int terms);

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

    printf("\nutilizando la funcion en asm:");
    cantidad=funcion_asm(L,N,output,nterms);
    printf("%d\n",cantidad);

    for (int i=0;i<nterms;i++){
        printf("%d ",output[i]);
    }

    return 0;
}



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
