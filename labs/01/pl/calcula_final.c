//en C

#include <stdio.h>
#include <stdlib.h>

int nota_del_final(int a, int b){
    return (110 - 3*a - 3*b) / 4;
}

int main(int argc, char *argv[]){ //el primero cantidad(count) y el segundo los argumentos
    
  if(argc != 3){ //argc es 3 = 2 argumentos + name
      printf("Debe ingresar exactamente 2 notas\r\n");
      return 0;
  }

  int x = atoi(argv[1]); //guardamos en la primera
  int y = atoi(argv[2]); //atoi convierte cadena a entero
  //ya que lo recibe como ascii o utf-8 convertimos al numero

  printf("Me voy por: %d", nota_del_final(x, y));
}
