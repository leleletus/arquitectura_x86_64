import sys  # importamos lo del systema

def calcula_primos(lim_inf, lim_sup): # hago la conversion de mi codigo en c pero en formato para python
    cantidad_primos=0
    #el limite superior no lo incluye por eso +1
    for i in range (lim_inf, lim_sup+1,1): #desde un rango y que vaya de 1 en 1, 
        valida_primo=0
        if i<=1:
            valida_primo=0
        else:
            for j in range (2, i+1, 1):
                if i % j ==0:
                    valida_primo+=1
        if valida_primo==1:
            cantidad_primos+=1
    return cantidad_primos

def calcula_potencias(lim_inf, lim_sup, base):
    cantidad_potencias=0
    for i in range (0,lim_sup+1,1):
        elevado = pow(base,i) #tambien se puede usar el **
        if elevado<=lim_sup and elevado>=lim_inf : # && es and en python
            cantidad_potencias+=1
    return cantidad_potencias


if len(sys.argv) != 4: #comprobamos cuiantos argumentos llegaron, default es 1 (el name)
    sys.exit("Debe ingresar 3 argumentos de entrada")
else:
    lim_inf = int (sys.argv[1])
    lim_sup = int (sys.argv[2])
    opcion  = int (sys.argv[3])

    if opcion==1 : # usamos f para dar formato con las variables en llaves
        print(f"Hay {calcula_primos(lim_inf,lim_sup)} numeros primos en este rango")
    elif opcion >=2 :
        print(f"Hay {calcula_potencias(lim_inf, lim_sup, opcion)} potencias de {opcion} en este rango")