from datetime import datetime
import time

def registra_num(pista: str) -> float:
    num_flag = False
    while not num_flag:
        num = input(pista)
        try:
            num_val = float(num)
            num_flag = True
        except ValueError: #si es que no se ejecuta todo el try , pasa algun error en medio , sale
            print(f"{datetime.now()}: Numero invalido --> {num}, ingrese uno bueno")
    return num_val
            

        
if __name__ == "__main__":
    inicio = time.perf_counter()
    labs =list()
    
    #Opeeraciones de E/S
    for i in range(12):
        lab = registra_num(f"Por gavor ingrese nota del lab {i+1}: ")
        print(f"Nota ingresada: {lab}")
        labs.append(lab)
        
    e1 = registra_num(f"Por gavor ingrese nota del examen 1: ")
    e2 = registra_num(f"Por gavor ingrese nota del examen 2: ")
    
    
    #Procesamiento
    n1= sum(labs) /float(len(labs))
    nota_final = (5*n1 + 2.5*e1 + 2.5*e2 )/10.0
    
    
    fin = time.perf_counter()
    #Salida
    print(f"La nota final del curso es: {nota_final}")
    print(f"Tiempo de ejeucion total: {fin-inicio} segundos")