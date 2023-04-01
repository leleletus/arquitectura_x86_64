
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double s_formula(double ra){
    return (ra / (1 - ra));
}

double s_for(int cant_terms, double* terms){
    double s = 0;
    for(int i = 0; i < cant_terms; i++){
        s += 1 / (pow(2.0, (double)(i+1)));
        terms[i] = s;
    }
    return s;
}

double s_while_1(double ref, double cota, double tol, int max_iter){
    double s = 0;
    int i = 0;
    double term = 0.0;
    double eps = 0.0;
    while( 1 ){
        term = 1 / (pow(2.0, (double)(i+1)));

        if (term < cota){
            break;
        }

        s += term;

        eps = fabs(ref - s) / ref;

        if (eps < tol) {
            break;
        }

        i++;

        if (i > max_iter){
            break;
        }
    }
    return s;
}

double s_while_2(double tol, int max_iter){
    double s = 0;
    int i = 0;
    double eps = 1.0;
    double s_ant = 0.0;
    while( 1 ){ 
        s += 1 / (pow(2.0, (double)(i+1)));

        if (i > 0){
            eps = fabs(s_ant - s) / s_ant;
        }

        if (eps < tol) {
            break;
        }

        s_ant = s;

        i++;

        if (i > max_iter){
            break;
        }
    }
    return s;
}

void print_terms(int N, double* terms){
    printf("%lf\t%lf\t%lf\t%lf\n", terms[N-4], terms[N-3], terms[N-2], terms[N-1]);
}

int main(){
    
    double ref = s_formula(0.5);
    double tol = 1e-4;

    int cant_terms = 8;
    double* for_terms = (double*)malloc(sizeof(double)*cant_terms);

    printf("ref:%lf\n", ref);
    printf("s_for:%lf\n", s_for(cant_terms, for_terms));
    print_terms(cant_terms, for_terms);
    printf("s_while_1:%lf\n", s_while_1(ref, 0.005, tol, 10));
    printf("s_while_2:%lf\n", s_while_2(tol, 10));
    return 0;
}
