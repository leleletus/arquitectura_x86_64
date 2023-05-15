global func2_asm
section .text

func2_asm:
;RDI = arr[0] / RSI = suma[0] / RDX = mul[0] / RCX = N
  xorpd xmm0, xmm0
  xorpd xmm1, xmm1
  xorpd xmm2, xmm2
  xorpd xmm3, xmm3
  movss xmm0, [rdi]
  add rdi, 4
  movss xmm1, [rdi]
  sub rcx, 2

lazo: 
  add rdi, 4
  movss xmm2, [rdi]
  addss xmm0,xmm2
  sub rcx,1
  add rdi, 4
  movss xmm3, [rdi]
  mulss xmm1, xmm3
  sub rcx,1
  jnz lazo

done:  
  movss [rsi], xmm0
  movss [rdx], xmm1
  ret

  ;nasm -f elf64 func2_asm.asm -o func2_asm.o
  ;gcc -shared func2_c.c func2_asm.o -o funciones.so
  ;python3 func2_py.py
