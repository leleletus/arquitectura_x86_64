
; Para ensamblar ejecutar:
; nasm -f elf64 encontrar_pares.asm -o encontrar_pares.o
; Para enlazar ejecutar:
; ld encontrar_pares.o -o encontrar_pares
; Para correr el ejecutable:
; ./encontrar_pares

;para compilar todo de una:
;  nasm -f elf64 -g encontrar_pares.asm -o encontrar_pares.o && ld encontrar_pares.o -o encontrar_pares && ./encontrar_pares
; agregamos la bandera -g para mas info al depurar en gdb



; SEGMENTO DE DATOS
; Se empleara la etiqueta de las variables y se reservaran elementos de 16 bits
section .data                   
	inf dw -5 ;defineword es de 16bits= 2bytes
    sup dw 4
    sum dw 2

;SEGMENTO DE RESERVA DE VARIABLES SIN VALORES INICIALES
;como cada dato es de 2 bytes, reservamos 8 bytes para tener 4 datos
section .bss
x resw 8
y resw 8


; SEGMENTO DE TEXTO
section .text
    global _start



_start:
    xor r15w, r15w  ;inicializamos en 0 sera mi cant_pares
    xor r14w, r14w ; inicializamos en 0 mi contador i
    xor r13w, r13w  ;inicializamos en 0 sera mi tempx
    xor r12w, r12w ; inicializamos en 0 sera mi tempy

    mov r14w, inf ;le damos el valor a nuestro contador del inferior

_countLoop:    ;inicio del loop


    xor r13w, r13w  ;inicializamos en 0 sera mi tempx
    xor r12w, r12w ; inicializamos en 0 sera mi tempy

;parte del if
    xor r11w, r11w ; inicializamos en 0 sera mi tempy
    sub r13w, r14w
    cmp r13w, 

    inc r14w      ; Incrementamos su valor
    cmp r14w,sup    ; Comparamos con el sup
    jle loop1   ; si es menor o igual repite
;fin del loop












; LLAMADA AL SISTEMA SYS_EXIT
; rax => ID <= 60  : sys_exit
; rdi => Primer parametro   : 0 <= sin errores
	mov rax, 60
	mov rdi, 0
	syscall

