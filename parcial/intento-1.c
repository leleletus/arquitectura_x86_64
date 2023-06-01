

#include <stdio.h>
#include <stdlib.h>

extern double medArm(int* xn, int* xp);

double parcial_1_c (int* xn, int* xp){
    int p = 4;
    int M = 0;
    double H_den = 0.0;
    double H;
    for (int i = 0; i){
        M += xp[i];
        H_den += (double)(xp[i])/(double)(xn[i]);
    }   
    printf("%d",M);
    H = (double)(M)/H_den;
    return H;
}

int main(void){
    int arr1[4]={1,2,3,4};
    int arr2[4]={3,4,8,5};
    printf("resultado en C: %f\n",parcial_1_c(arr1,arr2));
    printf("resultado en ASM: %f\n",medArm(arr1,arr2));
}
