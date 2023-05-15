import socket
import time
import statistics
import matplotlib.pyplot as plt

archivos_dpto = ["dpto_00.csv","dpto_01.csv","dpto_02.csv","dpto_03.csv","dpto_04.csv","dpto_05.csv",
                 "dpto_06.csv","dpto_07.csv","dpto_08.csv","dpto_09.csv","dpto_10.csv","dpto_11.csv",
                 "dpto_12.csv","dpto_13.csv","dpto_14.csv","dpto_15.csv","dpto_16.csv","dpto_17.csv",
                 "dpto_18.csv","dpto_19.csv","dpto_20.csv","dpto_21.csv","dpto_22.csv","dpto_23.csv",
                 "dpto_24.csv","dpto_25.csv","dpto_26.csv","dpto_27.csv","dpto_28.csv","dpto_29.csv",
                 "dpto_30.csv","dpto_31.csv","dpto_32.csv","dpto_33.csv","dpto_34.csv","dpto_35.csv",
                 "dpto_36.csv","dpto_37.csv","dpto_38.csv","dpto_39.csv","dpto_40.csv","dpto_41.csv",
                 "dpto_42.csv","dpto_43.csv","dpto_44.csv","dpto_45.csv","dpto_46.csv","dpto_47.csv",
                 "dpto_48.csv","dpto_49.csv","dpto_50.csv","dpto_51.csv","dpto_52.csv","dpto_53.csv",
                 "dpto_54.csv","dpto_55.csv","dpto_56.csv","dpto_57.csv","dpto_58.csv","dpto_59.csv",
                 "dpto_60.csv","dpto_61.csv","dpto_62.csv","dpto_63.csv","dpto_64.csv","dpto_65.csv",
                 "dpto_66.csv","dpto_67.csv","dpto_68.csv","dpto_69.csv","dpto_70.csv","dpto_71.csv",
                 "dpto_72.csv","dpto_73.csv","dpto_74.csv","dpto_75.csv","dpto_76.csv","dpto_77.csv",
                 "dpto_78.csv","dpto_79.csv","dpto_80.csv","dpto_81.csv","dpto_82.csv","dpto_83.csv",
                 "dpto_84.csv","dpto_85.csv","dpto_86.csv","dpto_87.csv","dpto_88.csv","dpto_89.csv",
                 "dpto_90.csv","dpto_91.csv","dpto_92.csv","dpto_93.csv","dpto_94.csv","dpto_95.csv",
                 "dpto_96.csv","dpto_97.csv","dpto_98.csv","dpto_99.csv"]

#Pregunta B:
def filtro_mediana (arr):
   for j in range(len(arr)-1): 
     for i in range(len(arr)-1):
       if (arr[i]>=arr[i+1]):
          aux=arr[i]
          arr[i]=arr[i+1]
          arr[i+1]=aux
   mediana = statistics.median(arr)
   
   return mediana

if __name__=="__main__":

    valores_cercanos = [] #Arreglo para los elementos cercanos al valor erroneo
    diferencia_lista = [] #Arreglo para los valores registrados del medidor
    promedios_lista = [] #Arreglo para los promedios obtenidos
   

    for archivos in range(len(archivos_dpto)):
       dpto = archivos_dpto[archivos]

       a = 0 #Variable para detectar las mediciones erradas
       suma = 0 #Variable para acumular la suma de las diferencias obtenidas, multiplicadas por 300
       promedio = 0 #Varianle para hallar el flujo promedio de los valores calculados
       contador = 0

       f = open(dpto,'r')
       contenido = f.read()
       f.close()
       datos = contenido.split("\n")

       num_datos = 287

       for i in range(287):
          litros_1 = datos[i+1+a].split(",")
          litros_2 = datos[i+2+a].split(",")
          a = 0
          diferencia = (float(litros_2[1]) - float(litros_1[1]))
      
          if ( diferencia > 15.0) or (diferencia < -15.0) :
              valores_cercanos.clear()

              #Pregunta C:
              for j in range(4):
                  if ((i+1+a) > 283):
                      medidas_1 = 0

                  else:     
                     valor_1 = datos[(i+1+a)+(j+1)].split(",")
                     valor_2 = datos[(i+2+a)+(j+1)].split(",")
                     medidas_1 = (float(valor_2[1]) - float(valor_1[1]))

                  valores_cercanos.append(medidas_1)

              for k in range(4):
                  if ((i+1+a) < 4):
                      medidas_2 = 0

                  else:    
                     valor_1 = datos[(i+1+a)-(j+1)].split(",")
                     valor_2 = datos[(i+2+a)-(j+1)].split(",")
                     medidas_2 = (float(valor_2[1]) - float(valor_1[1]))
                  valores_cercanos.append(medidas_2)  

              valores_cercanos.append(diferencia) 

              nuevo_valor = filtro_mediana(valores_cercanos) 
              diferencia = nuevo_valor 

              contador = contador + 1
              a = a + 1
      
          #diferencia_lista.append(diferencia)
          suma = suma + 300*diferencia

       promedio = suma/num_datos  

       promedios_lista.append(promedio)  

       #print(f"Cantidad de valores erróneos : {contador}")
   
    veces = range(len(archivos_dpto)) 

    plt.bar(veces,promedios_lista,color='red',edgecolor = 'black')
    plt.xlabel("Nro de departamento ")
    plt.ylabel("flujo promedio")
    plt.grid
    plt.savefig("grafico.png",dpi = 500)