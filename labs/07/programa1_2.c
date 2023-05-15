
#include <stdio.h>
#include <time.h>

int main()
{
    int N = 512;
    int matriz[N][N];
    int transpuesta[N][N];

    struct timespec ti, tf;
    double elapsed;

    for (int i = 0; i<N; i++){
        for(int j = 0; j<N;j++){
            matriz[i][j] = i+j*N;
        }
    }
    
    clock_gettime(CLOCK_REALTIME, &ti);
    for (int i = 0; i<N; i++){
        for(int j = 0; j<N;j++){
            transpuesta[j][i] = matriz[i][j];
        }
    }
    clock_gettime(CLOCK_REALTIME, &tf);
    elapsed = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("El tiempo en milisegundos que toma la función en C es %.2lf\n", elapsed*1e-6);
    
    return 0;
}
