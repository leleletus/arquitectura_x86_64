

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

//int 32 bits , float 32 bits
int cont_parej_cuad_perf(int *v, int tam,int **x,int **y  ){
    int q=0; //cantidad

    //creando un bubble sort
    for(int i=0;i<tam-1;++i){
        for(int j=0;j<tam-i-j;++j){
            if (v[j] > v[j + 1]){
                int temp = v[j];
                v[j] = v[j+1];
                v[j+1] = temp;
            }
        }
    }

    
    for(int i=0; i<tam-1;i++){
        for(int j=i+1;j<tam;j++){
            if ( (v[i]>=0 && v[i]<=9) && (v[j]>=0 && v[j]<=9) ){
                float raiz= sqrt((float)(v[i] * v[j]));
                if( raiz % 1) ==0  ){ //residuo de un float no es posible
                    q+=1;
                }
            }
        }
    }
    
    return q;
}



//gcc cont_parej_cuad_perf.c -o cont_parej_cuad_perf -lm && ./cont_parej_cuad_perf