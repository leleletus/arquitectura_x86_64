# Contenidos
* ## [Tipos de dato de MPI](#tipos-de-dato-de-mpi-1)
* ## [Funciones básicas de MPI](#funciones-básicas-de-mpi-1)
    * [Inicialización y finalización](#inicialización-y-finalización)
    * [Comunicación punto a punto](#comunicación-punto-a-punto)
* ## [Ejemplos](#ejemplos-1)
    * [Hola mundo](#hola-mundo)
    * [Norma-2](#norma-2)

El modelo de programacion MPI es una abstracción de un sistema con mútiples unidades de procesamiento que no comparten un espacio de memoria. En este modelo, cada procesador se comunica uno con otro de forma independiente y cuentan con una memoria independiente que solo ellos pueden accesar. 

# Tipos de dato de MPI

Los **datatype** son tipos de datos predefinidos de MPI que corresponden a tipos de datos ya definidos en C. En la tabla siguiente, se presentan algunos de estos.

|   Tipo de dato en MPI  |         Tipo de dato en C        |
|:----------------------:|:--------------------------------:|
|        MPI_CHAR        |            signed char           |
|        MPI_SHORT       |         signed short int         |
|         MPI_INT        |            signed int            |
|        MPI_LONG        |          signed long int         |
|    MPI_LONG_LONG_INT   |           long long int          |
|    MPI_UNSIGNED_CHAR   |           unsigned char          |
|   MPI_UNSIGNED_SHORT   |        unsigned short int        |
|      MPI_UNSIGNED      |           unsigned int           |
|    MPI_UNSIGNED_LONG   |         unsigned long int        |
| MPI_UNSIGNED_LONG_LONG |      unsigned long long int      |
|        MPI_FLOAT       |               float              |
|       MPI_DOUBLE       |              double              |
|     MPI_LONG_DOUBLE    |            long double           |
|        MPI_WCHAR       |             wide char            |
|       MPI_PACKED       |       tipo de dato especial      |
|        MPI_BYTE        | tipo de dato de tamaño de 1 byte |

Los ultimos 2 datos de la tabla no tiene un equivalente exacto an C. [↑](#contenidos)

# Funciones básicas de MPI

El modelo de programacion MPI utiliza [funciones propias](https://www.mpich.org/static/docs/v3.3/www3/) para poder realizar la configuración de threads y la comunicación entre ellos. A continuación se listan algunas de las funciones basicas de MPI.

## Inicialización y finalización

1. `MPI_Init`

Inicializa la estructura de comunicacion de MPI entre los procesos. Ninguna función de comunicación MPI funcionará sin esta instrucción al inicio del programa. [↑](#contenidos)

```c
int MPI_Init(int *argc, char ***argv)
```

Donde:

* `argc` es el puntero al número de argumentos.
* `argv` es el puntero al vector de argumentos.

2. `MPI_Comm_size`

Determina el tamaño del comunicador seleccionado, es decir, el número de procesos que están actualmente asociados a este. [↑](#contenidos)

```c
int MPI_Comm_size(MPI_Comm comm, int *size)
```

Donde:

* `comm` es el comunicador.
* `size` es el número de procesos.

3. `MPI_Comm_rank`

Determina el _rank_ (identificador) del proceso que lo llama dentro del comunicador seleccionado. [↑](#contenidos)

```c
int MPI_Comm_rank(MPI_Comm comm, int *rank)
```

Donde:

* `comm` es el comunicador.
* `rank` es el identificador del procesos.

4. `MPI_Finalize`

Corta la comunicación entre los procesos y elimina los tipos de datos creados para ello. [↑](#contenidos)

```c
int MPI_Finalize(void)
```

## Comunicación punto a punto

1. `MPI_Send`

Envía datos desde un nodo a otro. [↑](#contenidos)

```c
int MPI_Send(const void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)
```

Donde:

* `buf` es un buffer que contiene los datos a enviar.
* `count` es la cantidad de datos a enviar.
* `datatype` es el tipo de dato a enviar.
* `dest` es el rank o identificador del proceso que debe recibir los datos.
* `tag` es un mensaje que permite distinguir los distintos mensajes posibles de un mismo origen.
* `comm` especifica el tipo de comunicacion usada.

2. `MPI_Recv`

Recibe datos desde un nodo a otro. [↑](#contenidos)

```c
int MPI_Recv(void *buf, int count, MPI_Datatype datatype, int source, int tag, MPI_Comm comm, MPI_Status *status)
```

* `buf` es un buffer que contiene los datos a recibir.
* `count` es la cantidad de datos que se espera recibir.
* `datatype` es el tipo de dato a recibir.
* `dest` es el rank o identificador del proceso que envió los datos.
* `tag` es un mensaje que permite distinguir los distintos mensajes posibles de un mismo origen.
* `comm` especifica el tipo de comunicacion usada.
* `status` es una estructura que contiene información sobre la comunicación.

# Ejemplos

Los siguientes ejemplos fueron compilados y ejecutados en una máquina virtual que tiene 4 _cores_, con memoria _RAM_ de 4GB y sistema operativo Ubuntu-18.04 (para conocer sus datos en Ubuntu puede usar los comandos `cat /proc/cpuinfo` y `cat /proc/meminfo` en el terminal). Para compilar y ejecutar los ejemplos deberá tener instalado `mpicc` y `mpirun`. Si no los tiene, los puede instalar. [↑](#contenidos)

```shell
sudo apt update
sudo apt install mpich
```

## Hola Mundo

El siguiente código se ejecutará en la cantidad de procesos que se indiquen:

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    // Inicializar el entorno MPI
    MPI_Init(NULL, NULL);

    // Obtener el número de procesos
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    // Obtener el rank del proceso
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    // Obtener el nombre del procesador
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;
    MPI_Get_processor_name(processor_name, &name_len);

    // Imprimir hola mundo
    printf("Hola mundo desde el procesador %s, rank %d de %d procesos\n", processor_name, world_rank, world_size);

    // Finalizar el entorno MPI
    MPI_Finalize();
}
```

Para compilar:

```shell
mpicc mpihelloworld.c -o mpihelloworld
```
Para ejecutar en 4 procesos:
```shell
mpirun -np 4 ./mpihelloworld
```

## Norma-2

La norma-2 de la diferencia de dos vectores de tamaño N se calcula de la siguiente manera:

![norma2diff](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/mpi/norma-2-vec-diff.png)

La solución puede ser esquematizada de la siguiente manera:

* Asumir que los vectores son de longitud que se puede dividir entre la cantidad de procesos, y que se encuentran inicialmente en el proceso con _rank_ `0`, y que este separa a los vectores en _chunks_.
* El proceso de _rank_ `0` envía cada par de _chunks_ a un proceso específico, excepto por el de _rank_ 0.
* Cada proceso ejecuta la función `quad_diff`.
* Luego de realizar la operación anterior, cada proceso devuelve su resultado parcial al proceso de _rank_ `0`, y este último acumulará esos resultados parciales.
* Por último, el proceso de _rank_ `0` realiza la raíz cuadrada de los resultados parciales acumulados, que es lo buscado.

Es importante mencionar que se introdujo 2 tomas de tiempo en el proceso de _rank_ `0` debido a que este tiene el resultado correcto al final de realizada la operación. 

```c
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void array_init(float *arr, int numel, float var, float media)
{
    int i, k;
    float temp, desv;

    desv = (float)sqrt((double)var);

    srand(time(NULL));

    for (i = 0; i < numel; i++)
    {
        temp = 0;
        for (k = 0; k < 100; k++)
        {
            temp += (float)rand() / RAND_MAX;
        }
        arr[i] = desv * (float)(sqrt((double)3 / 5) * (temp - (float)50) + media);
    }
}

float quad_diff(float *a, float *b, int numel)
{
    int i;
    float temp = 0.0;

    for (i = 0; i < numel; i++)
    {
        temp += (a[i] - b[i]) * (a[i] - b[i]);
    }
    return temp;
}

int main(int argc, char **argv)
{
    MPI_Init(NULL, NULL);

    float *a, *b;

    int n = 1000000, i, world_size;

    float d = 0, dp = 0;

    int world_rank;

    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    clock_t begin, end;

    a = (float *)malloc(sizeof(float) * n);
    b = (float *)malloc(sizeof(float) * n);

    if (world_rank == 0)
    {
        array_init(a, n, 1.0, 0.0);
        for (i = 0; i < n; i++)
        {
            b[i] = a[n - i - 1];
        }
    }

    int chunk = n / world_size;

    if (world_rank == 0)
    {
        begin = clock();

        for (i = 1; i < world_size; i++)
        {
            MPI_Send((float *)(a + chunk * i), chunk, MPI_FLOAT, i, 0, MPI_COMM_WORLD);
            MPI_Send((float *)(b + chunk * i), chunk, MPI_FLOAT, i, 0, MPI_COMM_WORLD);
        }
    }
    else
    {
        MPI_Recv(a, chunk, MPI_FLOAT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        MPI_Recv(b, chunk, MPI_FLOAT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }

    dp = quad_diff(a, b, chunk);

    if (world_rank == 0)
    {
        d = dp;
        for (i = 1; i < world_size; i++)
        {
            MPI_Recv(&dp, 1, MPI_FLOAT, i, 2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            d = d + dp;
        }
    }
    else
    {
        MPI_Send(&dp, 1, MPI_FLOAT, 0, 2, MPI_COMM_WORLD);
    }

    d = sqrt(d);

    if (world_rank == 0)
    {
        end = clock();
        double elapsed_secs = (double)(end - begin) / CLOCKS_PER_SEC;
        printf("Demora %f segundos con resultado %f\n", elapsed_secs, d);
    }

    MPI_Finalize();
}
```
Para compilar:
```shell
mpicc mpi_norm2.c -o mpi_norm2 -lm
```
Para ejecutar:
```shell
mpirun -np 4 ./mpi_norm2
```