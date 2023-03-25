#!/bin/sh


# hay $# $@ y '$@'
echo "Número de argumentos: $#"
cantidad=$# #tienen que estar pegados $# para saber cuantos argumentos pase

for ((i=1;i<=$cantidad;i+=2)) #doble parentesis para que use mecanismo de c
#no utilizo directamente $# porque se altera al hacer shit y se rompe el ciclo for
do

    echo "Ciclo iterativo número $(( (i+1)/2 ))" #doble parentesis para expresdion aritmetica
    bash c.sh $1 $2
    shift 2


done



   
