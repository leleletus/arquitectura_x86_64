#include <stdio.h>
#include <stdlib.h>

double nota_del_final(int a, int b){
    return (110-3*a-3*b)/4.0;
}

int main(int argc, char *argv[]){ //argc me da el tamaño 

  if(argc !=3){ // analiza si se agregaron 2 argumentos (1+ 2)
        printf("Error al ingresar argumentos\n");
        exit(1);// termina el programa con codigo de error
  }

  int x= atoi(argv[1]); //los valores pasados a partir del 1
  int y= atoi(argv[2]); //atoi es de ascii to integer
  printf("Me voy por: %.2f\n", nota_del_final(x,y) );
  return 0;
}