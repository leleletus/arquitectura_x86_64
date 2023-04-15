
//como todos son operaciones entre enteros se usara int
//int puede tener un valor de 2147483647 max positivo

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

//-Os para menos espaico
// -c para que cree el object file
// -o para indicar el archivo de salida