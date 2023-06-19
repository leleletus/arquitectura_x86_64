import asyncio
import time
import random
import numpy as np

min = 20000
max = 2147483647 #fijo un numero base int max
data =  []
cliente = []
tsubasta= 60


async def precio(idx: str): #funcion que calcula precio y lo que demora en ofertar cada uno
   
    
    valor= random.randint(min,max) #poniendo como maximo que puedan ofrecer 999k
    await asyncio.sleep(random.randint(0, 10))
    #print(f"{idx} ofrece: {valor}") #para depurar
    
    data.append(valor)
    cliente.append(idx)

async def comparar_precio(numero): #funcion de la 2
    global min
    global max
    if (numero > data): #si ofrece mayor que el entonces considera reofertar
        if(random.randint(0,1)): #si deciden hacer una reoferta
            min= min+500 #el nuevo minimo serta de 500 extra
            max= min*1.2 #el nuevo maximo sera 1.2 el nuevo minimo


async def main(): #principal donde se ejecutara asincronamente para cada uno
    await asyncio.gather (precio("a") , precio("b"), precio("c"), precio("d"), precio("e"))
    await asyncio.sleep(tsubasta)
    lista=list(zip(cliente,data)) #los unimos
    
    print(f"Participante {cliente} hizo reoferta de {dato}")
    ofertas= sorted(lista, key=lambda price: price[1],reverse=True) #las ordenamos de mayor a menor
    print(f"El ganador es: {ofertas[0][0]}")

if __name__ == "__main__":
    asyncio.run(main())