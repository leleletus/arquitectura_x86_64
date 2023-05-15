	global asmFloatNormTwo ;se decara la funcion para poderla usar en otros
	section .text

;En el código que proporcionó, 
;rdi se utiliza para almacenar la dirección del vector cuya norma-2 se está calculando. 
;En cada iteración del bucle, se incrementa en 4 bytes (el tamaño de un flotante) 
;para apuntar al siguiente elemento del vector. rsi, por otro lado, 
;se utiliza para almacenar el número de elementos en el vector y se decrementa en cada iteración del bucle.
	
asmFloatNormTwo:
	xorpd	xmm0,	xmm0 ; ponemos a 0 los registros
	xorpd	xmm1,	xmm1
	cmp	rsi,	0 	;comparo el valor de rs1 con 0
	je	done ;si la conmparacion cumple (rsi=0) saltamos a done

next: ; nuestro bulce hasta que se cumpla el rsi=0
	movss	xmm0,	[rdi] ;mueve el valor rdi a xmm0 
	mulss	xmm0,	xmm0 ;multipliplica el valor de xm0 por si mimso y se guarda ahi
	addss	xmm1,	xmm0 ;guardo el resuldado de xmm0 a xmm1
	add	rdi,	4
	sub	rsi,	1
	jnz	next	
done:
	sqrtss	xmm1,	xmm1
	movss	xmm0,	xmm1
	ret