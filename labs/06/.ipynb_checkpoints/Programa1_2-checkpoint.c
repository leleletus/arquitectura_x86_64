#include <stdio.h>

#define N 1000000

int main() {
  int sum = 0;

  // Calculate the sum of the array
  for (int i = 0; i < N; i++) {
    sum += i;
  }

  // Print the sum
  printf("Sum: %d\n", sum);

  return 0;
}

