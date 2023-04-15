
#include <x86intrin.h> // para pider usar __rdtsc(); y ver los ciclos
#include <stdio.h> // 
#include <stdlib.h> // incluimos las librerias estandars y math para operaciones
#include <math.h>  // para usarla al compilar debemos utilizar -lm
#include <time.h> // para utilizar el tiempo como una semilla

int Crear_rand_num(void){
    int c;
    c= rand()%(9 +1); //sacamos un numero del 0 al 9 utilizando residuo
    return c;
}

int suma(int a, int b){ //funcion que suma 2 numeros
    int c; //c es el resultado
    c=a+b;
    return c; //retorna el resultado obtenido
}

int resta(int a, int b){ // resta 2 numeros enteros, el primero menos el 2do
    int c; //c es el resultado
    c=a-b;
    return c; //retorna el resultado obtenido
}

int prod(int a, int b){// multiplica 2 numeros enteros
    //al ser en int no debe superar la multiplicacion el valor de 2147483647
    int c; //c es el resultado
    c=a*b;
    return c; //retorna el resultado obtenido
}

int num_instrucciones(int arg){
    int c;
    switch (arg){
        case 1: //cuando se quiere saber el #inst de la suma
            c=3; //si fuera una iteracion podria utilizarse el a*n+b para saber cuantas instrucciones en base del valor del n 
            break;
        case 2: //cuando se quiere saber el #inst de la resta
            c=4; 
            break;
        case 3: //cuando se quiere saber el #inst del prod
            c=4; 
            break;

        default: //en caso ingresar otro valor
            c=0; //c valdria 0
            break;
    }

    return c;
}

double calcular_CPI(long int num_cic, int num_inst){ //solo recibe la cantidad de ciclos e instrucciones
    double c; //resultado
    c= (double)num_cic / (double)num_inst; //usamos la formula
    return c; //usamos la formula
}

double calcular_MIPS(long int freq,long int cpi){ 
    double c; //resultado
    c= (double)(freq)/(double)(cpi); //al considerar f en Mhz no se necesita divider por 1M
    return c; //usamos la formula
}

double calcular_mediana(long int* v, long int terminos){ //si ingresa un arreglo 
    double resultado; //resultado
    
    //ordenamos el arreglo con bubble sort
    long int c, d, t;
    for (c = 0 ; c < ( terminos - 1 ); ++c){
        for (d = 0 ; d < terminos - c - 1; ++d){
            if (v[d] > v[d+1]){
                t = v[d];
                v[d]   = v[d+1];
                v[d+1] = t;
            }
        }
    }

    if(terminos %2 ==0){ //es par
        resultado=(double)(v[terminos/2]+ v[terminos/2-1])/2.0; //media aritmetica de los del centro
    }else{ // es impar
        resultado= v[(terminos-1)/2]; //devolvemos el termino central
    }
    return resultado; //usamos la formula
}

void test(int (*f)(int, int),int cant,char nombre[]){ // entra la funcion a probar la cantidad y el nombre
    //fui lento y me falto terminar por eso :c
    //falta ordenar bien y condicionales para verificar e imprimir


    long int tic = __rdtsc(); //limite inicial del tiempo
    //aqui la funcion para calcular los ciclos que tarda
    long int toc = __rdtsc(); //limite final del tiempo
    long int ciclos = toc - tic; //calculamos los ciclos de ejecucion de la funcion

    int num_instr = num_instrucciones(cant); //donde segun el numero que nos dan vemos las instrucciones que tiene con nuestra funcion

    double CPI = calcular_CPI(ciclos, num_instr); // calculamos el cpi

    int freq;
    double MIPS = calcular_MIPS(long int freq,long int CPI);
    double Mediana =

    printf("%d\n", Crear_rand_num()); //para visualizar el numero generado

    printf("#instrucciones:%d\n", num_instr);
    printf("ciclos:%ld\n", ciclos);
    printf("CPI:%lf\n",CPI);
    printf("MIPS:%lf\n",MIPS);
    printf("mediana:%lf\n",mediana);


}


int main(void){
    srand(time(NULL)); //semilla del time null 
    
    // probando correctamente
    test(suma(a,b),1,"suma");
    test(resta(a,b),2,"resta");
    test(prod(a,b),3,"prod");
    
    //pruebas malas
    test(suma(a,b),1,"resta");
    test(resta(a,b),1,"resta");
    test(prod(a,b),0,"hola");

    return 0;
}

