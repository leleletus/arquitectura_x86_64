global func1_asm
section .text

func1_asm:
;RDI = arr[0] / RSI = suma[0] / RDX = mul[0] / RCX = N
  xorpd xmm0, xmm1
  xorpd xmm1, xmm1
  xorpd xmm2, xmm2
  xorpd xmm3, xmm3
  xorpd xmm4, xmm4
  movss xmm0, [rdi]
  add rdi, 4
  movss xmm1, [rdx]
  movss xmm4, [rdi] 
  mulss xmm1, xmm4
  sub rcx, 2

lazo: 
  add rdi, 4
  movss xmm2, [rdi]
  addss xmm0,xmm2
  sub rcx,1
  jz done
  add rdi, 4
  movss xmm3, [rdi]
  mulss xmm1, xmm3
  sub rcx,1
  jnz lazo

done:  
  movss [rsi], xmm0
  movss [rdx], xmm1
  ret

  ;nasm -f elf64 func1_asm.asm -o func1_asm.o
  ;gcc -shared func1_c.c func1_asm.o -o funciones.so
  ;python3 func1_py.py