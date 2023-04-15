;nasm -f elf64 -g test.asm -o test.o && ld test.o -o test && ./test

section .data
    num1 dw 45,350 ;defineword es de 16bits= 2bytes

section .bss
    resultado resw 1
    ;para verlo x/h &resultado     no x/b porque tomaria el menor y -122
    ;info r rax

section .text
global _start

_start: ;primero guardamos en los registros lo que quiero multiplicar
    mov ax, [num1]  ;ax solo puede almacenar 2 bytes asi que solo toma 2 primeros bytes que seria el 45
    mov r8w, [num1+2]; dentro del corchete la direcion de memoria num1+ 2 bytes mas (que seria donde empieza el 350) (como los arreglos)
    mul r8w
    
    mov [resultado], ax

_exit: ;(salgo del programa)
	mov rax, 60
	mov rdi, 0
	syscall
    
