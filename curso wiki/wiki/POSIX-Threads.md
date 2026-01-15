# Contenidos
* ## [Introducción](#introducción-1)
     * [Beneficios](#beneficios)
* ## [Funciones básicas del API](#funciones-básicas-del-api-1)
* ## [Ejemplos](#ejemplos-1)
    * [Suma de vectores](#suma-de-vectores)
    * [Producto interno](#producto-punto)
# Introducción

**POSIX threads**, por lo general llamados **pthreads**, es un modelo de ejecución en paralelo, que permite que un programa pueda controlar múltiples flujos de trabajo (_threads_) en simultáneo. Un _thread_ se compone de un _ID_, un _program counter_, un conjunto de registros, y una pila o _stack_. Los _threads_ comparten el segmento de código (**.text**), el segmento de datos (**.data**), y otros recursos del sistema operativo como archivos abiertos y señales, con otros _threads_ que estén **dentro del mismo proceso**. Por lo general, un proceso solo dispone de un _thread_, pero si despliega múltiples _threads_, podrá realizar más de una tarea en simultáneo. [↑](#contenidos)

## Beneficios

* Capacidad de respuesta:
Implementar una aplicación con varios _threads_ permite que el programa continue su ejecución incluso si parte de este está bloqueado, o está ejecutando una operación extensa. De esta forma se incrementa la capacidad de respuesta.
* Compartir recursos:
Por defecto, los _threads_ comparten memoria y otros recursos del proceso al que pertenecen. El beneficio de compartir el segmento de código y datos es que permite a la aplicación tener varios _threads_ trabajando dentro de un mismo espacio de direcciones.
* Economía:
Alojar memoria y recursos para crear un proceso es costoso. Como los _threads_ comparten recursos es menos costoso desplegar _threads_ y commutar entre estos.
* Uso de arquitecturas de varios procesadores:
En estas arquitecturas hay una cantidad de _threads_ por procesador y eso permite aumentar el paralelismo de la aplicación. 

# Funciones básicas del API

El API y su uso puede variar según el sistema operativo que se use. Para los ejemplos que se van a presentar se hará uso del API para sistemas operativos basados en Linux, en específico, para Ubuntu 18.04, por medio de la librería `pthread.h`. El modelo de programacion con _pthreads_ utiliza [funciones propias](https://pubs.opengroup.org/onlinepubs/7908799/xsh/pthread.h.html) para poder ralizar la configuración de threads y la comunicación entre ellos.


1. `pthread_create` 

Se emplea para crear un _thread_, en caso este sea creado de forma exitosa devolverá `0`. Imagine que su programa consta de dos funciones que tienen que ejecutar algo de forma permanente. 

```c
#include <stdio.h>
#include <unistd.h>

void fun1()
{
    int i = 0;
    while (1)
    {
        sleep(1);
        printf("fun1 iteración %d\n", i);
        i++;
    }
}

void fun2()
{
    int i = 0;
    while (1)
    {
        sleep(1);
        printf("fun2 iteración %d\n", i);
        i++;
    }
}

int main()
{
    fun1();
    fun2();
    return 0;
}
```

Si usted compila el programa y lo ejecuta, notará que la función `fun2` nunca se ejecuta, pues el programa es puramente secuencial y `fun1` nunca termina de ejecutarse. Para poder usar las dos funciones en simultáneo se requiere de por lo menos un _thread_ que corra en simultáneo que la función principal, y para esto se hará uso de la función `pthread_create`. [↑](#contenidos)

```c
int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine)(void*), void *arg)
```
Donde:

* `thread` es un puntero a una variable `pthread_t`.
* `attr` son los atributos del _thread_ dentro del proceso, en caso sea `NULL`, se emplearán los atributos por defecto.
* `start_routine` es un puntero a una función que devuelve un `void*` y su argumento es un `void*`.
* `arg` es un `void*` y se emplea para pasar argumentos a `start_routine`.

El ejemplo quedaría de la siguiente forma:

```c
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *fun1(void *arg)
{
    int i = 0;
    while (1)
    {
        sleep(1);
        printf("fun1 iteración %d\n", i);
        i++;
    }

    return NULL;
}

void fun2()
{
    int i = 0;
    while (1)
    {
        sleep(2);
        printf("fun2 iteración %d\n", i);
        i++;
    }
}

int main()
{
    pthread_t pth;

    pthread_create(&pth, NULL, fun1, NULL);

    fun2();
    return 0;
}
```
Note que se ha agregado la cabecera `pthread.h` y que `fun1` ha sido modificada para que se ajuste al prototipo de `pthread_create`. Para crear el ejecutable deberá pasar la opción `pthread` al momento de la compilación, de la siguiente forma: 

```shell
gcc ejemplo_pthread.c -pthread -o ejemplo_pthread
```

2. `pthread_self` 

Devuelve el `ID` del _thread_. Por lo general, se emplea dentro de la función que se pasa al _thread_ durante su creación. Al modificar el ejemplo para que `fun1` indique el `ID` del _thread_ en cada iteración queda de la siguiente manera:

```c
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *fun1(void *arg)
{
    int i = 0;
    while (1)
    {
        sleep(1);
        printf("Saludos del pthread %lu en su iteración %d\n", pthread_self(), i);
        i++;
    }

    return NULL;
}

void fun2()
{
    int i = 0;
    while (1)
    {
        sleep(2);
        printf("fun2 iteración %d\n", i);
        i++;
    }
}

int main()
{
    pthread_t pth;

    pthread_create(&pth, NULL, fun1, NULL);

    fun2();
    return 0;
}
```
Las reglas de compilación para crear el ejecutable no cambian. [↑](#contenidos)

3. `pthread_exit`

Esta función se emplea para terminar la ejecución de la función asociada a determinado _thread_. Su argumento está relacionado con el función `pthread_join`. 

```c
void pthread_exit(void *value_ptr)
```
Donde:

* `value_ptr` es el un puntero asociado al valor que se espera devuelva la función que ejecuta el _thread_.

4. `pthread_join` 

Esta función hace que tengamos que esperar hasta que el _thread_ indicado termine su actividad, en caso exitoso devuelve `0`. El ejemplo se modificará para que las funciones se detengan cuando los contadores cumplan determinada condición, en lugar de operar de forma permanente.

```c
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *fun1(void *arg)
{
    int i = 0;
    while (i < 10)
    {
        sleep(1);
        printf("Saludos del pthread %lu en su iteración %d\n", pthread_self(), i);
        i++;
    }

    return NULL;
}

void fun2()
{
    int i = 0;
    while (i < 2)
    {
        sleep(2);
        printf("fun2 iteración %d\n", i);
        i++;
    }
}

int main()
{
    pthread_t pth;

    pthread_create(&pth, NULL, fun1, NULL);

    fun2();
    return 0;
}
```

Si usted compila y ejecuta el programa, notará que el programa termina su ejecución antes que `fun1` termine de hacer su trabajo. Esto ocurre, porque el programa principal termina luego de que `fun2` termina su trabajo. Para evitar eso se emplea la función `pthread_join`.[↑](#contenidos)

```c
int pthread_join(pthread_t thread, void **value_ptr)
```

Donde:

* `thread` es el _thread_ que se desea esperar.
* `value_ptr` es el valor que se pasó por referencia a la función `pthread_exit` y que se usa para devolver valores desde la función que ejecuta el _thread_.

El ejemplo queda de la siguiente forma:

```c
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void *fun1(void *arg)
{
    int i = 0;
    while (i < 10)
    {
        sleep(1);
        printf("Saludos del pthread %lu en su iteración %d\n", pthread_self(), i);
        i++;
    }

    return NULL;
}

void fun2()
{
    int i = 0;
    while (i < 2)
    {
        sleep(2);
        printf("fun2 iteración %d\n", i);
        i++;
    }
}

int main()
{
    pthread_t pth;

    pthread_create(&pth, NULL, fun1, NULL);

    fun2();

    pthread_join(pth, NULL);

    return 0;
}
```
Con esta ligera modificación, luego de compilar y ejecutar el programa, usted debería observar que ahora las dos tareas se ejecutan hasta el final. Las reglas de compilación para crear el ejecutable son las mismas. [↑](#contenidos)

# Ejemplos

## Suma de vectores

Suma de vectores con n _threads_.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/time.h>

void print_vector(float *v, int size)
{
    printf("\n");
    for (int i = 0; i < size; i++)
    {
        printf("%f\n", v[i]);
    }
    printf("\n");
}

void init_vector(float *v, int size)
{
    for (int i = 0; i < size; i++)
    {
        v[i] = (float)i;
    }
}

double calcularsegundos(struct timeval ti, struct timeval tf)
{
    return (tf.tv_sec - ti.tv_sec) + (tf.tv_usec - ti.tv_usec) / 1000000.0;
}

typedef struct th_info
{
    pthread_t thread;
    int size;
    int id;
    float *v1;
    float *v2;
    float *v3;
} th_info;

void *pth_func(void *args)
{
    th_info *th_info_args = (th_info *)args;
    struct timeval ti, tf;
    gettimeofday(&ti, NULL);
    for (int i = 0; i < th_info_args->size; i++)
    {
        th_info_args->v3[i] = th_info_args->v1[i] + th_info_args->v2[i];
    }
    gettimeofday(&tf, NULL);
    double segundos = calcularsegundos(ti, tf);
    printf("pth_func-%d: %lf segundos\n", th_info_args->id, segundos);
    return NULL;
}

void parallel_vector_sum(float *v1, float *v2, float *v3, int tam, int ths)
{
    int size = (tam / ths);

    th_info threads[ths];

    for (int i = 0; i < ths; i++)
    {
        threads[i].size = size;
        threads[i].id = i;
        threads[i].v1 = v1 + i * size;
        threads[i].v2 = v2 + i * size;
        threads[i].v3 = v3 + i * size;
    }

    pth_func((void *)&threads[0]);

    if (ths > 1)
    {
        for (size_t i = 1; i < ths; ++i)
        {
            pthread_create(&threads[i].thread, NULL, pth_func, (void *)&threads[i]);
        }

        for (size_t i = 1; i < ths; ++i)
        {
            pthread_join(threads[i].thread, NULL);
        }
    }
}

int main(int argc, char **argv)
{
    if (argc != 3)
    {
        printf("Usage: %s <tam> <ths>\n", argv[0]);
        exit(-1);
    }

    struct timeval ti, tf;

    int tam = atoi(argv[1]);

    int ths = atoi(argv[2]);

    float *v1 = (float *)malloc(tam * sizeof(float));
    float *v2 = (float *)malloc(tam * sizeof(float));
    float *v3 = (float *)malloc(tam * sizeof(float));

    // init vectores
    init_vector(v1, tam);
    init_vector(v2, tam);

    gettimeofday(&ti, NULL);
    parallel_vector_sum(v1, v2, v3, tam, ths);
    gettimeofday(&tf, NULL);

    double segundos = calcularsegundos(ti, tf);
    printf("Main: %lf segundos\n", segundos);

    free(v1);
    free(v2);
    free(v3);

    return 0;
}
```
Para compilar:
```shell
gcc sumavectpth.c -o sumavectpth -pthread 
```
En el [siguiente enlace](https://nbviewer.org/github/stefano-andre/sobre-python/blob/main/perfil-pthreads.ipynb) se presenta un perfil con pruebas para varios tamaños y número de _threads_. Observe como cambia el tiempo de ejecución según la cantidad de _threads_ y el tamaño de los vectores. [↑](#contenidos)

## Producto punto

Producto punto con n _threads_.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/time.h>

void print_vector(double *v, int size)
{
    printf("\n");
    for (int i = 0; i < size; i++)
    {
        printf("%lf\n", v[i]);
    }
    printf("\n");
}

void init_vector(double *v, int size)
{
    for (int i = 0; i < size; i++)
    {
        v[i] = (double)i;
    }
}

double calcularsegundos(struct timeval ti, struct timeval tf)
{
    return (tf.tv_sec - ti.tv_sec) + (tf.tv_usec - ti.tv_usec) / 1000000.0;
}

typedef struct th_info
{
    pthread_t thread;
    int size;
    int id;
    double *v1;
    double *v2;
    double pint;
} th_info;

void *pth_func(void *args)
{
    double pint = 0.0;
    th_info *th_info_args = (th_info *)args;
    struct timeval ti, tf;
    gettimeofday(&ti, NULL);
    for (int i = 0; i < th_info_args->size; i++)
    {
        pint += th_info_args->v1[i] * th_info_args->v2[i];
    }
    th_info_args->pint = pint;
    gettimeofday(&tf, NULL);
    double segundos = calcularsegundos(ti,tf);
    printf("pth_func-%d: %lf segundos\n", th_info_args->id, segundos);
    return NULL;
}

double parallel_prod_int(double *v1, double *v2, int tam, int ths)
{
    int size = (tam / ths);

    th_info threads[ths];

    for (int i = 0; i < ths; i++)
    {
        threads[i].size = size;
        threads[i].id = i;
        threads[i].v1 = v1 + i * size;
        threads[i].v2 = v2 + i * size;
    }

    pth_func((void *)&threads[0]);

    if (ths > 1)
    {
        for (int i = 1; i < ths; ++i)
        {
            pthread_create(&threads[i].thread, NULL, pth_func, (void *)&threads[i]);
        }

        for (int i = 1; i < ths; ++i)
        {
            pthread_join(threads[i].thread, NULL);
        }
    }

    float pint = 0.0;

    for (int i = 0; i < ths; i++)
    {
        pint += threads[i].pint;
    }

    return pint;
}

int main(int argc, char **argv)
{
    if (argc != 3)
    {
        printf("Usage: %s <tam> <ths>\n", argv[0]);
        exit(-1);
    }

    struct timeval ti, tf;

    int tam = atoi(argv[1]);

    int ths = atoi(argv[2]);

    double *v1 = (double *)malloc(tam * sizeof(double));
    double *v2 = (double *)malloc(tam * sizeof(double));

    // init vectores
    init_vector(v1, tam);
    init_vector(v2, tam);

    double pint = 0.0;

    gettimeofday(&ti, NULL);
    pint = parallel_prod_int(v1, v2, tam, ths);
    gettimeofday(&tf, NULL);

    double segundos = calcularsegundos(ti, tf);
    printf("Result: %g\n", pint);
    printf("Main: %lf segundos\n", segundos);

    free(v1);
    free(v2);

    return 0;
}
```
Las reglas de compilación son las mismas que para el ejemplo anterior. También se sugiere realizar el mismo análisis. Se recomienda, a manera de ejercicio, realizar un perfil similar al ejemplo anterior. [↑](#contenidos)