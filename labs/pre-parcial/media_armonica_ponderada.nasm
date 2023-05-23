
; media_armonica_ponderada
; Calcula la media armónica ponderada de un arreglo de números enteros
; Argumentos:
;   xn - puntero al arreglo de números enteros
;   xp - puntero al arreglo de pesos enteros
;   n - número de elementos en los arreglos
; Devuelve:
;   El resultado en st0

section .text
global media_armonica_ponderada

media_armonica_ponderada:
    ; Guardar los registros en la pila
    push ebp
    mov ebp, esp
    push ebx
    push esi
    push edi

    ; Inicializar variables locales
    xor eax, eax ; M = 0
    xor ebx, ebx ; i = 0
    fldz ; suma_inversas = 0.0

    ; Calcular M = sum(xp)
    mov ecx, [ebp + 16] ; ecx = n
    mov esi, [ebp + 12] ; esi = xp
.loop_M:
    cmp ebx, ecx ; i < n?
    jge .end_loop_M ; si no, salir del bucle
    add eax, [esi] ; M += xp[i]
    add esi, 4 ; xp++
    inc ebx ; i++
    jmp .loop_M
.end_loop_M:

    ; Calcular suma_inversas = sum(xp[i] / xn[i])
    xor ebx, ebx ; i = 0
    mov ecx, [ebp + 16] ; ecx = n
    mov esi, [ebp + 8] ; esi = xn
    mov edi, [ebp + 12] ; edi = xp
.loop_suma_inversas:
    cmp ebx, ecx ; i < n?
    jge .end_loop_suma_inversas ; si no, salir del bucle

    ; Calcular xp[i] / xn[i]
    fild dword [edi] ; cargar xp[i] como punto flotante
    fidiv dword [esi] ; dividir por xn[i]

    ; Sumar al acumulador suma_inversas += xp[i] / xn[i]
    faddp st1, st0

    add esi, 4 ; xn++
    add edi, 4 ; xp++
    inc ebx ; i++
    jmp .loop_suma_inversas
.end_loop_suma_inversas:

    ; Calcular M / suma_inversas y dejar el resultado en st0
    fild dword [ebp - 4] ; cargar M como punto flotante
    fdivrp st1, st0

.end:
    pop edi
    pop esi
    pop ebx
    mov esp, ebp
    pop ebp

ret
