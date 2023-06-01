from datetime import datetime
import time


def registra_num(pista: str) -> float:
    num_flag = False

    while not num_flag:
        num = input(pista)
        try:
            num_val = float(num)
            num_flag = True
        except ValueError:
            print(f"{datetime.now()}: Ocurrio un error de conversion -> {num}")
        
    return num_val


if __name__ == "__main__":
    inicio = time.perf_counter()
    labs = list()

    # Operaciones de E/S
    for i in range(12):
        lab = registra_num(f"Por favor ingrese nota del lab {i + 1}: ")
        print(f"Nota ingresada: {lab}")
        labs.append(lab)
    
    e1 = registra_num(f"Por favor ingrese la nota del examen 1: ")
    e2 = registra_num(f"Por favor ingrese la nota del examen 2: ")

    # Procesamiento
    nl = sum(labs) / float(len(labs))

    nota_final = ((5 * nl) + (2.5 * e1) + (2.5 * e2)) / 10.0

    fin = time.perf_counter()
    # Salida
    print(f"La nota final del curso es: {nota_final}")
    print(f"Tiempo de ejecucion total: {fin - inicio} segundos")
