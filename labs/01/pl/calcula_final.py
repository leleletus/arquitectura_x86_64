#en python

import sys #para recibir parametros de entrada

def nota_del_final(a, b):
  res = (110 - 3*a - 3*b) / 4
  print("Calculando por cuánto me voy:", res)
  return res

if len(sys.argv) != 3: #siempre la mimsa funcion es un parametro asi serian 2 + name
  print("Debe ingresar exactamente 2 notas") #de no recibir 2 mostrar esto
  sys.exit(0) #se acaba

x = int(sys.argv[1]) #guardamos el primero  cast de entero para pasarlo a entero
y = int(sys.argv[2]) #guardamos el segundo

resultado = nota_del_final(x, y)
print(resultado)
