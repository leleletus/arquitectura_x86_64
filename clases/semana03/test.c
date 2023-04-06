
#include <x86intrin.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int* crear_arr(int N){
    int* v = (int*)malloc(sizeof(int)*N);
    for(int i = 0; i < N; i++){
        v[i] = rand() % 9;
    }
    return v;    
}

void fill_arr(int* v, int N){
    for(int i = 0; i < N; i++){
        v[i] = rand() % 9;
    }
}


void vec_sum(int* a, int* b, int* c, int N){
    for(int i = 0; i < N; i++){
        c[i] = a[i] + b[i];
    }
}

int calc_num_instr(int N){
    return 7*N+5;
}

double calcular_CPI(long int num_cic, int num_inst){
    return (double)num_cic / (double)num_inst;
}

int main(){
    
    srand(time(NULL));

    int N = 8;

    int* a = crear_arr(N);
    int* b = crear_arr(N);
    int* c = crear_arr(N);

    long int tic, toc, ciclos;

    tic = __rdtsc();
    vec_sum(a, b, c, N);
    toc = __rdtsc();

    ciclos = toc - tic;

    int num_instr = calc_num_instr(N);

    double CPI = calcular_CPI(ciclos, num_instr);

    printf("#instrucciones:%d\n", num_instr);
    printf("ciclos:%ld\n", ciclos);
    printf("CPI:%lf\n",CPI);

    return 0;
}

