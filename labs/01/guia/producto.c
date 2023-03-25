#include <stdio.h> //estandar input output
#include <stdlib.h> //estandar libreria

//el main siempre int y le pasamos 2 argumentos
//argc minimo vale 1 ya que el primero argv[0] el nombre del programa
//argc contiene el numero de argumentos pasados en tipo entero
//argv contiene argumentos apsados desde el SO arreglo de punteros a caracteres
int main(int argc,char const *argv[]){  //siempre lo mismo para pasar agumentos
//char y apuntamos a la direccion para traer los valores?

    if(argc !=3){ // analisa si se agregaron 2 argumentos (1+ 2)
        printf("el tarado se olvido ingresar los numeros o agrego algo demas en c xd\n");
        exit(1);// termina el programa con codigo de error
    }

    int a= atoi(argv[1]);//los valores pasados a partir del 1
    int b= atoi(argv[2]);//atoi es de ascii to integer
    int c = a*b;
    printf("El producto %d x %d es: %d \n",a,b,c);

    return 0; //siempre acabar con return 0
}