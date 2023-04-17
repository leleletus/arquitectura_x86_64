	    global suma_float
	    section .text

	
	;xmm0 <- a
    ;xmm1 <- b
    ;retorna por xmm0
	suma_float:
		addss xmm0,xmm1 ; va a acumular la suma rdi
		ret ; retorna



;nasm -f elf64 suma_float.asm -o suma_float.o -g
;gcc suma_float.o suma_float.c -o suma_float
;./suma_float



;gdb suma_float
;gdb set-disassembly-favor intel
;break suma_float
;disassemble
;info r xmm0   (hay una menor en la wiki para ver)
;p %xmm0      o       p %xmm0.v4_float      si estamos en float





;xor ps    y xor pd si usamos para limpair por package