import matplotlib.pyplot as plt

def pi_cuarto_for(cant_terms): #definimos nuestra funcion
  s = 0
  l = []
  for i in range(cant_terms): #con 400 terminos
    if i % 2: #calculamos el signo alternado
      signo=-1
    else:
      signo=1
    term = signo*(1/(2*i+1)) #calculamos el termino individual
    #print(term)  #verificando que imprima los terminos
    s +=term #acumulamos la suma de la serie
    l.append(s)  
  return s,l

s1,l1 = (pi_cuarto_for(4000)) #vemos el valor para 400 terminos

plt.plot( l1, 'o')
plt.title('Serie Pi/4')
plt.grid(True)

print(f"El valor es {s1}")
print(f"La cantidad de terminos son: {len(l1)}")
print("Los terminos son:")
print(l1)