
#include <stdio.h>
#include <time.h> //para tomar mediciones del tiempo

#define N 1000000

int main() {
  int sum = 0;
  int array[N];

  // Initialize the array
  for (int i = 0; i < N; i++) {
    array[i] = i;
  }
    
  struct timespec ti, tf;
  double elapsed;

  clock_gettime(CLOCK_REALTIME, &ti);
  // Calculate the sum of the array
  for (int i = 0; i < N; i++) {
    sum += array[i];
  }
  clock_gettime(CLOCK_REALTIME, &tf);
  
  elapsed = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("el tiempo en mili que toma la función en C es %.2lf\n", elapsed*1e-6);
  

  // Print the sum
  printf("Sum: %d\n", sum);

  return 0;
}

