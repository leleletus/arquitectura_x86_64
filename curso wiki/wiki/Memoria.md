# Contenidos

* ## [Jerarquía de Memorias](#jerarquía-de-memorias-1)
* ## [Memoria Caché](#memoria-caché-1)
* ## [Técnica de _Blocking_](#técnica-de-blocking-1)
    * [Multiplicación de Matrices](#multiplicación-de-matrices)
    * [Matriz transpuesta](#matriz-transpuesta)
    * [Multiplicación de matrices usando bloques](#multiplicación-de-matrices-usando-bloques)
    * [Matriz transpuesta usando bloques](#matriz-transpuesta-usando-bloques)

# Jerarquía de Memorias

Se define como jerarquía de memorias, en arquitectura de computadoras, a la relación que existe entre los **tiempos de acceso** a los distintos tipos de memorias y la **capacidad de almacenamiento**. Dicha relación es inversamente proporcional, ello se debe a la complejidad y al costo que existe en la fabricación de memorias.

En la Fig.1 se muestra una organización triangular de la jerarquía de memoria. Las memorias más cercanas al vértice superior tienden a ser de menor tamaño; sin embargo, tienen un mejor rendimiento y un costo más alto por bit que las memorias más cercanas a la base. En el nivel L0 hay registros a los que el CPU puede acceder en un ciclo de reloj. Luego, hay una o más memorias caché basadas en **SRAM** a las que se pueden acceder en unos cuantos ciclos de reloj del CPU. Estos son seguidos por una memoria principal basada en **DRAM** a la que se accede de decenas a cientos de ciclos de reloj de CPU. Seguido están discos locales lentos, pero de gran capacidad. Finalmente, algunos sistemas incluyen un nivel adicional de discos en servidores remotos a los que se puede acceder de una red. Como regla general deducimos que cuanto más rápida es la memoria, mayor es el costo de almacenamiento por bit. 

![jerarquia](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/jerarquia.png)

Hoy en día, las computadoras incluyen una pequeña cantidad de memoria de muy alta velocidad denominada **caché**, donde los datos de las ubicaciones de uso frecuente pueden almacenarse temporalmente. El presente material pretende mostrar como la caché mejora la velocidad de acceso efectiva de la memoria. [↑](#contenidos)

# Memoria Caché

La memoria caché es un tipo de memoria pequeña de alta velocidad, es decir, de alto costo, y que sirve como _buffer_ para los datos a los que se accede. El tiempo de acceso a estos datos es mucho menor que el tiempo de acceso a RAM o al disco duro, y solo el tiempo de acceso a los registros del CPU es menor.

La computadora no tiene forma de saber, _a priori_, a qué datos es más probable que se acceda, por lo que utiliza el principio de **localidad** y transfiere un bloque completo de la memoria principal a la caché. El principio de localidad brinda la oportunidad para que el sistema use una pequeña cantidad de memoria muy rápida para así reducir el tiempo de lectura de datos. Hay dos formas principales de localidad y se definen a continuación:

* **Localidad temporal**: Los elementos a los que se accedió recientemente tienden a ser accedidos nuevamente en el futuro cercano.

* **Localidad espacial**: Si se accede a una posición de memoria una vez, es probable que el programa acceda a una ubicación de memoria cercana.

Los programas que emplean buenas prácticas de localidad tienen menor tiempo de ejecución. Considera la siguiente función, la cual suma los elementos de un vector.

```c
int sumvec(int* v, int N)
{
  int i, sum = 0;

  for(i = 0; i < N; i++)
    sum += v[i];
  return sum;
}
```

Se escribe en a variable `sum` una vez en cada iteración; por lo tanto, la función presenta una buena localidad temporal con respecto a `sum`; sin embargo, dado que `sum` es escalar, la función carece de una localidad espacial para dicha variable. Por otro lado, los elementos del vector `v` se leen secuencialmente, uno tras otro, en el orden en que se almacenan en la memoria. Debido a esto, con respecto al arreglo `v`, tiene buena localidad espacial, pero pobre localidad temporal. 

Las lecturas secuenciales son importantes en los programas que hacen referencias a arreglos. Por ejemplo, considere la función `sumarrayitems`, que suma los elementos de un arreglo bidimensional.

```c
int sumarrayitems(int **a, int M, int N)
{
    int i, j, sum = 0;

    for (i = 0; i < M; i++)
        for (j = 0; j < N; j++)
            sum += a[i][j];
    return sum;
}
```

Suponga que los elementos del arreglo bidimensional `a` están **escritos** en memoria fila por fila (_row-major_). Para este caso la forma en como se leen los datos tiene un buen impacto en la localidad espacial, pues el doble bucle **lee** los elementos fila por fila (_row-view_). Digamos que se realiza un cambio mínimo, y en lugar de leer el arreglo fila por fila, se hace columna por columna (_column-view_).

```c
int sumarrayitems(int **a, int M, int N)
{
    int i, j, sum = 0;

    for (j = 0; j < N; j++)
        for (i = 0; i < M; i++)
            sum += a[i][j];
    return sum;
}
```

El resultado numérico en la variable `sum` será el mismo, pero debido a que la lectura de los elementos se realiza de una forma que no se corresponde con la forma en que están escritos, la función tendrá un mayor tiempo de ejecución.

Reglas simples para evaluar cualitativamente la localidad en un programa:
* Los programas que acceden repetidamente a la mismas variables disfrutan de una buena localidad temporal.
* Para programas con bucles que incluyan matrices multidimensionales secuenciales, cuanto más pequeño sea el salto secuencial, mejor será la localidad espacial. Los programas con saltos grandes alrededor de la memoria presentan una localidad espacial pobre.
* Los bucles tienen una buena ubicación temporal y espacial con respecto a lectura de instrucciones. Cuanto más pequeño sea el cuerpo del bucle y mayor sea el número de iteraciones del bucle, mejor será la localidad.

En lo referente a las memorias caché, cuando se quiere acceder a un dato y este es encontrado, se dice que se ha producido un **acierto o _hit_** y en caso de que dicho dato no sea encontrado dentro de la caché se produce un **fallo o _miss_**. Esto último ocasiona que el dato deba ser buscado en la _RAM_ o disco duro, los cuales poseen un tiempo de acceso más lento. De esta manera, la ejecución del programa tiene un mayor tiempo de ejecución.

Es por eso que muchos algoritmos no solo se basan en la lógica de la resolución del problema en sí, sino que también organizan la estructura de acceso a datos de tal manera que, si algunos valores deben ser reutilizados para futuras operaciones, estos puedan aprovechar la localidad tanto espacial como temporal para la mejora del tiempo de ejecución del programa. [↑](#contenidos)

# Técnica de _Blocking_

_Blocking_ es una técnica que **aprovecha la localidad temporal y espacial** mediante el uso de algoritmos que organizan la estructura de datos en **bloques**. La idea principal es insertar una cantidad de datos (_chunk_) en la memoria caché, trabajar lo más que se pueda con dicha información y luego avanzar al siguiente bloque. De esta forma, los accesos a los datos que se encuentren dentro de nuestro bloque y, por ende, dentro de la memoria caché tendrán una mayor tasa de aciertos; así el programa estará optimizado. Previo a la explicación de la técnica de _blocking_ debemos conocer dos operaciones básicas de algebra lineal. [↑](#contenidos)

## Multiplicación de Matrices

Sea `A` una matriz de `n` filas y `m` columnas (`n x m`), y `B` una matriz de `m` filas y `p` columnas (`m x p`), entonces el producto de ambas matrices, `C = A*B`, es una matriz de `n` filas y `p` columnas (`n x p`). Cada elemento se calcula de la siguiente manera:

![matrixmult](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/matrix-mult.png)

Ejemplo:

![matrixmultej](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/matrix-mult-ejemplo.png)

Se verifica que el número de columnas de la matriz `A` es igual al número de filas de la matriz `B` y que el producto, denotado como matriz `C`, tiene la cantidad de filas de la matriz `A` y la cantidad de columnas de la matriz `B`. [↑](#contenidos)

## Matriz transpuesta

Sea `A` una matriz de tamaño `n x m`, la transpuesta será una matriz de tamaño `m x n` y se obtiene mediante el cambio de filas por columnas (o viceversa). Cada elemento será calculado de la siguiente manera:

![transposeop](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/mat-transpose.png)

Ejemplo:

![transposex](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/mat-transpose-ejemplo.png)

Se verifica que esta operación realiza un giro de la matriz y considera como eje la diagonal de la matriz. [↑](#contenidos)

## Multiplicación de matrices usando bloques

El objetivo principal de trabajar por bloques es mejorar el tiempo de procesamiento debido a la existencia de localidad temporal y espacial. Por ejemplo, si se tuviesen dos matrices cuadradas de igual tamaño que deseamos multiplicar, estas se pueden dividir en submatrices y luego explotar el hecho matemático de que estas submatrices pueden manipularse como escalares. Supongamos que queremos calcular `C = AB`, donde `A`, `B` y `C` son cada una matrices de 8 x 8. Podemos dividir cada matriz en cuatro submatrices de 4 x 4 de la siguiente forma:

![matrixblockmult](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/matrix-mult-block.png)

Luego:

![matrixblockmultres1](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/matrix-mult-block-1.png)<br/><br/>
![matrixblockmultres2](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/matrix-mult-block-2.png)<br/><br/>
![matrixblockmultres3](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/matrix-mult-block-3.png)<br/><br/>
![matrixblockmultres4](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/matrix-mult-block-4.png)<br/><br/>

Note que se definió un tamaño de bloque igual a la mitad de la matriz; sin embargo, no siempre tiene que ser así; es recomendable usar tamaños de bloques de tal manera que todos los datos puedan ser localizados dentro de la memoria caché. Si el bloque es muy grande, ciertos datos se perderán y serán guardados fuera de la caché (al siguiente nivel de la jerarquía de memoria). 

Una forma de resolver la multiplicación `C = AB` usando _blocking_ es de la siguiente manera:

* Definir un tamaño de bloque `1 x bsize` (_block size_) para la matriz `A`. La matriz `A` disfruta de una buena localidad espacial porque cada bloque es accedido en fila unitaria (`1 x bsize`). Además, existe una buena localidad temporal porque el bloque es accedido _bsize_ veces seguidas.

* Realizar particiones de la matriz `B` en bloques de tamaño `bsize x bsize`. La intención es almacenar bloques de dicha matriz en la memoria caché, usar toda esa información y luego descartarla para cargar un nuevo bloque. El acceso a la matriz `B` disfruta de una buena localidad temporal porque se accede al bloque `bsize x bsize` completo `n` veces consecutivas.

* La matriz resultante `C` presenta una buena localidad espacial porque cada elemento del bloque está fijado en sucesión. Sin embargo, no presenta una buena localidad temporal porque cada bloque es accedido solo una vez.

En la siguiente figura se muestra una explicación gráfica de lo señalado anteriormente, donde `n` es el tamaño de las matrices cuadradas. Para el presente laboratorio se considera a `bsize` como un divisor exacto de `n`. [↑](#contenidos)

![matmultblockalg](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/mat-transpose-block-alg.png)

## Matriz transpuesta usando bloques

De igual forma que en el algoritmo anterior, obtendremos la transpuesta de una matriz mediante la técnica _blocking_. La idea principal se puede observar en la siguiente ecuación:

![matrixtranspblock](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/memoria/mat-transpose-block.png)

Cada matriz es un bloque que pertenece a la matriz principal `A`. De forma análoga a la multiplicación por bloques, aprovecharemos la buena localidad espacial y temporal así como también los aciertos a la memoria caché, los cuales se traducen a una ejecución del algoritmo en menor tiempo. [↑](#contenidos)



