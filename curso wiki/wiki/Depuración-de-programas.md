# Contenido
* ## [El depurador de GNU](#el-depurador-de-gnu-1)
* ## [Primeros pasos con GDB](#primeros-pasos-con-gdb-1)
    * [Programa de ejemplo](#programa-de-ejemplo)
    * [Primeros comandos con GDB](#primeros-comandos-con-gdb)
    * [Comandos para seguimiento de registros](#comandos-para-seguimiento-de-registros)
    * [Comandos para seguimiento de memoria](#comandos-para-seguimiento-de-memoria)
    * [Condicionales y bucles](#condicionales-y-bucles)
    * [Ganchos](#ganchos)
    * [Comandos personalizados](#comandos-personalizados)
* ## [Programas con funciones](#programas-con-funciones-1)
* ## [Scripts](#scripts-1)
    * [Primer ejemplo](#primer-ejemplo)
    * [Segundo ejemplo](#segundo-ejemplo)

# El depurador de GNU

Depurar (_debug_) un programa con fallas (_bugs_) es el proceso de confirmar, sentencia por sentencia, que los supuestos que afirmamos que hace el programa se cumplen. Cuando se ubica la línea exacta de código en la cual esos supuestos no se cumplen, es cuando se afirma que se ha detectado la falla (_bug_).

GDB (_GNU Project debugger_) permite entender que es lo que sucede al interior de un programa cuando se está ejecutando, o analizar el estado del mismo cuando ocurre alguna falla. GDB puede realizar una serie de tareas que permiten la correcta depuración del código fuente. GDB puede realizar una serie de tareas que permiten la correcta depuración del código fuente. Entre ellas tenemos:

* Iniciar un programa especificando las condiciones que puedan afectar su funcionamiento.
* Detener el programa cuando alguna condición se cumpla.
* Examinar cuál es el estado de las variables cuando el programa se detiene.
* Experimentar con los errores para su correcta depuración.

GDB es la herramienta de depuración más empleada por los usuarios de distribuciones UNIX/LINUX. Por lo general, GDB viene instalado por defecto, pero en caso no sea así lo puede instalar ejecutando los siguientes comandos en un terminal:

```shell
sudo apt update
sudo apt install gdb
```

Se empleará GDB para realizar seguimiento de las variables locales, registros, y posiciones de memoria de interés de un programa en lenguaje ensamblador y C. [↑](#contenido)

# Primeros pasos con GDB

## Programa de ejemplo

Se hará una presentación general de los comandos que nos servirán para hacer un seguimiento del programa con el siguiente ejemplo: 

```asm
; para ensamblar:
; nasm -f elf64 -g ejemplo_gdb.asm -o ejemplo_gdb.o
; para enlazar:
; ld ejemplo_gdb.o -o ejemplo_gdb
        segment .data
a       dd      4   
b       dd      1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9
btam    dd      9
c       dw      1,2 
e       db      "hola mundo",10,0
f       equ     $-e 

        segment .bss
g       resb    1   
h       resw    10  
i       resq    100 

        segment .text
        global _start

_start:
    
        mov     rax, 1
        mov     rdi, 1
        mov     rsi, e
        mov     rdx, f
        syscall
    
        mov     rax, 60
        mov     rdi, 0
        syscall
```

## Primeros comandos con GDB

Antes de ejecutar el depurador, debe estar seguro de que ha colocado la bandera `-g` en el momento de generar el ejecutable. A pesar de que se menciona en los comentarios del archivo, se le recuerda que debe ser de la siguiente manera:

```shell
nasm -f elf64 -g ejemplo_gdb.asm -o ejemplo_gdb.o
ld ejemplo_gdb.o -o ejemplo_gdb
```

Para correr el depurador con nuestro programa ejemplo deberá ejecutar el siguiente comando:

```shell
gdb ejemplo_gdb
```

Luego de ejecutar el comando anterior se debería observar una salidad **similar** a la siguiente:

```shell
GNU gdb (Ubuntu 8.1-0ubuntu3.2) 8.1.0.20180409-git
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ejemplo_gdb...done.
(gdb) 
```

Dentro de GDB ya puede empezar a ejecutar comandos para la depuración.

* Para hacer seguimiento de los comandos ejecutados:

```shell
set trace-commands on
```

* Para guardar las salidas de los comandos ejecutados en un archivo de salida:

```shell
set logging file commands.txt
```

* Para empezar a guardar los resultados:

```shell
set logging on
```

* Para fijar un punto de quiebre en el código:

```shell
break _start
```
Esta sentencia, en general, debe indicar el comando `break` y la **etiqueta** en la que se desea hacer la pausa. Puede haber más de un _breakpoint_. También puede fijar un punto de quiebre indicando el número de línea. (En caso sea un programa en ensamblador, debe ser una línea del segmento `.text`)

Para fijar un punto de quiebre en la línea 23:

```shell
b 23
```

O para fijar un punto de quiebre en la línea 24:

```shell
b 24
```

* Para ver la información de los _breakpoints_:

```shell
info break
```

* Para borrar un _breakpoint_:

```shell
delete 2 3
```

Para este comando basta con indicar el número del _breakpoint_ luego de `delete`. Luego, podemos verificar que se han borrado volviendo a ejecutar el comando `info`.

* Para ejecutar el código:

```shell
run
```

Si se han fijado _breakpoints_ el programa se ejecutará hasta el primero de estos, en caso contrario ejecutará todo el programa.

* Para fijar la sintaxis del _dissassembly_:

```shell
set disassembly-flavor intel
```

* Para mostrar el _disassembly_:

```shell
disassemble
```

También puede usar la forma corta `disass`.

Este comando muestra el código ensamblado y su lugar en la memoria de cada instrucción. La flecha en la parte izquierda indica la instrucción en la que se encuentra y **aún no ha ejecutado**.

* Para mostrar variables:

```shell
info variables
```

* Para **ver** la siguiente instrucción:

```shell
x/i $pc
```

* Para **ejecutar** la siguiente instrucción:

```shell
nexti
```

También puede usar su forma corta `ni`.

* Para definir un símbolo con un valor:

```shell
set $raxval=$rax
```
En este caso se ha definido un símbolo `$raxval` que tiene el valor del registro `rax` en el momento que se definió el símbolo. Debe tener en cuenta que si el valor de `rax` cambia el valor del símbolo no cambiará, y si usted desea que cambie con el nuevo valor, deberá actualizar el símbolo ejecutando otra vez el comando `set`. Este comando también se pudo haber realizado con variables definidas en el segmento de datos, por ejemplo:

```shell
set $aval=(int)a
```

Por último, mencionar que también lo pudo haber efectuado con un valor constante. [↑](#contenido)

## Comandos para seguimiento de registros

* Para mostrar la información de los registros de propósito general:

```shell
info registers
```

También tiene una forma corta:

```shell
i r
```

* Para mostrar la información de un registro específico:

```shell
i r rax
```

También puede indicar una lista de registros:

```shell
i r rax rbx rcx
```

* Para mostrar la información de todos los registros:

```shell
i all-registers
```

* Para mostrar la información de los registros de la unidad SIMD:

```shell
p $xmm0
```

El mismo comando se puede usar para todos los registros de la unidad, desde `xmm0` hasta `xmm15`. Este comando será más útil cuando emplee operaciones en coma flotante. 

## Comandos para seguimiento de memoria

* Comando `print`:

El formato para el comando `print` es `print expression` o `print/format expression` donde _format_ es una letra que define el formato de las datos que se van a mostrar. Los formatos a elegir pueden ser algunos de los siguientes:

| Letra |     Formato    |
|:-----:|:--------------:|
|   d   |     decimal    |
|   x   |   hexadecimal  |
|   t   |     binario    |
|   u   |    sin signo   |
|   f   | punto flotante |
|   i   |   instrucción  |
|   c   |    caracter    |
|   s   |     string     |
|   a   |     address    |

Cuando emplea el comando `print` sobre una variable es recomendable indicar el tipo de dato adecuado para mostrar el resultado correcto. Por ejemplo, para imprimir el valor de la variable `a`:

```shell
print (char) a
```

Pero si usted desea imprimir la misma variable en formato **hexadecimal**, puede ejecutar:

```shell
print/x (char) a
```

O en formato **binario**:

```shell
print/t (char) a
```

También lo puede imprimir como caracter:

```shell
print/c (char) a
```

En el caso de otras variables como `b`, solo es cuestión de indicar el tipo de dato y el formato adecuado:

```shell
p/f (float) b
```

Observe que con el comando `print` es necesario indicar el tipo de dato de la variable entre paréntesis.

* Comando `x`: 

El formato para el comando `x` es `x/CantFormTam direccion`  donde **Cant** es el número de elementos a examinar, **Form** es el formato, y **Tam** es el tamaño de cada posición de memoria. Los formatos son los mismos que para el comando `print` y los tamaños a elegir pueden ser algunos de los siguientes:

| Letra |  Tamaño  | Bytes |
|:-----:|:--------:|:-----:|
|   b   |   byte   |   1   |
|   h   | halfword |   2   |
|   w   |   word   |   4   |
|   g   |   giant  |   8   |

Por ejemplo, para ver 4 _bytes_ en formato hexadecimal de la variable `e`:

```shell
x/4xb &e
```

Para ver la cadena en `e` en formato _string_:

```shell
x/s &e
```

Para examinar la varible `b`:

```shell
x/f &b
```

Recuerde que también puede examinar la memoria empleando los símbolos de los registros. Esto es especialmente útil cuando se pasan punteros como argumentos de alguna función.

```shell
x/4wd $rdi
```

Como ejercicio se le pide que examine e imprima otras variables del programa con los otros formatos y tamaños disponibles. [↑](#contenido)

## Condicionales y bucles

* Sentencia `if`:

Le herramienta gdb le permite condicionar la ejecución de comandos por medio de la sentencia `if`. Si usted está dentro de GDB e ingresa el comando `if`, seguido de alguna condición, por ejemplo:

```
if (unsigned int)a > 0
```

Debería observar una salida similar a la siguiente:

```
>
```

Eso le indica que puede ingresar los comandos que desea que se ejecuten en caso se cumpla la condición, estos pueden ser uno o varios, y se deben ingresar uno a la vez. Para indicar que queremos terminar de ingresar comandos se hace:

```
> end 
```

* Sentencia `while`:

Las indicaciones son las mismas que con el comando `if`.

Tenga en cuenta que las sentencias de `if` y `while` se pueden usar también con símbolos que usted haya definido como `$raxval` o por símbolos predefinidos como `$rax`. [↑](#contenido)

## Ganchos

La herramienta gdb le permitirá crear ganchos o _hooks_, es así como le llaman a una secuencia de comandos que estarán enganchados al comando que se indica al momento de su definición. Los _hook_ pueden ser previos y posteriores al comando de interés.

Por ejemplo, para definir un _hook_ previo al comando `echo`:

```shell
define hook-echo
```

Debería observar una salida **similar** a la siguiente:

```shell
Type commands for definition of "hook-echo".
End with a line saying just "end".
>
```

Para el ejemplo vamos a incluir lo siguiente:

```shell
>echo <<<--- 
```

Y para terminar el _hook_:

```shell
>end
```

Para definir un _hook_ posterior al comando `echo`:

```shell
define hookpost-echo
```

Debería observar una salida **similar** a la siguiente:

```shell
Type commands for definition of "hookpost-echo".
End with a line saying just "end".
>
```

Para el ejemplo vamos a incluir lo siguiente:

```shell
>echo --->>>\n 
```

Y para terminar el _hook_:

```shell
>end
```

Para probar el gancho implementado:

```shell
echo Hola mundo
```

Debería observar el siguiente resultado:

```shell
<<<---Hola mundo--->>>
```

Queda como ejercicio para el lector hacer otros ejercicios similares. [↑](#contenido)

## Comandos personalizados

La herramienta también le permite crear comando personalizados. Por ejemplo, para crear un comando llamado `saludar` se emplea la palabra reservada `define`.

Desde GDB ejecute el siguiente comando:

```shell
define saludar
```

Debería observar una salida **similar** a la siguiente:

```shell
Type commands for definition of "saludar".
End with a line saying just "end".
>
```

Nuestro comando se limitará a decir `Hola`:

```shell
>printf "Hola\n"
```

Para terminar:

```shell
>end
```

Ahora ya puede ejecutar el siguiente comando:

```shell
saludar
```

Y observar la siguiente salida:

```shell
Hola
```

Se recomienda, como ejercicio, crear sus propios comandos al lector. [↑](#contenido)

# Programas con funciones

Se presentarán unos cuantos comandos útiles para el análisis de códigos que contienen funciones. Como ejemplo se emplearán códigos sencillos que realizan llamadas a funciones.

El código en ensamblador se encargará de incrementar en una unidad a un número _double_.

```asm
; funcion que incrementa en una unidad un double
; la palabra reservada rel indica que la lectura de esta variable 
; es relativa a las direcciones del object file generado
	global incdouble
	section .data
uno	dq	1.0
	section .text
incdouble:
	addsd	xmm0,	[rel uno] 
	ret
```
El código C incrementará los elementos de un vector de _doubles_ en una unidad llamando a ese código en ensamblador.

```c
// la funcion main llama a genvector
// la funcion genvector llama a incdouble

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

extern double incdouble(double d);

void genvector(double *v, int size){
	for(int i = 0; i < size; i++){
                v[i] = 0.0;
		v[i] = incdouble(v[i]);
	}
}


int main(int argc, char** argv){

	int size = 0;
	if (argc != 2) {
		printf("usage: ./funcs <numero_entero>\n");
	}
	else {
		size = atoi(argv[1]);
	}	

	double *v;
	v = (double *)malloc(sizeof(double)*size);

	genvector(v,size);	

	return 0;
}
```

Para crear el ejecutable:

```shell
nasm -g -f elf64 incdouble.asm -o incdouble.o
gcc -g incdouble.o funcs.c -o funcs -lm
```

Luego de crear el ejecutable, ingrese a GDB y cargue el ejecutable:

```shell
file funcs
```

Una vez cargado el archivo, se deben fijar las condiciones necesarias para empezar a analizar el código paso a paso. Primero, se fijará el _disassembly_ a la sintaxis de intel:

```shell
set disassembly-flavor intel
```

Para que imprima bonito:

```shell
set print pretty
```

Para pasar los argumentos del programa, que en este caso es el tamaño del vector:

```shell
set args 4
```

Luego, fije puntos de quiebre. En este caso, el nombre de cada función será un punto de quiebre:

```shell
b main
```
```shell
b genvector
```
```shell
b incdouble
```

Empiece a ejecutar el programa con `r`. Si gusta, antes de empezar con la ejecución, puede validar sus puntos de quiebre con `ìnfo b`.

Una vez ejecute el comando `run` o `r`, el programa se detendrá en `main`. Para que el programa siga su ejecución hasta el siguiente punto de quiebre use el comando `continue` o `c`, y el programa avanzará hasta la función `genvector`. Vuelva a ejecutar `c` para que avance hasta la función `incdouble`.

Una vez en este punto, usted puede ver cual será la siguiente instrucción en ejecutarse:

```shell
x/i $pc
```

Luego debería observar una salida **similar** a la siguiente:

```shell
=> 0x5555555546d0 <incdouble>:  addsd  xmm0,QWORD PTR [rip+0x200938]        # 0x555555755010 <uno>
```

Usted puede observar los valores del registro `xmm0`:

```shell
p $xmm0
```

Con un resultado parecido a esto:

```shell
$1 = {
  v4_float = {0, 0, 0, 0}, 
  v2_double = {0, 0}, 
  v16_int8 = {0 <repeats 16 times>}, 
  v8_int16 = {0, 0, 0, 0, 0, 0, 0, 0}, 
  v4_int32 = {0, 0, 0, 0}, 
  v2_int64 = {0, 0}, 
  uint128 = 0
}
```

Como esta función emplea _doubles_ nos podemos quedar solo con los valores en tipo _double_:

```shell
p $xmm0.v2_double
```

Si vuelve a ejecutar `netxi` terminará la función (porque la siguiente instrucción es `ret`) y volverá a la función `genvector`.

Como ejercicio, se deja al lector, que depure todo el programa y vea los valores de la variable `i` y del vector `v` para cada `i`. Cuando la función `genvector` haya concluido su ejecución vea los valores de todo el arreglo con el comando `p *v@size`. [↑](#contenido)

# Scripts

Para concluir, realizar de forma automática los procesos indicados en esta guía, se puede conseguir mediante _scripts_ basados en sentencias de gdb.

## Primer ejemplo

Se implementará un _script_ para el código de [muestra](https://github.com/alexandrojim/iee240-learning-material/wiki/Depuraci%C3%B3n-de-programas#programa-de-ejemplo). Este incluye el uso de comandos para definir y mostrar símbolos, examinar la memoria, condicionales, bucles y definiciones de comandos personalizados.

```bash
# para indicar el archivo de salida
set logging file ejemplo_gdb.txt

# para que las impresiones sean bonitas
set print pretty on

# para que comience el registro de resultados
set logging on

set pagination off

# para indicar el ejecutable
file ejemplo_gdb

# este comando imprime una variable entera en caso sea positiva
define intispos

if (unsigned int)$arg0 > 0

p (unsigned int)$arg0

end

end

# este comando examina un arreglo de floats elemento por elemento
define xarrfloat

set $i=0
while($i < (unsigned int)$arg1)
p $i
set $dir=(float*)&$arg0 + $i
x/fw $dir
set $i=$i+1
end

end

# este comando imprime todo el arreglo de floats en una sola línea
define parrfloat

print *(float*)&$arg0 @ (unsigned int)$arg1

end

# punto de quiebre en la etiqueta _start
b _start

# para correr el ejecutable
r

# imprimir la variable a si es positiva
intispos a

# examinar los elementos de b
xarrfloat b btam

# imprimir los elementos de b
parrfloat b btam

# continuar hasta el final
c

# salir de gdb
q
```

Puede usar el siguiente _script_ de bash

```bash
# en caso exista el archivo exista será eliminado
if [ -e ejemplo_gdb.txt ]; then
    rm ejemplo_gdb.txt
fi

# para generar el object file
nasm -f elf64 -g ejemplo_gdb.asm -o ejemplo_gdb.o

# para generar el ejecutable
ld ejemplo_gdb.o -o ejemplo_gdb

# para pasar el archivo de comandos a gdb
gdb -x ejemplo_gdb.gdb
``` 

Se le deja a usted como ejercicio ejecutar el _script_ y observar los resultados. [↑](#contenido)

## Segundo ejemplo:

Se implementará un _script_ para un código que imprime `hello world` la cantidad de veces que indica el argumento que se pase al programa, en caso no se pase argumentos se imprimirá la cadena solo dos veces.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{

    int cont = 0;

    if (argc == 1)
    {
        cont = 2;
    }
    else
    {
        cont = atoi(argv[1]);
    }

    while (cont > 0)
    {
        printf("hello world\n");
        cont--;
    }

    return 0;
}
```

Para depurar el código se empleará el siguiente script, arriba de cada sentencia se incluirán comentarios del propósito de cada sentencia:

```shell
# con esta sentencia se indica el archivo de salida 
# para poder ver los resultados
set logging file output.txt

# para que las salidas de print se vean bien
set print pretty on

# para que las salidas de los comandos se registren
set logging on

# para evitar que gdb haga preguntas y\n
set pagination off

# fijar el argumento del programa
set args 10

# indicar el archivo que se va a depurar
file helloworld

# fijar un breakpoint en main
b main

# fijar un breakpoint donde se imprime la cadena de texto
b 20

# hook previo para echo
define hook-echo
echo <<<---
end

# hook posterior para echo
define hookpost-echo
echo --->>>\n
end

# definimos un comando de nombre log 
# que muestra el valor de su primer argumento
define log
	printf "counter value is %d\n", $arg0
end

# aqui empieza el programa
echo INICIO

# empezar a correr el programa
r

echo ARGUMENTOS

# mostrar los valores de argc y argv
info args

echo INFO DE ARGUMENTOS 

# imprimir los elementos que componen argv
print *argv@argc

# para que continue porque hay breakpoints
c

# aqui empieza el bucle
echo BUCLE

# para que repita log y continue
# mientras que la variable cont del programa 
# es mayor que uno
while(cont > 1)
	log cont
	c
end

# aqui termina
echo FIN 

# gracias
```

Para crear el ejecutable:

```shell
gcc -g helloworld.c -o helloworld
```

Para que gdb ejecute el script:

```shell
gdb -x test.gdb
```

Se le deja a usted como ejercicio ejecutar el _script_ y observar los resultados. [↑](#contenido)

