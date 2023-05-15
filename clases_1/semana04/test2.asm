;nasm -f elf64 -g test2.asm -o test2.o && ld test2.o -o test2 && ./test2
;gdb

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
    mov rbx, [arreglo+8*rcx]  ;usar b en vez de a cuando usamos div y mul para no tener problemas 
    add r8,rbx
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
    
;debe salir 431