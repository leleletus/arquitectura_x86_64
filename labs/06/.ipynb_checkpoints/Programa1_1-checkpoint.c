#include <stdio.h>

#define N 1000000

int main() {
  int sum = 0;
  int array[N];

  // Initialize the array
  for (int i = 0; i < N; i++) {
    array[i] = i;
  }

  // Calculate the sum of the array
  for (int i = 0; i < N; i++) {
    sum += array[i];
  }

  // Print the sum
  printf("Sum: %d\n", sum);

  return 0;
}

