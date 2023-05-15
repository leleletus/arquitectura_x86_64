#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern void asmFloatNormTwo(float *v1, int N, float *n2);
void cFloatNormTwo(float *v1, int N, float *n2);

int main() {

	float *v1, n2C, n2Asm; //declaro mis variabnles y arreglo v1
	int N = 1024; //el numero de elementos

	v1 = malloc(N * sizeof(float)); //reservo espacio de memoria

	int i = 0;

	for(i = 0; i < N; i++){
		v1[i] = (float)i; //dando valores al valor v1
	}//le hago un cast a float para que los elementos guardados sean float
    //ya que mas adelante sacaque raiz cuadrada y multisplicacion

	cFloatNormTwo(v1, N, &n2C); //retorna la norma como puntero
    //tambien ponemos hacerlo apra quesalga en la variabble n2c
	 //le da el vector, numero de elementos y la diceccion de memoria

	asmFloatNormTwo(v1, N, &n2Asm);

	printf("%f\n%f\n",n2C,n2Asm);

        free(v1);

	return 0;
};

void cFloatNormTwo(float *v1, int N, float *n2) {
	int i = 0;
	float sum = 0;
	for(i = 0; i < N; i++) {
		sum += v1[i] * v1[i]; //sumo los cuadrados de cada valor del vector
	}
	n2[0] = sqrtf(sum);
    //guardo en la posicion de memoria del puntero a n2 el cuadrado de la suma
}

