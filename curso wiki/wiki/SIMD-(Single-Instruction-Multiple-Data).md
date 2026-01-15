# Contenidos
* ## [Unidad SIMD](#unidad-simd-1)
* ## [Registros SIMD](#registros-simd-1)
* ## [Instrucciones SIMD](#instrucciones-simd-1)
    * [Intrucciones de transferencia para vectores de elementos en punto flotante](#instrucciones-de-transferencia-para-vectores-de-elementos-en-punto-flotante)
    * [Instrucciones aritméticas para vectores de elementos en punto flotante](#instrucciones-aritméticas-para-vectores-de-elementos-en-punto-flotante)
    * [Intrucciones de comparación para vectores de elementos en punto flotante](#intrucciones-de-comparación-para-vectores-de-elementos-en-punto-flotante)
    * [Intrucciones para chocolatear vectores de elementos en punto flotante](#intrucciones-para-chocolatear-vectores-de-elementos-en-punto-flotante)
    * [Intrucciones lógicas para vectores de elementos en punto flotante](#intrucciones-lógicas-para-vectores-de-elementos-en-punto-flotante)
* ## [Ejemplo](#ejemplo-1)

# Unidad SIMD

En [otra](Punto-Flotante-y-Convenciones-de-llamadas-a-funci%C3%B3n-en-64-bits) guía se hizo un comentario breve de la unidad **SIMD** y del uso de los registros **XMM** para operaciones con números en punto flotante. En esta guía se presentará una extensión del conjunto de instrucciones SSE para operaciones vectoriales con números en punto flotante. [↑](#contenidos)

# Registros SIMD

Como ya se mencionó, hay un conjunto dedicado de registros, referidos como registros **XMM**, empleados para dar soporte a las instrucciones en punto flotante. Estos mismos registros dan soporte a las instrucciones en vectoriales y dependiendo del tipo de dato podrán almacenar una cantidad diferente de elementos. Por ejemplo, el registro **xmm0** por ser de 128 bits puede contener **4 floats**, o **2 doubles**. [↑](#contenidos)

# Instrucciones SIMD

La presentación de las instrucciones para operaciones vectoriales será breve. Solo serán cubiertas las más básicas y serán presentadas en el siguiente orden:

* Instrucciones de transferencia para vectores de elementos en punto flotante.
* Instrucciones aritméticas para vectores de elementos en punto flotante.
* Intrucciones de comparación para vectores de elementos en Punto flotante.
* Intrucciones para chocolatear vectores de elementos en punto flotante.
* Intrucciones lógicas para vectores de elementos en punto flotante.

Para una lista completa de las instrucciones se puede revisar el siguiente [enlace](https://www.felixcloutier.com/x86/index.html). Como observación se menciona que para hacer uso de estas instrucciones se recomienda que los datos en memoria tengan un alineamiento de 16 bits. [↑](#contenidos)

## Instrucciones de transferencia para vectores de elementos en punto flotante

Estas instrucciones permiten transferir múltiples datos de una posición de memoria a un registro, y de un registro a una posición de memoria y de un registro a otro registro. La cantidad de datos que se transfieren dependen del tipo de dato. [↑](#contenidos)

```asm
    movaps xmm0, [a]    ; mover 4 floats desde a al registro xmm0
    movapd [b], xmm1    ; mover 2 doubles del registro xmm1 a b
    movaps xmm2, xmm0   ; mover 4 floats en xmm0 a xmm2
```

## Instrucciones aritméticas para vectores de elementos en punto flotante

Estas instrucciones permiten realizar las operaciones aritméticas básicas sobre múltiples datos. [↑](#contenidos)

```asm
    movapd xmm0, [a]    ; mover 2 doubles desde a al registro xmm0
    movapd xmm1, [b]    ; mover 2 doubles desde b al registro xmm1
    addpd  xmm1, xmm0   ; suma a[0] con b[0], y a[1] con b[1]
```

Se pueden realizar ejemplos análogos para las siguientes instrucciones:

```asm
    ; addps : suma de vectores de floats
    ; addpd : suma de vectores de doubles
    ; subps : resta de vectores de floats
    ; subpd : resta de vectores de doubles
    ; mulps : producto de vectores de floats
    ; mulpd : producto de vectores de doubles
    ; divps : division de vectores de floats
    ; divpd : division de vectores de doubles
```

## Intrucciones de comparación para vectores de elementos en punto flotante

Se realizan comparaciones elemento a elemento. [↑](#contenidos)

```asm
    ; cmpps : compara vectores de floats elemento a elemento.
    ; cmppd : compara vectores de doubles elemento a elemento.
```

## Intrucciones para chocolatear vectores de elementos en punto flotante

Son instrucciones que permiten reordenar los elementos del primer y segundo operando de acuerdo a los valores de un tercer operando que es llamado máscara. [↑](#contenidos)

```asm
    ; shufps : para vectores de floats
    ; shufpd : para vectores de doubles
```

Ejemplos:

Solo se hará ejemplo gráfico para este primer caso:

![shufps_ejemplo](https://github.com/alexandrojim/iee240-learning-material/blob/master/imgsWiki/simd/reg_xmm.jpeg)

A partir de este se podrán comprender todos los demás ejemplos.

```asm
    ; Dados dos vectores u y v de floats
    ; u: {1.0, 2.0, 3.0, 4.0}
    ; v: {5.0, 6.0, 7.0, 8.0}
    ; Asumiendo que xmm1 tiene el valor de u y xmm2 el valor de v
    shufps xmm1, xmm2, 11001100b 
    ; en u el valor resultante es:
    ; u: {5.0, 8.0, 1.0, 4.0}
```

```asm
    ; Dados dos vectores u y v de floats
    ; u: {1.0, 2.0, 3.0, 4.0}
    ; v: {5.0, 6.0, 7.0, 8.0}
    ; Asumiendo que xmm1 tiene el valor de u y xmm2 el valor de v
    shufps xmm1, xmm2, 01111001b 
    ; en u el valor resultante es:
    ; u: {7.0, 5.0, 2.0, 3.0}
```

```asm
    ; Dados dos vectores u y v de floats
    ; u: {1.0, 2.0, 3.0, 4.0}
    ; v: {5.0, 6.0, 7.0, 8.0}
    ; Asumiendo que xmm1 tiene el valor de u y xmm2 el valor de v
    shufps xmm2, xmm1, 01111001b
    ; en u el valor resultante es:
    ; u: {3.0, 1.0, 6.0, 7.0}
```

```asm
    ; Dados dos vectores u y v de floats
    ; u: {1.0, 2.0, 3.0, 4.0}
    ; v: {5.0, 6.0, 7.0, 8.0}
    ; Asumiendo que xmm1 tiene el valor de u y xmm2 el valor de v
    shufps xmm1, xmm1, 10001100b 
    ; en u el valor resultante es:
    ; u: {2.0, 4.0, 1.0, 4.0}
```

## Intrucciones Lógicas para vectores de elementos en punto flotante

Son instrucciones que permiten ejecutar operaciones booleanas bit a bit en vectores de elementos en punto flotante. [↑](#contenidos)
 
```asm
    ; andps : AND bit a bit para vectores de floats
    ; andpd : AND bit a bit para vectores de doubles
    ; orps  : OR bit a bit para vectores de floats
    ; orpd  : OR bit a bit para vectores de doubles
    ; xorps : XOR bit a bit para vectores de floats
    ; xorpd : XOR bit a bit para vectores de doubles
```

# Ejemplo

Código en ensamblador que suma vectores de _floats_ usando SIMD.

```asm
	global asmVecSum
	section .text
asmVecSum:
	xorpd	xmm0, xmm0
	xorpd	xmm1, xmm1
	cmp	rcx, 0
	je 	done
next:
	movaps	xmm0, [rdi]
	movaps	xmm1, [rsi]
	addps	xmm0, xmm1
	movaps  [rdx], xmm0
	add	rdi, 16
	add	rsi, 16
	add	rdx, 16
	sub	rcx, 4
	jnz 	next
done:
	ret
```

Para ensamblar:

```shell
nasm -f elf64 asmVecSum.asm -o asmVecSum.o
```

Código principal en C que llama a la función en ensamblador:

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void genVectors(float *v, int TAM);
void cVecSum(float *v, float *u, float *w, int TAM);
extern void asmVecSum(float *v, float *u, float *w, int TAM);

int main(){

	srand(time(NULL));
	float *v, *u, *wc, *wasm;
	int N = 16;
	int REPS = 20, j = 0;

	posix_memalign((void **)&v, 16, N * sizeof(float));

	posix_memalign((void **)&u, 16, N * sizeof(float));

	posix_memalign((void **)&wc, 16, N * sizeof(float));

	posix_memalign((void **)&wasm, 16, N * sizeof(float));

	genVectors(v, N);
	
	genVectors(u, N);

	cVecSum(v,u,wc,N);	

	asmVecSum(v,u,wasm,N);
	
	for(j = 0; j < N; j++){
		printf("%f\t%f\n",wc[j],wasm[j]);
	}	

	return 0;
}

void genVectors(float *v, int TAM){
	int i = 0;
	float ele = 0.0;
	for(i = 0; i < TAM; i++){
		ele = (float)(rand()%100);
		ele = (sinf(ele) + cosf(ele)) / 1.4142;
		v[i] = ele;
	}
}

void cVecSum(float *v, float *u, float *w, int TAM) {
	int i = 0;
	for(i = 0; i < TAM; i++){
		w[i] = v[i] + u[i];
	}
}
```

Para generar el ejecutable:

```shell
gcc asmVecsum.o example.c -o example -lm
```
