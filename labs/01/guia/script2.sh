#!/bin/sh

echo "Alternativa 1"
for i in 1 2 3 4 5
do
    echo "Ciclo iterativo número $i"
done
#Alternativa 2 (me gusta mas)
echo "Alternativa 2"
for ((i=1;i<6;i++)) #doble parentesis para que use mecanismo de c
do
    echo "Ciclo iterativo número $i"
done

