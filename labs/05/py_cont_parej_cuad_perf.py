

import math
import numpy as np

def py_cont_parej_cuad_perf(v):
    q=0 #cantidad de pares encontrados 
    x=np.array([]) #arreglo de los x
    y=np.array([]) #arreglo de los y

    #empezamos ordenando el arreglo
    cantidad=len(v) #calculamos numero de terminos
    for i in range(cantidad): # desde el 0 a cantidad -1

        for j in range(0, cantidad - i - 1):
          
            if v[j] > v[j + 1]:
                temp = v[j]
                v[j] = v[j+1]
                v[j+1] = temp

    #una vez ordenado emepezamos la funcion

    for i in range(cantidad-1): #ya que j siempre es 1 mayor este no llega a cantidad
        #hacemos que siempre sea mayor que j asi evitamos comparar con el mismo termino y 
        #eliminamos las repetidas ya que (x[i],y[j]) es lo mismo que (x[j],y[i])

        for j in range(i+1,cantidad): 
             
            #comprobamos que pertenezcan del 0 al 9
            if ( (v[i]>=0 and v[i]<=9) and (v[j]>=0 and v[j]<=9) ):

                #preguntamos si son cuadrados perfectos
                if( math.sqrt(v[i] * v[j])%1==0  ): #la raiz cuadrada de su multiplicacion no debe dar residuo
                     x=np.append(x,v[i]) #agregamos los valores al arreglo
                     y=np.append(y,v[j]) #agregamos los valors al arreglo
                     q+=1  #actualizamos la cantidad de pares
                     #print(f"{v[i],v[j]}")  #par ver los valores

    return (q,x,y)

