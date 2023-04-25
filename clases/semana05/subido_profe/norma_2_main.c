#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern float asmFloatNormTwo(float *v1, int N);
float cFloatNormTwo(float *v1, int N);

int main() {

	float *v1, n2C, n2Asm;
	int N = 1024;

	v1 = malloc(N * sizeof(float));

	int i = 0;

	for(i = 0; i < N; i++){
		v1[i] = (float)i;
	}

	n2C = cFloatNormTwo(v1, N);
	
	n2Asm = asmFloatNormTwo(v1, N);

	printf("%f\n%f\n",n2C,n2Asm);

        free(v1);

	return 0;
};

float cFloatNormTwo(float *v1, int N) {
	int i = 0;
    float n2;
	float sum = 0;
	for(i = 0; i < N; i++) {
		sum += v1[i] * v1[i];
	}
	n2 = sqrtf(sum);
}