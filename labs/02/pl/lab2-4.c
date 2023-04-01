
#include <stdio.h> // generamos el archivo con %%file
#include <stdlib.h> // incluimos las librerias estandars y math para operaciones
#include <math.h>  // para usarla al compilar debemos utilizar -lm

#ifndef M_PI // en caso no este definido pi lo definimos
#define M_PI 3.14159265358979323846
#endif

double pi_cuarto_for(int cant_terms){ //definimos nuestra funcion en double ya que es con decimales
    double s = 0.0; //la serie es en decimales y se inicializa con 0.0 para que continue igual
    double term=0.0;
    int signo=0; 
  
    for (int i=0;i<cant_terms;i++){ //inilizamos fort para las iteraciones y finalizara con el parametro terminos

        if(i % 2 ){
            signo=-1;
        }else{
            signo=1;
        }

    term = signo*(1.0/(2*i+1)); // se calcula cada termino de la sumatoria
    //printf("%lf ",term); //para ver los valores conseguidos si deseamos verificar
    s +=term; //acumulamos la suma de la serie
    }

    return s;
}

double pi_cuarto_while_1(double ref,double tol){ // funcion de la pregunta 2 en c 
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

        eps = fabs(ref - s) / ref;

        if(eps < tol){ //condicion para finalizar iteraciones
            break;
        }

        i+=1;
    }

    return s; //retornamos valor
}



double pi_cuarto_while_2(double tol){ // funcion de la pregunta 3
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

    if(i>0){
        eps = fabs(s_ant - s) / s_ant;
    }

    if(eps < tol){ //condicion para finalizar iteraciones
        break;
    }

    s_ant = s;
    i+=1;

    }

    return s;
}


int main(void){ // %lf para double y como no ingresamos ningun argumento esta vacio
    
    //en el main directamente imprimimos las respuestas con el resultado de las 3 funciones declaradas y sus parametros de entrada
    printf("Pregunta 1 s_for en c:\nEl valor resultante es: %lf\n",pi_cuarto_for(4000));
    printf("Pregunta 2 s_while_1 en c:\nEl valor resultante es: %lf\n",pi_cuarto_while_1(M_PI/4.0,1e-4));
    printf("Pregunta 3 2_while_2 en c:\nEl valor resultante es: %lf\n",pi_cuarto_while_2(1e-5));

    return 0;

}
