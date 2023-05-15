
#!/bin/bash  #siempre para indicar bash


# Encontrar los números primos del 1 al 100 con primo.c
echo "Números primos del 1 al 100 (primo.c):" #para mostrar en terminal
start=$(date +%s.%N) #obtenemos un timepo de inicio
for i in {1..100}; do #repetimos las 100 veces
    ./primo $i #ejecutamos pasandole el parametro
done #acaba el for
end=$(date +%s.%N) #obtenemos tiempo final
runtime=$(echo "$end - $start" | bc) #echo lo imprime, bc calculamos la diferencia
echo "Tiempo de ejecución: $runtime segundos" #mostramos tiempos
#time (ejecutable) mide el tiempo de ejecucion del scriot,py,c 


# Encontrar los números primos del 1 al 100 con primo.py
echo "Números primos del 1 al 100 (primo.py):"
start=$(date +%s.%N)
for i in {1..100}; do
    python3 primo.py $i
done
end=$(date +%s.%N)
runtime=$(echo "$end - $start" | bc)
echo "Tiempo de ejecución: $runtime segundos"
