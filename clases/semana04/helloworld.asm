; Programa helloworld.asm
; Para ensamblar ejecutar:
; nasm -f elf64 helloworld.asm -o helloworld.o
; Para enlazar ejecutar:
; ld helloworld.o -o helloworld
; Para correr el ejecutable:
; ./helloworld

;https://github.com/stefano-sosac/iee240-learning-material/wiki/Lenguaje-ensamblador
;para compilar todo de una:
;  nasm -f elf64 helloworld.asm -o helloworld.o && ld helloworld.o -o helloworld && ./helloworld

; SEGMENTO DE DATOS
; Se empleara la etiqueta message y se reservaran elementos de 8 bits
; Cada letra de la cadena se corresponde con un elemento de 8 bits
; El numero 10 se corresponde con el caracter \n
section .data                   
	message db "Hello World",10 ; el 10 está para el salto de linea
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