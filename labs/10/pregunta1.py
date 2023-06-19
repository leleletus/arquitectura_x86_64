import asyncio
import time
import random
import numpy as np

min = 20000
max = 100000
data =  []
cliente = []

async def precio(idx: str): #funcion que calcula precio y lo que demora en ofertar cada uno
    valor= random.randint(min,max) #poniendo como maximo que puedan ofrecer 999k
    await asyncio.sleep(random.randint(0, 10))
    #print(f"{idx} ofrece: {valor}") #para depurar
    data.append(valor)
    cliente.append(idx)

async def main(): #principal donde se ejecutara asincronamente para cada uno
    await asyncio.gather (precio("a") , precio("b"), precio("c"), precio("d"), precio("e"))
    lista=list(zip(cliente,data)) #los unimos
    print(f"Ofertas finales: {lista}")
    ofertas= sorted(lista, key=lambda price: price[1],reverse=True) #las ordenamos de mayor a menor
    print(f"El ganador es: {ofertas[0][0]}")

if __name__ == "__main__":
    asyncio.run(main())


    # mi_diccionario = {'clave1': 1, 'clave2': 'dos', 'clave3': 3.0} #usando dicccionarios
   # mi_diccionario['clave4'] = 4  # para agregar
   # mi_diccionario.pop('clave1') o del mi_diccionario['clave1']  #para borrar 1