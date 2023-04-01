#include <stdio.h>
#include <stdlib.h>

void modify_array(int **arr, int n) {
    for (int i = 0; i < n; i++) {
        (*arr)[i] = i;
    }
}


void resize_array_1(int **arr, int new_size) {
    int *temp = realloc(*arr, new_size * sizeof(int));
    if (temp == NULL) {
        printf("Error: No se pudo asignar memoria.\n");
        free(*arr);
        exit(1);
    }
    *arr = temp;
}

void resize_array_2(int **arr, int new_size) {
    *arr = realloc(*arr, new_size * sizeof(int));
    if (*arr == NULL) {
        printf("Error: No se pudo asignar memoria.\n");
        exit(1);
    }
}

int main() {
    int n = 10;
    int *arr = malloc(n * sizeof(int));

    // Cambiar el tamaño del arreglo a 20 elementos
    resize_array(&arr, 20);

    // Usar el arreglo ...

    free(arr);
    return 0;
}

int main() {
    int n = 10;
    int *arr = malloc(n * sizeof(int));

    // Modificar los valores en el arreglo
    modify_array(&arr, n);

    // Imprimir los valores en el arreglo
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    free(arr);
    return 0;
}