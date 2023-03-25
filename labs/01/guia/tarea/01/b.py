import sys  # importamos lo del systema

if len(sys.argv) != 3: #por si escribimos mal
    sys.exit("Error en los argumentos ingresados")
else:
    a = int (sys.argv[1]) 
    b = int (sys.argv[2])

    suma=0;
    for i in range(a,b+1): #le aumento 1 para que incluya b
        suma += 1/i

    mediaArmonica = (b - a + 1) / suma
    print("La media armonica de los numeros desde {} hasta {} es: {:.2f}".format(a, b, mediaArmonica))

    #tarda mas python