import math
import matplotlib.pyplot as plt

def pi_cuarto_while(tol):
  s = 0
  i = 0
  l = []
  term = 0
  eps = 1
  s_ant = 0

  while 1:

    if i % 2:
      signo=-1
    else:
      signo=1
      
    term = signo*(1/(2*i+1))
    s +=term
    l.append(s)

    if i > 0:
      eps = abs(s_ant - s) / s_ant

    if eps < tol:
      break

    s_ant = s
    i+=1

  return s,l


s,l = (pi_cuarto_while(1e-5))

plt.plot( l, 'o')
plt.title('Serie Pi/4')
plt.grid(True)

print(f"El valor es {s}")
print("Los terminos son:")
print(l)