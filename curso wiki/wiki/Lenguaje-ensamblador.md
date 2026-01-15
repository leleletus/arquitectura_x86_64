# Contenidos
* ## [Formato de un código ensamblador](#formato-de-un-código-ensamblador-1)
  * [Comentarios](#comentarios)
  * [Valores numéricos](#valores-numéricos)
  * [Definiciones](#definiciones)
  * [Sección .data](#sección-data)
  * [Sección .bss](#sección-bss)
  * [Sección .text](#sección-text)
* ## [Registros](#registros-1)
  * [Registro de banderas](#registros-de-banderas)
* ## [Modos de direccionamiento](#modos-de-direccionamiento-1)
* ## [Llamadas al Sistema](#llamadas-al-sistema-1)
* ## [Conjunto de Instrucciones](#conjunto-de-instrucciones-1)
  * [Instrucciones para mover datos](#instrucciones-para-mover-datos)
  * [Instrucciones aritméticas](#instrucciones-aritméticas)
  * [Instrucciones lógicas](#instrucciones-lógicas)
  * [Instrucciones de control](#instrucciones-de-control)
  * [Etiquetas](#etiquetas)
  * [Saltos sin condición](#saltos-sin-condición)
  * [Saltos con condición](#saltos-con-condición)
  * [Iteraciones](#iteraciones)
* ## [Ejemplos](#ejemplos-1)
  * [Imprimir cadena](#imprimir-cadena)
  * [Calcular longitud de cadena](#calcular-la-longitud-de-una-cadena)
  * [Leer cadena desde el terminal](#leer-cadena-desde-el-terminal)

# Formato de un código ensamblador

Los requerimientos de formato son específicos al ensamblador que se emplee, en el caso específico del curso se empleará _nasm_ y el **ensamblador de intel**. En caso se emplee otro ensamblador, el formato puede presentar ligeras variantes.

Un programa completo en ensamblador consiste de varias partes, pero por lo general presenta las tres siguientes:

* Sección `.data` donde los datos iniciales son declarados y definidos.
* Sección `.bss` donde se declaran y definen variables sin valor inicial.
* Sección `.text` donde se colocan las instrucciones del código.

## Comentarios

Se emplea punto y coma `(;)` para indicar el inicio del comentario. Los comentarios se pueden colocar en cualquier lugar del código. Todo caracter colocado luego del `;` será ignorado por el ensamblador y considerado como comentario. [↑](#contenidos)

## Valores Numéricos

Los valores numéricos pueden ser especificados en formato decimal, octal o hexadecimal. En _nasm_, por defecto, se emplea la base decimal. Si se desea emplear la base octal, se deberá  indicar una `q` al final del número, y si se desea emplear la base hexadecimal, el número deberá ser precedido por un `0x`. [↑](#contenidos)

## Definiciones

El valor de una definición no puede variar durante la ejecución del programa. Estas son substituidas por sus valores definidos durante el proceso de ensamblaje. Debido a esto, a las definiciones no se les asigna una dirección de memoria. Esto les da mayor flexibilidad en su uso debido a que no se les asigna un tipo de dato específico. Para realizar una definición se emplea la directiva `.equ`. [↑](#contenidos)

## Sección .data

En esta sección se ubican las variables y constantes que pueden ser leídas por todo el código (globales). Los nombres deben empezar con letras, y al momento de ser declaradas se debe indicar su nombre, tipo de dato y valor inicial. [↑](#contenidos)

Los tipos de datos que soporta _nasm_ son los siguientes:

| Declaración |          Significado         |
|:-----------:|:----------------------------:|
|      db     |      Variable de 8 bits      |
|      dw     |      Variable de 16 bits     |
|      dd     |      Variable de 32 bits     |
|      dq     |      Variable de 64 bits     |

<!-- |     ddq     | Variable entera de 128 bits  | -->
<!-- |      dt     |  Variable float de 128 bits  | -->

## Sección .bss

En esta sección se ubican las variables que no tienen valores iniciales. En su declaración se aplican las mismas reglas que en la sección `.data`, salvo que los elementos en está sección no tienen valor inicial, en este caso el valor que acompaña al tamaño indica la cantidad de elementos que se solicitan. [↑](#contenidos)

| Declaración |      Significado      |
|:-----------:|:---------------------:|
|     resb    |   Variable de 8 bits  |
|     resw    |  Variable de 16 bits  |
|     resd    |  Variable de 32 bits  |
|     resq    |  Variable de 64 bits  |

<!-- |    resdq    | Variable de 128 bits  | -->

## Sección .text

En esta sección se especifican las instrucciones, solo debe haber una por línea, y debe  incluir los operandos requeridos. Se deberán incluir algunas etiquetas que definan al programa inicial. Por ejemplo, asumiendo un programa básico que emplea  al enlazador `ld`, se deberá incluir la siguiente expresión:

```asm
section .text
    global _start
_start
```

Tenga en cuenta que esto solo se cumple cuando el enlazador es `ld`, en caso se emplee otro enlazador, el código requerido cambiará. [↑](#contenidos) 

# Registros

La memoria de un ordenador es esencialmente un arreglo de bytes que el software emplea para instrucciones y datos. Los registros son un tipo especial de memoria que permiten al CPU accesar a datos de forma muy rápida. Los CPUs x86-64 tienen 16 registros de propósito general de 64 bits y 16 registros especiales para datos en coma flotante. Esto último pueden ser de 128 a 256 bits dependiendo del modelo del CPU y permiten operar múltiples valores enteros o en coma flotante.

La lista de registros que se pueden emplear es la siguiente:

| 64-bits | 32-bits | 16-bits | 8-bits |    Significado    |
|:-------:|:-------:|:-------:|:------:|:-----------------:|
|   rax   |   eax   |    ax   |   al   |     Acumulador    |
|   rbx   |   ebx   |    bx   |   bl   |        Base       |
|   rcx   |   ecx   |    cx   |   cl   |      Contador     |
|   rdx   |   edx   |    dx   |   dl   |       Datos       |
|   rsi   |   esi   |    si   |   sil  |    Source Index   |
|   rdi   |   edi   |    di   |   dil  | Destination Index |
|   rbp   |   ebp   |    bp   |   bpl  |    Base Pointer   |
|   rsp   |   esp   |    sp   |   spl  |   Stack Pointer   |
|    r8   |   r8d   |   r8w   |   r8b  | Propósito General |

La tabla se puede extender con los registros de propósito general que fueron añadidos al procesor cuando se extendió a 64 _bits_, y van desde r8 hasta r15 que tienen las mismas características que r8 en la tabla. Otra observación que se debe hacer es que `rax`, `eax`, `ax` y `al` son porciones de un mismo registro. La imagen, a continuación, ilustra la relación entre estos:

![Registro rax](https://i.stack.imgur.com/fFSF3.png)

El gráfico aplica para todos los registros del procesador. [↑](#contenidos)

## Registros de banderas

El registro de banderas se llama `rflags` y es de 64 bits, pero solo se emplean 32 bits, por lo que para referirse a este registro es suficiente con `eflags`. Adicionalmente, el registro de banderas no es usado directamente, sino que se emplean instrucciones condicionales las cuales internamente acceden al registro de banderas y emplean una o más de estas.

La lista de banderas que se pueden emplear es la siguiente:

| Bandera |                          Descripción                          |
|:-------:|:-------------------------------------------------------------:|
|    CF   |                Carry Flag (Bandera de acarreo)                |
|    PF   |                Parity Flag (Bandera de paridad)               |
|    ZF   |                  Zero Flag (Bandera de cero)                  |
|    SF   |                  Sign Flag (Bandera de signo)                 |
|    OF   |              Overflow Flag (Bandera de desborde)              |
|    AF   |                Adjust Flag (Bandera de ajuste)                |
|    IF   | Interrupt Enable Flag (Bandera para habilitar interrupciones) |

Por lo general, el registro de banderas no es modificado directamente por el programador [↑](#contenidos).

# Modos de direccionamiento

Por su naturaleza CISC, los procesadores x86-64 admiten una variedad de modos de direccionamiento. Un modo de direccionamiento es una expresión que calcula una dirección en la memoria para leer o escribir. Estas expresiones se utilizan como origen o destino para una instrucción `mov` y otras instrucciones que acceden a la memoria. El siguiente código demuestra como escribir el valor inmediato `1` en varias ubicaciones de memoria en un ejemplo para cada uno de los modos de direccionamiento disponible. [↑](#contenidos)

```asm
    mov 0x604892,      1 ; modo directo (la dirección es un valor constante)
    mov [rax],         1 ; modo indirecto (la dirección está en un registro)
    mov [rbp-24],      1 ; modo indirecto con desplazamiento
    mov [rsp+8+4*rdi], 1 ; modo indirecto con desplazamiento y escalamiento
    mov [rsp+4*rdi],   1 ; modo indirecto con desplazamiento 0
    mov [8+4*rdi],     1 ; modo indirecto con base 8
    mov [rsp+8+rdi],   1 ; modo indirecto con escalamiento 1 
```

# Llamadas al sistema

Cuando un proceso corre en alguno de los sistemas operativos Linux, por lo general, se ejecuta en modo usuario, esto significa que el proceso está limitado a ejecutar solo un cierto grupo de instrucciones. El proceso puede mover datos entre registros dentro del programa, realizar operaciones aritmética, comparaciones, saltos, etc. pero, por ejemplo, operaciones de lectura y escritura no están permitidas.

Cuando un programa necesita hacer una operación de este tipo, se realiza una llamada al sistema. Una llamada al sistema es una llamada a función que cambia el CPU a modo _kernel_ y ejecuta una función que es parte del _kernel_. En este modo el CPU ya puede ejecutar instrucciones de lectura/escritura y entrada/salida. 

Los parámetros de las llamadas al sistema se indican en registros específicos, y estos varían dependiendo de la cantidad de bits y del _kernel_ del sistema operativo que se emplea. La siguiente tabla muestra los argumentos, y el registro asociado a cada uno:

| Registro |             Uso             |
|:--------:|:---------------------------:|
|    rax   | ID de la llamada al sistema |
|    rdi   |       Primer argumento      |
|    rsi   |      Segundo argumento      |
|    rdx   |       Tercer argumento      |
|    r10   |       Cuarto argumento      |
|    r8    |       Quinto argumento      |
|    r9    |       Sexto argumento       |

Dependiendo de la llamada al sistema que se está realizando la cantidad de parámetros variará; sin embargo, se debe tener en cuenta que el ID de la llamada al sistema siempre se deberá indicar. Las llamadas al sistema en x64 salvan el registro que apunta a la instrucción `rip` en `rcx` y luego salvan el registro de banderas en el registro `r11`, no modifican nada en la pila, ni alteran el valor de `rsp`. Tenga en cuenta esto al usar `syscall`, porque estos registros volverán con valores modificados.

Luego de que los parámetros estén fijos, se deberá ejecutar la instrucción `syscall`. Esta instrucción pondrá el programa en pausa, y le dará el control al sistema operativo, el cual ejecutará la llamada indicada en el registro `rax`. [↑](#contenidos)

# Conjunto de instrucciones

En esta sección se hará una presentación general y breve de las instrucciones; sin embargo, si usted desea puede dirigire al siguiente [enlace](https://www.felixcloutier.com/x86/) para ver una descripción más detallada.
Las instrucciones serán presentadas por funcionalidad y en el siguiente orden:

* Instrucciones para mover datos
* Instrucciones aritméticas
* Instrucciones lógicas
* Instrucciones de control

## Instrucciones para mover datos

Mover datos es una tarea fundamental en el lenguaje ensamblador. El comando básico para mover datos de/hacia un registro es `mov`. Con esta instrucción se pueden mover constantes, direcciones y contenidos de posiciones de memoria a registros, mover datos de un registro a otro y mover datos de un registro a una posición de memoria. 

```asm
    mov rax, 100 ; rax <- 100
    mov rax, a   ; rax <- a
    mov rax, [a] ; rax <- el contenido de la dirección a
    mov [a], rax ; el valor de rax se escribe en el contenido de la dirección a 
    mov rax, rbx ; rax <- rbx
```

Cuando realizamos un acceso a memoria, la mayoría de veces el tamaño del operando es obvio. Por ejemplo, la siguiente instrucción:

```asm
    mov eax, [rbx]
```

Mueve una palabra doble (32 bits); sin embargo, en algunos casos puede haber confusión sobre el tamaño del operando. Por ejemplo:

```asm
    inc [rbx]
```

Debido a que el tamaño del operando no está claro, se recomienda emplear un **calificador de tamaño** para que quede claro el tamaño del operando. Los calificadores pueden ser: byte, word, dword y qword. Con esta aclaración, el ejemplo anterior queda de la siguiente manera:

```asm
    inc byte [rbx]
```

De esta forma, el ensamblador sabe que solo debe incrementar un byte. [↑](#contenidos)

## Instrucciones aritméticas

Estas instrucciones permiten ejecutar operaciones de suma, resta, multiplicación y división sobre valores enteros.

```asm
    inc rax      ; rax <- rax + 1
    add rax, rbx ; rax <- rax + rbx
    dec rax      ; rax <- rax - 1
    sub rax, rbx ; rax <- rax - rbx
```

Cuando se usan estas instrucciones, se recomienda que los operandos sean del mismo tamaño. [↑](#contenidos)

## Instrucciones lógicas

Estas instrucciones permiten ejecutar operaciones del álgebra de Boole, bit a bit entre los operandos.

```asm
    neg rax      ; rax <- ! rax
    and rax, rbx ; rax <- rax && rbx
    or  rax, rbx ; rax <- rax || rbx
    xor rax, rbx ; rax <- rax xor rbx
```

Cuando se usan estas instrucciones, se recomienda que los operandos sean del mismo tamaño. [↑](#contenidos)

## Instrucciones de control

Para la implementación de estructuras condicionales e iterativas, y se emplean en conjunto instrucciones de comparación e instrucciones de salto. Los saltos pueden ser con condición o sin condición. [↑](#contenidos)

## Etiquetas

Una etiqueta es una ubicación en un programa, la cual será empleada por una instrucción de control. Por lo general, los nombres de las etiquetas están compuestos solo por letras, pero pueden contener números y algunos caracteres especiales; sin embargo, el uso de estos últimos no es recomendado. Luego de definir una etiqueta se deben usar los dos puntos (`:`). [↑](#contenidos)

## Saltos sin condición

Permite un salto a una etiqueta específica del programa. Para esto se emplea la instrucción `jmp`.

```asm
    jmp loopStart ; saltar a la etiqueta loopStart
    jmp ifDone    ; saltar a la etiqueta ifDone
    jmp end       ; saltar a la etiqueta end
```

La etiqueta puede estar en cualquier lugar del segmento `.text`. [↑](#contenidos)

## Saltos con condición

Un salto condicional permite implementar una estructura selectiva básica (IF-ELSE). Se requieren dos pasos: una operación aritmética y un salto especial. El salto especial se ejecutará dependiendo del resultado de la operación de comparación, el cual será almacenado en el registro de banderas. 

A continuación se presenta una tabla con algunos de los posibles saltos especiales que se pueden realizar junto con una operación de comparación (instrucción `cmp`):

| Instrucción | Resultado de cmp a, b |
|:-----------:|:---------------------:|
|      je     |         a == b        |
|     jne     |         a != b        |
|     jg      |         a > b         |
|     jge     |         a >= b        |
|      jl     |         a < b         |
|      jz     |         a == 0        |
|     jnz     |         a != 0        |

Ejemplo:

```asm
    ; si rax es menor o igual que rbx
    ; saltar a la etiqueta notNewMax
    cmp rax, rbx
    jle notNewMax
```

Tome en cuenta que la tabla no incluye todos los casos. [↑](#contenidos)

## Iteraciones

Las instrucciones básicas de control descritas proporcionan un mecanismo para crear lazos iterativos. Se puede implementar un bucle básico que consiste en un contador que se verifica en la parte inferior o superior de un bucle con un salto de comparación y condicional.

Por ejemplo, asuma que la siguiente porción de código está dentro de un programa:

```asm
    cant    dq  15      ; cantidad de iteraciones
    suma    dq  0       ; suma
```

Esta otra porción de código acumulará los enteros impares del 1 al 30:

```asm
    mov     rcx,    qword [cant]    ; contador de iteraciones
    mov     rax,    1               ; registro de impares
sumLoop:
    add     qword [suma], rax       ; acumulando
    add     rax,    2               ; siguiente impar
    dec     rcx
    cmp     rcx,    0               ; 
    jne     sumLoop
```

Existe una instrucción especial que emplea el registro rcx e instrucciones de comparación para iterar: `loop`. Su formato general de uso es el siguiente:

```asm
    loop    <etiqueta>
```

La instrucción decrementará el registro `rcx`, lo comparará con 0 y saltará a la etiqueta indicada en caso `rcx` sea distinto de cero. La etiqueta debería estar definida solo una vez y el registro `rcx` no debería ser reescrito durante su uso.

Por ejemplo, el código anterior se puede reescribir de la siguiente manera:

```asm
    mov     rcx,    qword [cant]    ; contador de iteraciones
    mov     rax,    1               ; registro de impares
sumLoop:
    add     qword [suma], rax       ; acumulando
    add     rax,    2               ; siguiente impar
    loop     sumLoop
```

La instrucción `loop` está limitada al registro `rcx` y no es recomendada para lazos anidados. [↑](#contenidos)

# Ejemplos

## Imprimir cadena

Ejemplo que imprime el mensaje `Hello World` en el terminal.

```asm
; Programa helloworld.asm
; Para ensamblar ejecutar:
; nasm -f elf64 helloworld.asm -o helloworld.o
; Para enlazar ejecutar:
; ld helloworld.o -o helloworld
; Para correr el ejecutable:
; ./helloworld

; SEGMENTO DE DATOS
; Se empleara la etiqueta message y se reservaran elementos de 8 bits
; Cada letra de la cadena se corresponde con un elemento de 8 bits
; El numero 10 se corresponde con el caracter \n
section .data                   
	message db "Hello World",10 
	len equ $ - message

; SEGMENTO DE TEXTO
section .text
	global _start

_start:
; LLAMADA AL SISTEMA
; rax => ID <= 1 : sys_write
; rdi => Primer parametro   : output
; rsi => Segundo parametro  : direccion del mensaje
; rdx => Tercer parametro  : longitud del mensaje
	mov rax, 1
	mov rdi, 1
	mov rsi, message
	mov rdx, len
	syscall
; LLAMADA AL SISTEMA
; rax => ID <= 60  : sys_exit
; rdi => Primer parametro   : 0 <= sin errores
	mov rax, 60
	mov rdi, 0
	syscall
```

## Calcular la longitud de una cadena

Modificación del ejemplo anterior para incluir comparaciones e iteraciones.

```asm
; Programa helloworldlen.asm
; Para ensamblar ejecutar:
; nasm -f elf64 helloworldlen.asm -o helloworldlen.o
; Para enlazar ejecutar:
; ld helloworldlen.o -o helloworldlen
; Para correr el ejecutable:
; ./helloworldlen

; SEGMENTO DE DATOS
; Se empleara la etiqueta message y se reservaran elementos de 8 bits
; Cada letra de la cadena se corresponde con un elemento de 8 bits
; El numero 10 se corresponde con el caracter \n
; El numero 0 se emplea como fin de cadena
section .data
	message db "Hello World",10,0

; SEGMENTO DE TEXTO
section .text
	global _start

; rax apunta al principio de la cadena
; rbx se empleara como contador
; nos desplazamos a lo largo de la cadena hasta encontrar un cero
; cuando rax vale cero dejamos de iterar
; en rbx se encuentra la longitud de la cadena
_start:
	mov	rax, message
	mov	rbx, 0

_countLoop:
	inc	rax
	inc	rbx
	mov	cl, [rax]
	cmp	cl, 0
	jne	_countLoop

; SYS_WRITE
	mov 	rax, 1
	mov 	rdi, 1
	mov 	rsi, message
	mov	rdx, rbx
	syscall

; SYS_EXIT
	mov	rax, 60
	mov	rdi, 0
	syscall
```

## Leer cadena desde el terminal

Ejemplo que lee datos de entrada y los imprime en el terminal.

```asm
; Programa getname.asm
; Para ensamblar ejecutar:
; nasm -f elf64 getname.asm -o getname.o
; Para enlazar ejecutar:
; ld getname.o -o getname
; Para correr el ejecutable:
; ./getname

; SEGMENTO DE DATOS
section .data
	question db "What is your name? "
	lenq equ $ - question
	greet db "Hello, "
	leng equ $ - greet

; SEGMENTO BSS (Block Started by Symbol)
; Reservamos 16 bytes para el nombre que sera ingresado 
section .bss
	name resb 16

; SEGMENTO DE TEXTO
section .text
	global _start

; SYS_WRITE
_start:
	mov rax, 1
	mov rdi, 1
	mov rsi, question
	mov rdx, lenq
	syscall

; SYS_READ
	mov rax, 0
	mov rdi, 0
	mov rsi, name
	mov rdx, 16
	syscall

; SYS_WRITE
	mov rax, 1
	mov rdi, 1
	mov rsi, greet
	mov rdx, leng
	syscall

; SYS_WRITE
	mov rax, 1
	mov rdi, 1
	mov rsi, name
	mov rdx, 16
	syscall

; SYS_EXIT
	mov rax, 60
	mov rdi, 0
	syscall
```
