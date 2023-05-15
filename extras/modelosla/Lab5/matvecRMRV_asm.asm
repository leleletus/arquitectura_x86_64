global matvecRMRV_asm
section .text

matvecRMRV_asm:
;RDI = A[0] / RSI = x[0] / RDX = b[0] / RCX = N

  xorpd xmm0, xmm0 ; tmp = 0.0
  xorpd xmm1, xmm1
  xorpd xmm2, xmm2
  xorpd xmm3, xmm3

  mov r15, rcx
  mov r14, 0 
for_i:

    xorpd xmm0, xmm0 ; tmp = 0.0
    mov r10, rdi
    mov r9, rsi
    mov r13, rcx
    add r10, r14
for_j:

    movsd xmm1,[r10]
    movsd xmm2, [r9]
    mulsd xmm1, xmm2
    addsd xmm0, xmm1
    add r10, 8
    add r9, 8
    dec r13
    jnz for_j

fin_lazo:
    movsd [rdx], xmm0    
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
    jnz for_i   

done:
    ret     

; nasm -f elf64 matvecRMRV_asm.asm -o matvecRMRV_asm.o  
; gcc -shared funciones_c.c matvecRMRV_asm.o -o funciones.so 
; python3 funciones_py.py 



  
