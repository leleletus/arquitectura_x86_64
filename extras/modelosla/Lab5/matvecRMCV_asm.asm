global matvecRMCV_asm
section .text

matvecRMCV_asm:
;RDI = A[0] / RSI = x[0] / RDX = b[0] / RCX = N

    xorpd xmm0, xmm0 ; tmp = 0.0
    xorpd xmm1, xmm1
    xorpd xmm2, xmm2
    xorpd xmm3, xmm3

    mov r15, rcx
    mov r14, 0

for_j:
    xorpd xmm0, xmm0 ; tmp = 0.0
    mov r10, rdi
    mov r9, rsi
    mov r13, rcx
    add r10, r14 

for_i:

    movsd xmm1,[r10]
    movsd xmm2, [r9]
    movsd xmm3, [rdx]
    mulsd xmm1, xmm2
    addsd xmm3, xmm1
    add r10, 8
    add r9, 8
    dec r13
    jnz for_i  

fin_lazo:
    movsd [rdx], xmm3
    add rdx, 8
    add r14, rcx
    add r14, rcx
    add r14, rcx
    add r14, rcx
    add r14, rcx
    add r14, rcx
    add r14, rcx
    add r14, rcx
    dec r15
    jnz for_j

done:
    ret       

; nasm -f elf64 matvecRMCV_asm.asm -o matvecRMCV_asm.o   
; gcc -shared funciones_c.c matvecRMCV_asm.o -o funciones.so 
; python3 funciones_py.py 