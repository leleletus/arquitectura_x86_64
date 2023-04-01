
#include <stdio.h>
#include <stdlib.h>
#include <math.h> 

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

//para poder utilizar unicamente una funcion debemos hacer pequeños cambios en las 3 funciones anterirormente creadas
double pi_cuarto_for(int cant_terms, double* terms){ //definimos nuestra funcion en double ya que es con decimales //agregamos como parametro un puntero/arreglo
    double s = 0.0; //la serie es en decimales y se inicializa con 0.0 para que continue igual
    double term=0.0;
    int signo=0;
    int i;
  
    for (i=0;i<cant_terms;i++){

        if(i % 2 ){
            signo=-1;
        }else{
            signo=1;
        }

    term = signo*(1.0/(2*i+1));
    //printf("%lf ",term); //para ver los valores conseguidos
    s +=term; //acumulamos la suma de la serie

    terms[i]=s; // guardamos en este la serie por cada uno de sus terminos
    }

    return s;
}


double pi_cuarto_while_1(double ref,double tol, double** terms,int* n_terms){ //utilizamos puntero a un puntero para modificar el bloque de memoria reservado
                                                                             //tambien pasamos como parametro el numero de terminos cuando acaba la funcion para saber cuantos tiene el arreglo
    double s = 0.0; //la serie es en decimales y se inicializa con 0.0 para que continue igual
    double term=0.0;
    double eps=0.0;
    int signo=0;
    int i=0;

    while(1){

        if(i % 2 ){
            signo=-1;
        }else{
            signo=1;
        }
        term = signo*(1.0/(2*i+1));
        s +=term;

        *terms = realloc(*terms, (i+1) * sizeof(double)); //realloc para que vaya aumentando conforme aumenta el i
        //ya que el i empieza en 0 se utiliza (i+1) terminos 
        (*terms)[i] = s; //guardamos en nuestro puntero del main

        eps = fabs(ref - s) / ref;

        i+=1; // alcualizamos la cuenta

        if(eps < tol){ // en caso que el epsilo es igual o supero la tolerancia acaba
            break;
        }

        
    }
    *n_terms=i;// sacamos la cantidad de terminos que hay a la variable del main
    return s;
}



double pi_cuarto_while_2(double tol, double** terms,int* n_terms){ //analogamente a la funcion anterior agregamos puntero de puntero y puntero para los terminos
                                                                  //con la finalidad de modificar directamente los del main y actualizar sus valores
    double s = 0.0; //la serie es en decimales y se inicializa con 0.0 para que continue igual
    double term=0.0;
    double eps=1.0;
    double s_ant=0.0;
    int signo=0;
    int i=0;

    while(1){

        if(i % 2 ){
            signo=-1;
        }else{
            signo=1;
        }
        term = signo*(1.0/(2*i+1));
        s +=term;

        *terms = realloc(*terms, (i+1) * sizeof(double)); //nuevamente utilizamos  el ralloc con un puntero al puntero para modificar directamente del main
        (*terms)[i] = s;
        //printf("%.16lf\n",terms[i]); // para comprobar loss terminos de igual longitud que en python

        if(i>0){ // en primer termino i=0 eps =1 no se actualiza
            eps = fabs(s_ant - s) / s_ant;
        }
    
        s_ant = s;
        i+=1;

        if(eps < tol){ //cuando finaliza
            break;
        }

    }
    *n_terms=i;// devolvemos el valor del numero de terminos del arreglo
    return s;
}



void print_terms(int cant_terms, double* terms){ // funcion pedida en esta pregunta para imprimir los ultimos 5 terminos que recibe de parametro la cantidad de terminos y puntero al arreglo
    printf("%.5lf\t%.5lf\t%.5lf\t%.5lf\t%.5lf\n", terms[cant_terms-5],terms[cant_terms-4], terms[cant_terms-3], terms[cant_terms-2], terms[cant_terms-1]); // ultimos 5
}



int main(void){ // %lf para double
    
    double cant_terms = 4000; // para la pregunta 1 nos piden que la cantidad de terminos sea 4mil
    double ref = M_PI/4.0; // nuestro valor de referencia utilizando el valor de pi dividido entre 4
    double tol1 = 1e-4; // tolerancia proporcionada en la pregunta previa 
    double tol2 = 1e-5; // tolerancia proporcionada
    int n_terms; // nuestra variable de numero de terminos

    double* for_terms = (double*)malloc(sizeof(double)*cant_terms); // reservamos en memoria con malloc los 4000 terminos 
    printf("Pregunta 1 s_for en c:\nEl valor resultante es: %lf\n",pi_cuarto_for(cant_terms,for_terms)); //utililzamos la funcion para guardar cada valor en nuestro arreglo y saber el resultado
    print_terms(cant_terms, for_terms); // imprimimos los ultimos 4 con nuestra funcion
    free(for_terms); //liberamos memoria

    n_terms=1; //inicializamos
    double* while_1_terms = (double*)malloc(sizeof(double)*n_terms); // reservamos memoria minimo para 1 termino, deberian ser 3184 terminos una vez se calcula
    printf("Pregunta 2 s_while_1 en c:\nEl valor resultante es: %lf\n",pi_cuarto_while_1(ref,tol1,&while_1_terms,&n_terms)); // se pasa como referencia el arreglo y el numero de terminos para actualizarlos directamente
    print_terms(n_terms, while_1_terms); // utilizamos la funcion que imprime los ultimos 5 terminos con los valores obtenidos de la funcion anterior y actualizados
    free(while_1_terms); // liberamos memoria

    n_terms=1; //nuevamente inicializamos con 1 termino como minimo
    double* while_2_terms = (double*)malloc(sizeof(double)*n_terms); // deberian ser 63663 terminos
    printf("Pregunta 3 2_while_2 en c:\nEl valor resultante es: %lf\n",pi_cuarto_while_2(tol2,&while_2_terms,&n_terms));
    print_terms(n_terms, while_2_terms);
    free(while_2_terms); //y liberamos

    //tambien se pudo unicamente utilizar una reserva de memoria dinamica pero para mayor comprension se generaron 3 de diferentes nombres
    //se pudo agregar una verificacion de que se pudo el realloc sin ningun problema ya que de haber problea regresa un null y podria afectar el codigo

    return 0;

}
