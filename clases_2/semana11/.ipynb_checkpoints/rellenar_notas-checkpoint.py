import random
#solucion del profe

if __name__ == '__main__':
    contenido_nuevo = ''
    codigo_inicio = 20230002
    
    for i in range(39):
        linea = f"{codigo_inicio + i},"
        notas = [f"{str(random.randint(0, 21))}," for _ in range(14)]
        notas_txt = ''.join(notas)[:-1] + "\n"
        contenido_nuevo += f"{linea}{notas_txt}"
    
    with open("notas.csv", "r") as f:
        contenido = f.read()

    contenido += f"\n{contenido_nuevo}"[:-1]

    with open("notas.csv", "w+") as f:
        f.write(contenido)
