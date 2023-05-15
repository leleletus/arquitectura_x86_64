

#include <stdio.h>

double media_armonica_ponderada(int xn[], int xp[], int n) { //lo mismo que usar *xn y *xp ya que son punteros a los arreglos
    int M = 0;
    for (int i = 0; i < n; i++) {
        M += xp[i]; //calculamos la suma de todos los pesos en M
    }
    double suma_inversas = 0;
    for (int i = 0; i < n; i++) {
        suma_inversas += (double)xp[i] / xn[i]; //calculamos la usma de tosas las fracciones m/suma_inversas
    }
    return M / suma_inversas; //devolvemos resultado
}

int main() {
    // Ejemplo de uso
    int xn[] = {5, 4, 8, 9};
    int xp[] = {1, 5, 10, 20};
    int n = sizeof(xn) / sizeof(xn[0]); //calculamos la cantidad de terminos n
    double resultado = media_armonica_ponderada(xn, xp, n); //pasamos los datos a la funcion
    printf("La media armónica ponderada es: %.2f\n", resultado);
    
    return 0;
}
