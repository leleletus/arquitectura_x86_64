#include<math.h>

extern float asmFloatNormTwo(float *v1, int N);

float cFloatNormTwo(float *v1, int N) {
	int i = 0;
    float n2;
	float sum = 0;
	for(i = 0; i < N; i++) {
		sum += v1[i] * v1[i]; //sumo los cuadrados de cada valor del vector
	}
	n2 = sqrtf(sum);
    //guardo en la posicion de memoria del puntero a n2 el cuadrado de la suma

    return n2;
}



//tenemos que generar con gcc el sahred object file

//gcc -fPIC -shared libreria_norma_2.c asmFloatNormTwo.o -o libreria_normal_2.so -lm