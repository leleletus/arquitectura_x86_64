;nasm -f elf64 -g test.asm -o test.o && ld test.o -o test && ./test

section .data
    arreglo dq 45,250,1000 ; 64 bits = 8bytes
    len equ $ - arreglo

section .bss
    resultado resq 1
    ;para verlo x/h &resultado     no x/b porque tomaria el menor y -122

section .text
    global _start

_start: ;
    xor r8,r8 ;aqui acumulare
    xor rcx,rcx
    xor  rdx,rdx
    mov r9, len 
    mov r10, 8
    div r10   ; rax=len verdadero
lazo:
    mov rax, [arreglo+8*rcx]  ;
    add r8,rax
    inc rcx ; incremento
    cmp rcx,r9
    jnz lazo ; si no es 0
    
    xor rdx,rdx ;limpiamos por si acaso
    mov rax, r8 ; guardamos la suma acumulada en rax
    div rcx  ; o r9,
    mov [resultado], rax   ;guardamos el resultado (cociente)

_exit: ;(salgo del programa)
	mov rax, 60
	mov rdi, 0
	syscall
    
