#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern void matvecRMRV_asm(double *A, double *x, double *b, int N);
extern void matvecRMCV_asm(double *A, double *x, double *b, int N);
void matvecRMRV_c(double *A, double *x, double *b, int N)
{
    float tmp = 0.0;
    for(int i = 0; i < N; i++)
    {
        tmp = 0.0;
        for(int j = 0; j < N; j++)
        {
            tmp += A[i*N + j]*x[j];
        }
        b[i] = tmp;
    }
}

void matvecRMCV_c(double *A, double *x, double *b, int N)
{
    float tmp = 0.0;
    for(int j = 0; j < N; j++)
    {
        for(int i = 0; i < N; i++)
        {
            b[i] += A[i*N + j]*x[j];
        }
    }
}