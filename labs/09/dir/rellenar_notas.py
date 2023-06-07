#suponiendo hay un notas.cv

#generando mi base de datos csv con: codigo, labs, examenes
import random #para crear numeros random


#abre el arcicho notas en modo escritura w
with open ("notas.csv", mode="w") as file: #aqui simplemente remplaza su contenido, para agregar seria modo a
    
    labs = [f"Lab{i}" for i in range(1,13)] #generamos los labs 1 al 12 en un arreglo (nombres en un arreglo)
    exams = [f"Lab{i}" for i in range(1,3)] #generamos los 2 examenes (los nombres en un arreglo)
    
    #para completar el encabezado que es la primera linea de los nombres
    file.write(f'Codigo,{",".join(labs)},{",".join(exams)}\n')  #se usan  '  para que no se confunda con el otro
    #utilizmamos join para unir elementos de del arreglo labs en una sola cadena de texto, y estaran separados por una ,
    
    #generamos los 40 datos
    for i in range(40): #de 0 a 39 (40 interaciones)
        codigo = f"2020{random.randint(1000,9999)}" #genera sus codigos (ultimos 4 digitos a partir de 1000)
        notas = [0] * 14  #para "declararlo" antes del subfor

        for j in range(14):
            notas[i] = random.randint(0,20)
            notas = [random.randint(0,20) for j in range(14)]
        
        #escribimos los datos
        file.write(f'{codigo},{",".join(map(str,notas))}\n') # convertimos la lista en una cadena de texto separados por coma
        #map toma 2 argumentos: una funcion y un iterable
        #aplica la funcion str a cada elemento e la lista notas , los convierte cada codigo en string ( es decir texto)
        #join une cada cadena de texto y hace que se separe por comas
    
    