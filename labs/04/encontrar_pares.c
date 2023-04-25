
#include <stdio.h>
#include <stdlib.h>
//#include <math.h>


short  encontrar_pares(short  inf, short  sup, short  sum, short** arreglo_x, short** arreglo_y){
    short  cant_pares=0;

    //printf("%d %d %d \n",inf, sup,sum); //viendo los valores ingresados

    for(short  i=inf;i<=sup;i++){ // empezamos desde el valor mas pequeño hasta el mas grande
        if( (sum-i) >=inf && (sum-i) <=sup){ //si x toma el valor de "y" entonces y deberia tomar el valor de la resta
            short  tempx= i;
            short  tempy= sum-i;

            if(tempx <= tempy){ //para que no se repitan x debe ser siempre menor o igual 
                cant_pares++;//si la resta esta dentro del rango entonces es una pareja

                *arreglo_x = realloc(*arreglo_x, (cant_pares) * sizeof(double)); //realloc para que vaya aumentando conforme aumenta el los pares encontrados
                (*arreglo_x)[cant_pares-1] = tempx; //guardamos en nuestro puntero del main

                *arreglo_y = realloc(*arreglo_y, (cant_pares) * sizeof(double)); //realloc para que vaya aumentando conforme aumenta el los pares encontrados
                (*arreglo_y)[cant_pares-1] = tempy; //guardamos en nuestro puntero del main


                //printf("%d %d \n",tempx,tempy); //imprimiendo el par
            }

            
        }
    }

    return cant_pares;
}

int  main(void){
    //declaramos nuestros datos
    short  inf=-5;
    short  sup=4;
    short  sum=2;

    //los terminos de x e y
    int cant_terms = 1; //declaramos la cantidad minima de terminos
    short* x = (short*)malloc(sizeof(short)*cant_terms);
    short* y = (short*)malloc(sizeof(short)*cant_terms);
    //printf("%ld \n",sizeof(short)); //2bytes = 16 bits

    short cantidad=encontrar_pares(inf,sup,sum,&x,&y); //guardamos el valor en una variable


    printf("Cantidad de pares: %d\n",cantidad); //imprimimos cantidad
    printf("Los pares encontrados son:\n"); //imprimimos cantidad
    for(int i=0;i<cantidad;i++){ //imprimimos los pares encontrador
        printf("(%d,%d)\t", x[i],y[i]);
    }
    printf("\n"); 


    return 0;
}


//gcc encontrar_pares.c -o  encontrar_pares && ./encontrar_pares
