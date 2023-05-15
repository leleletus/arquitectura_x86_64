		global suma_int
	section .text

	
	;rdi <- a  (valdra a)
	;rsi <- v 
	;retorna por rax
	suma_int:
		add rdi,rsi ; va a acumular la suma rdi
		mov rax,rdi	; lo mueve a rax
		ret ; retorna

;-g para usar desamblaje gdb
; gcc compila y linkea


;nasm -f elf64 suma_int.asm -o suma_int.o -g
;gcc suma_int.o suma_entera.c -o suma_int
;./suma_int


;usamos comandos para depurar en gcc