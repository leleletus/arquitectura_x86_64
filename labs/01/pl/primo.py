
import sys

def main():
    # Verificar si se ingresó un argumento
    if len(sys.argv) != 2:
        print("Ingrese solo 1 numero")
        return

    # Convertir el argumento a un entero
    n = int(sys.argv[1])
    es_primo = 1

    # Verificar si el número es primo
    if n <= 1:
        es_primo = 0
    else:
        for i in range(2, int(n**(0.5))+1): #calcula la raiz cuadrada y le suma 1 y lo redondea abajo
            if n % i == 0: # si encuentra algun divisor
                es_primo = 0 #entonces no es primo 
                break

    # Imprimir el resultado
    if es_primo:
        print(f"El número {n} es primo")
    else:
        print(f"El número {n} no es primo")


if __name__ == "__main__":
    main()
#para poder ejecutarlo directamente como independiente 0
#poderlo llamar como modulo y usar la funcion cuando desee
