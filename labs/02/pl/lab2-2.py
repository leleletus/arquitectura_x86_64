import math
import matplotlib.pyplot as plt

def pi_cuarto_while_1(ref,tol): 
  s = 0
  l = []
  i = 0
  term = 0
  eps = 0 #agregamos

  while 1:

    if i % 2:
      signo=-1
    else:
      signo=1
      
    term = signo*(1/(2*i+1))
    s +=term
    l.append(s)

    eps = abs(ref - s) / ref

    if eps < tol:
      break

    i+=1

  return s,l

s2,l2 = pi_cuarto_while_1(math.pi/4,1e-4)

plt.plot( l2, 'o')
plt.title('Serie Pi/4')
plt.grid(True)

print(f"El valor es {s2}")
print(f"La cantidad de terminos son: {len(l2)}")
print("Los terminos son:")
print(l2)