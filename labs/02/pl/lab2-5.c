
#include <stdio.h>
#include <stdlib.h>
#include <math.h> 

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

double pi_cuarto_for(int cant_terms, double* terms){ //definimos nuestra funcion en double ya que es con decimales
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

    terms[i]=s; 
    }

    return s;
}


double pi_cuarto_while_1(double ref,double tol, double** terms,int* n_terms){
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
        (*terms)[i] = s;

        eps = fabs(ref - s) / ref;

        i+=1; // alcualizamos la cuenta

        if(eps < tol){ // en caso que el epsilo es igual o supero la tolerancia acaba
            break;
        }

        
    }
    *n_terms=i;// sacamos la cantidad de terminos que hay
    return s;
}



double pi_cuarto_while_2(double tol, double** terms,int* n_terms){
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

        *terms = realloc(*terms, (i+1) * sizeof(double)); //realloc para que vaya aumentando conforme aumenta el i
        (*terms)[i] = s;
        //printf("%.16lf\n",terms[i]); // para ver los terminos de igual longitud que en python y comprobar

        if(i>0){ // en primer termino i=0 eps =1 no se actualiza
            eps = fabs(s_ant - s) / s_ant;
        }
    
        s_ant = s;
        i+=1;

        if(eps < tol){ //cuando finaliza
            break;
        }

    }
    *n_terms=i;// sacamos la cantidad de terminos que hay
    return s;
}



void print_terms(int cant_terms, double* terms){
    printf("%.5lf\t%.5lf\t%.5lf\t%.5lf\t%.5lf\n", terms[cant_terms-5],terms[cant_terms-4], terms[cant_terms-3], terms[cant_terms-2], terms[cant_terms-1]); // ultimos 5
}



int main(){ // %lf para double
    
    double cant_terms = 4000;
    double ref = M_PI/4.0;
    double tol1 = 1e-4;
    double tol2 = 1e-5;
    int n_terms;

    double* for_terms = (double*)malloc(sizeof(double)*cant_terms); // en el primero son 4000 terminos
    printf("Pregunta 1 s_for en c:\nEl valor resultante es: %lf\n",pi_cuarto_for(cant_terms,for_terms));
    print_terms(cant_terms, for_terms);
    free(for_terms);

    n_terms=1; //inicializamos
    double* while_1_terms = (double*)malloc(sizeof(double)*n_terms); // deberian ser 3184 terminos
    printf("Pregunta 2 s_while_1 en c:\nEl valor resultante es: %lf\n",pi_cuarto_while_1(ref,tol1,&while_1_terms,&n_terms));
    print_terms(n_terms, while_1_terms);
    free(while_1_terms);

    n_terms=1;
    double* while_2_terms = (double*)malloc(sizeof(double)*n_terms); // deberian ser 63663 terminos
    printf("Pregunta 3 2_while_2 en c:\nEl valor resultante es: %lf\n",pi_cuarto_while_2(tol2,&while_2_terms,&n_terms));
    print_terms(n_terms, while_2_terms);
    free(while_2_terms);

    return 0;

}
