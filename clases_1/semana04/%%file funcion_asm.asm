%%file funcion_asm.asm

; SEGMENTO DE DATOS
;como usaremos como funcion externa no sera necesario

; SEGMENTO BSS (Block Started by Symbol)
;reserva espacio para un valor no inicializado

; SEGMENTO DE TEXTO
section .text
	global _start   ; hace el _start visible al linkeador

_start: ;definimos la etiqueta start como se establecio en .text la global

    push ebp ; guarda el valor del puntero de la pila
    mov ebp, esp ; mueve el puntero de la pila al marco de la pila actual
    push ebx ; guarda el valor de ebx
    push esi ; guarda el valor de esi
    push edi ; guarda el valor de edi
    mov eax, [ebp+8] ; mueve el primer argumento (L) a eax
    mov ecx, [ebp+12] ; mueve el segundo argumento (tam) a ecx
    xor edx, edx ; inicializa edx en 0
    mov [ebp+20], edx ; inicializa cantidad en 0
    xor ebx, ebx ; inicializa ebx en 0 (contador del bucle)
.loop:
    cmp ebx, ecx ; compara el contador con tam
    jge .endloop ; si el contador es mayor o igual a tam, salta al final del bucle
    mov edx, [eax+ebx*4] ; mueve L[i] a edx
    xor edi, edi ; inicializa edi en 0
    div dword [ebp+16] ; divide L[i] por N y guarda el resto en edi
    cmp edi, 0 ; compara el resto con 0
    jne .nodivisible ; si el resto no es 0, salta a .nodivisible
    inc dword [ebp+20] ; incrementa cantidad en 1
    mov eax, [ebp+24] ; mueve arreglo_output a eax
    mov dword [eax+ebx*4], 1 ; establece arreglo_output[i] en 1
    jmp .next ; salta a .next
.nodivisible:
    mov eax, [ebp+16] ; mueve N a eax
    xor edx, edx ; inicializa edx en 0
    div dword [eax+ebx*4] ; divide N por L[i] y guarda el resto en edx
    cmp edx, 0 ; compara el resto con 0
    jne .nomultiplo ; si el resto no es 0, salta a .nomultiplo
    inc dword [ebp+20] ; incrementa cantidad en 1
    mov eax, [ebp+24] ; mueve arreglo_output a eax
    mov dword [eax+ebx*4], 1; establece arreglo_output[i] en 1
    jmp .next; salta a .next
.nomultiplo:
    mov eax, [ebp+24]; mueve arreglo_output a eax
    mov dword [eax+ebx*4], 0; establece arreglo_output[i] en 0 
.next:
    inc ebx; incrementa el contador del bucle en 1 
    mov eax, [ebp+8]; mueve L a eax 
    jmp .loop; salta al inicio del bucle 
.endloop:
    pop edi; restaura el valor de edi 
    pop esi; restaura el valor de esi 
    pop ebx; restaura el valor de ebx 
    pop ebp; restaura el valor de ebp 
    ret; devuelve el control al código que llamó a la función
