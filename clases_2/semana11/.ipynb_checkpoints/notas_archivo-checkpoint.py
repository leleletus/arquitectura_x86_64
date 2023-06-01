#entrada procesamiento salida de imprimir resultados
#ponerle medidas de performance
def procesa_fila(fila: list[str]) -> list[float]:
    nums = list()
    for num_str in fila:
        num = float(num_str)
        nums.append(num)
    
    return nums


def calcula_nota_final(alumno: list[float]) -> float:
    nota_lab = 0
    for i in range(1, 13):
        nota_lab += alumno[i]
    nota_lab = nota_lab / 13.0

    nota_final = ((5 * nota_lab) + (2.5 * alumno[13]) + (2.5 * alumno[14])) / 10.0

    return nota_final


if __name__ == '__main__':
    with open("notas.csv", "r") as f:
        contenido = f.read()

    filas = contenido.split("\n")
    
    alumnos = list()
    for i in range(1, len(filas)):
        fila = filas[i].split(",")
        nota_alumno = procesa_fila(fila)
        alumnos.append(nota_alumno)
    
    notas_finales = list()
    for alumno in alumnos:
        nota = calcula_nota_final(alumno)
        notas_finales.append(nota)

    print(alumnos)
    print(notas_finales)