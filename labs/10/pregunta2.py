import asyncio
import time
import random
import numpy as np

min_price = 20_000
max_price = 999_000 #fijo un numero base int max
data =  [] #crea lista vacia, {} es para crear diccionario
cliente = []
tsubasta= 60

async def reofertar(idx:str):
    global min_price
    global max_price

    if(random.randint(0,1)): #si deciden hacer una reoferta
            if data: #si tiene datos
                max_oferta=max(data) #obtenemos la mayor oferta de la lista
                min_price= max_oferta+500 #el nuevo minimo sera de 500 extra
                max_price= min_price*1.2 #el nuevo maximo sera 1.2 el nuevo minimo

            valor = random.randint(min_price, int(max_price))  # Calculamos una nueva oferta
            data.append(valor)
            cliente.append(idx)
            print(f"Participante {idx} hizo reoferta de: {valor}")
            await asyncio.sleep(random.randint(0, 10))
    

async def main(): #principal donde se ejecutara asincronamente para cada uno

    inicio = time.perf_counter()
    while time.perf_counter()-inicio <=tsubasta-10:  # ya que la ultima corrida puede durar 10 min max     
        await asyncio.gather (reofertar("a") , reofertar("b"), reofertar("c"), reofertar("d"), reofertar("e"))
    
    lista=list(zip(cliente,data)) #los unimos
    
    #print(f"Participante {cliente} hizo reoferta de {dato}")
    ofertas= sorted(lista, key=lambda price: price[1],reverse=True) #las ordenamos de mayor a menor
    print(f"El ganador es: {ofertas[0][0]}")

if __name__ == "__main__":
    asyncio.run(main())