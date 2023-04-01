
#include <stdio.h>
#include <stdlib.h>
#include <math.h> 

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

double pi_cuarto_for(int cant_terms){ //definimos nuestra funcion en double ya que es con decimales
    double s = 0.0; //la serie es en decimales y se inicializa con 0.0 para que continue igual
    double term=0.0;
    int signo=0;
  
    for (int i=0;i<cant_terms;i++){

        if(i % 2 ){
            signo=-1;
        }else{
            signo=1;
        }

    term = signo*(1.0/(2*i+1));
    //printf("%lf ",term); //para ver los valores conseguidos
    s +=term; //acumulamos la suma de la serie
    }

    return s;
}

double pi_cuarto_while_1(double ref,double tol){
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

        if(eps < tol){
            break;
        }

        i+=1;
    }

    return s;
}



double pi_cuarto_while_2(double tol){
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

    if(eps < tol){
        break;
    }

    s_ant = s;
    i+=1;

    }

    return s;
}


int main(){ // %lf para double
    

    printf("Pregunta 1 s_for en c:\nEl valor resultante es: %lf\n",pi_cuarto_for(4000));
    printf("Pregunta 2 s_while_1 en c:\nEl valor resultante es: %lf\n",pi_cuarto_while_1(M_PI/4.0,1e-4));
    printf("Pregunta 3 2_while_2 en c:\nEl valor resultante es: %lf\n",pi_cuarto_while_2(1e-5));

    return 0;

}
