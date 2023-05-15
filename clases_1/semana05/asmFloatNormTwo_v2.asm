	    global asmFloatNormTwo
	    section .text



asmFloatNormTwo:
    xorpd xmm0, xmm0 ;con que limpie con un xor esta bien
    xorpd xmm1, xmm1
    cmp rsi, 0
    je done

next:
    movss xmm0, [rdi]
    mulss xmm0, xmm0
    addss xmm1, xmm0
    add rdi, 4
    sub rsi, 1
    jnz next

done:
    sqrtss xmm1, xmm1
    movss [rdx], xmm1



;nasm -f elf64 asmFloatNormTwo.asm -o asmFloatNormTwo.o -g
;gcc asmFloatNormTwo.o norma_2_main.c -o norma_2 -lm
;./norma_2

