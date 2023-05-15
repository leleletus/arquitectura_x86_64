; Programa getname.asm
; Para ensamblar ejecutar:
; nasm -f elf64 getname.asm -o getname.o
; Para enlazar ejecutar:
; ld getname.o -o getname
; Para correr el ejecutable:
; ./getname

;https://github.com/stefano-sosac/iee240-learning-material/wiki/Lenguaje-ensamblador
;para compilar todo de una:
;  nasm -f elf64 -g getname.asm -o getname.o && ld getname.o -o getname && ./getname
; agregamos la bandera -g para mas info al depurar en gdb


;para hacer permanetnte el disassemble en modo inte:
;  echo "set disassembly-flavor intel" >> ~/.gdbinit
;  cat  ~/.gdbinit
;  show disassembly-flavor                muentra en cual está, dentro de gdb 

;dentrooo del gdb:
;set disassembly-flavor intel    
;break     (name del apodo) ejemplo _start

;info break           para borrar un breakpoint 
;delete 2 3

;  c     para continuar corriendo hasta el proximo breakpoint

;run 
;disassemble    (para ver en donde está)

;ni                       ára avanzar una instruccion
;disassemble

;info r rax            para ver info de un registro

;q    para cerrar




; SEGMENTO DE DATOS
section .data
	question db "Cual es tu nombre? " ;definet world de 16 bits
	lenq equ $ - question ;restamos el current location $ con  el inicio de question
	greet db "Hola, "
	leng equ $ - greet

; SEGMENTO BSS (Block Started by Symbol)
; Reservamos 16 bytes para el nombre que sera ingresado 
section .bss
	name resb 16 ; reserva espacio para un valor no inicializado

; SEGMENTO DE TEXTO
section .text
	global _start   ; hace el _start visible al linkeador

;se pueden poner a 0 una variable con xor a ella misma <----------

_start: ;definimos la etiqueta start como se establecio en .text la global

; SYS_WRITE 
	mov rax, 1 ;se mueve 1 al registro
	;en este caso 1 es el número de llamada al sistema para sys_write
	;que escribe datos en un descriptor de archivo
	mov rdi, 1 ;1 es el descriptor de archivo para la salida estándar (stdout) "terminal"
	mov rsi, question ; mueve la dirección de la cadena question al registro rsi. 
	;Este es el búfer que se escribirá en stdout
	;la cadena de texto a mostrar
	mov rdx, lenq; mueve el valor de lenq al registro rdx. 
	;Este es el número de bytes a escribir desde el búfer.
	;la cantidad de bytes del texto a mostrar
	syscall ;realiza una llamada al sistema. escribirá la cadena question en stdout "terminal"

; SYS_READ (leo)
	mov rax, 0 ;es el número de llamada al sistema para sys_read,
	;que lee datos de un descriptor de archivo.
	mov rdi, 0 ;es el descriptor de archivo para la entrada estándar (stdin)
	mov rsi, name ; búfer donde se almacenarán los datos leídos
	;donde se guardara su nombre
	mov rdx, 16 ;es el número máximo de bytes a leer
	;la cantidad de bytes del texto a guardar
	syscall ;llama al siste,a, leerá hasta 16 bytes de stdin y los almacenará en el búfer name

; SYS_WRITE (escribo el hola)
	mov rax, 1
	mov rdi, 1
	; usamos igualmente los 2 anteriores
	mov rsi, greet ;aqui ponemos el texto a escribir
	mov rdx, leng ; el tamaño del texto
	syscall ;llamada al sistema para que lo haga

; SYS_WRITE (escribo su nombre)
	mov rax, 1
	mov rdi, 1 ;los 2 primeros iguales
	mov rsi, name ;ponemos el texto a escribir
	mov rdx, 16 ;el tamaño del texto
	syscall ;llamamos al sistema a que lo haga

; SYS_EXIT (salgo del programa)
	mov rax, 60 ;60 es el número de llamada al sistema para sys_exit, 
	;que termina la ejecución del programa
	mov rdi, 0 ;Este es el código de salida del programa
	syscall ;terminará la ejecución del programa con un código de salida de 0


;practicamente en rax se le dice el codigo a seguir al syscall,
; 0 para escribir, 1 para leer y 60 para acabar el programa
;rdi para leer u escrobor ogial que rax pero al usar salir del programa =0
;rsi donde va la cadena de texto
;rdx donde ba su tamaño
;syscall para acabar




; despues del dissasemble:

;0x0000000000401000 <+0>:     mov    eax,0x1
;   0x0000000000401005 <+5>:     mov    edi,0x1
 ;  0x000000000040100a <+10>:    movabs rsi,0x402000
  ; 0x0000000000401014 <+20>:    mov    edx,0x13
   ;0x0000000000401019 <+25>:    syscall 
   ;0x000000000040101b <+27>:    mov    eax,0x0
   ;0x0000000000401020 <+32>:    mov    edi,0x0
   ;0x0000000000401025 <+37>:    movabs rsi,0x40201c
   ;0x000000000040102f <+47>:    mov    edx,0x10
   ;0x0000000000401034 <+52>:    syscall 
   ;0x0000000000401036 <+54>:    mov    eax,0x1
   ;;;;0x000000000040103b <+59>:    mov    edi,0x1
   ;0x0000000000401040 <+64>:    movabs rsi,0x402013
   ;0x000000000040104a <+74>:    mov    edx,0x7
   ;0x000000000040104f <+79>:    syscall 
   ;;0x0000000000401051 <+81>:    mov    eax,0x1
   ;;;;0x0000000000401056 <+86>:    mov    edi,0x1
   ;0x000000000040105b <+91>:    movabs rsi,0x40201c
   ;0x0000000000401065 <+101>:   mov    edx,0x10
   ;0x000000000040106a <+106>:   syscall 
   ;0x000000000040106c <+108>:   mov    eax,0x3c
   ;0x0000000000401071 <+113>:   mov    edi,0x0
   ;0x0000000000401076 <+118>:   syscall 




; MUL //siempre en el ax
;https://www.felixcloutier.com/x86/mul

;MUL r/m8      AX := AL ∗ r/m8        se guarda en ax ( o sea sobreescribe todo)
;MUL r/m16     DX:AX := AX ∗ r/m16      ( se guarda en esos 2 con dx mas significativo)


;ejemplo de multi 3*4:
   ;mov al,3
   ;mov bl,4
   ;mul bl            ;ax=12

;pero si usas uno mas grande:
   ;mov rax,3
   ;mov rbx,4
   ;mul rbx            ;rax=12 y rdx=0   
;si tenias un contador en rdx valiste, f


; posibles problemas con div
; https://www.felixcloutier.com/x86/div

;DIV r/m8	;entonces seria ax/(r/m8)  dando  AL := Quotient, AH := Remainder.
;DIV r/m16	;entonces seria DX:AX/(r/m16) dando AX := Quotient, DX := Remainder.
;saldria cualquier cosa si esque tenemos valores en dx ya que lo toma parte significativa de la division

;mov ax,13
;mov bl,5
;div bl               ;al=2 y ah=3

;para poder usar el de 16 bits sin problemas:

; xor edx,edx    ; limpiamos el registro con 0
;mov eax,13
;mov ebx,5
;div ebx           ;eax=2  y edx=3







