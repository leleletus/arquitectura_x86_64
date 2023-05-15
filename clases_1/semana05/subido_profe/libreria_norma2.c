#include <math.h>
extern float asmFloatNormTwo(float *v1, int N);
float cFloatNormTwo(float *v1, int N) {
	int i = 0;
    float n2;
	float sum = 0;
	for(i = 0; i < N; i++) {
		sum += v1[i] * v1[i];
	}
	n2 = sqrtf(sum);
}