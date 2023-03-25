import sys  # importamos lo del systema

if len(sys.argv) != 3: #comprobamos cuiantos argumentos llegaron, default es 1 (el name)
    sys.exit("el tarado se olvido ingresar los numeros o agrego algo demas en py xd")
else:
    a = int (sys.argv[1]) #usamos el primer argumento recibido
    b = int (sys.argv[2])

    c = a*b

    print("El producto",a,"x",b,"es:",c) #el print ya da espacio al acabar
    #print("El producto "+str(a)+" x "+str(b)+" es: "+str(c)) #otra manera usando +, se uso str para convertirlos de entero a string
    