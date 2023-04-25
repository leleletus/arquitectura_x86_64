    global moda_asm_int
section .text

moda_asm_int:
;rdi <- *arreglo
;rsi <- N
    xor r8,r8   ; cont_max
    xor r9,r9   ; cont_int
    xor r10,r10 ; moda_value
    xor r11,r11
    xor r13,r13
    xor rbx,rbx
for_i:
    xor r9,r9    ; cont_int = 0
    xor r13,r13  ; j = 0
    for_j:
        mov eax, [rdi+4*r11]
        mov ebx, [rdi+4*r13]
        cmp eax,ebx
        je update_cont_int
    go_j:
        inc r13
        cmp r13,rsi
        jne for_j
    cmp r9,r8
    jg update_cont_max
go_i:
    inc r11
    cmp r11,rsi
    jne for_i

salida:
    mov eax,r10d
    ret

update_cont_int:
    inc r9
    jmp go_j

update_cont_max:
    mov r8, r9
    mov r10d, eax
    jmp go_i

