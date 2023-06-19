"""
Se quiere simular una subasta simple de un item valioso. En esta subasta 
simple, van a haber 5 participantes, cada uno de los cuales va a elegir un precio que 
están dispuestos a pagar por el item.  
El vendedor cree que como mínimo debe recibir $20000, por lo que ese será el precio 
base de la subasta(esto para prevenir que los participantes oferten solo $1 o $10 por 
el item).  
Simule los 5 participantes con funciones asíncronas. Cada uno se va a demorar un 
tiempo aleatorio entre 0-10 segundos (use asyncio.sleep) para decidir cuál va a ser 
su oferta. Una vez que el sleep asíncrono acabe, use una función aleatoria para decidir 
el precio por cada participante. Al final, se deben comparar los precios ofrecidos y se 
debe imprimir quién ganó la subasta. 
Este es un screenshot de cómo debería verse la ejecución de su programa:
"""

