#include <stdio.h>
#include <stdlib.h>
// SI USAMOS math.h usar -lm en el compilador

void ini_vector(float *vec, int N);
void suma_compleja(float *real, float *imag, float *suma_real, float *suma_imag, int N);

int main()
{
    int N = 4;
    float *real = (float *)malloc(N * sizeof(float)); // creo un puntero que haga referencia a la parte real
    float *img = (float *)malloc(N * sizeof(float));

    ini_vector(real, N);
    ini_vector(img, N);

    float suma_real = 0;
    float suma_imag = 0;

    suma_compleja(real, img, &suma_real, &suma_imag, N);
    printf("El resultado es: %.2f + %.2fi\n", suma_real, suma_imag);

    return 0;
}

void ini_vector(float *vec, int N)
{
    for (int i = 0; i < N; i++)
    {
        vec[i] = i + 1;
    }
}

void suma_compleja(float *real, float *imag, float *suma_real, float *suma_imag, int N)
{ // o corchetes vacios en vez de puntero *
    // acumulador

    for (int i = 0; i < N; i++)
    {
        suma_real[0] = suma_real[0] + real[i];
        suma_imag[0] = suma_imag[0] + imag[i]; // los devuelvo como puntero asi que actualizo el valor
    }
}

void multiplicacion_compleja(){ // depurar con gbb?

}