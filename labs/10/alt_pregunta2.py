import asyncio
import time
import random
import numpy as np

#usando diccionarioss

min_price = 20000  # El precio base de la subasta
max_price = 100000  # El precio máximo que puede ofrecer un participante
data =  {}  # Un diccionario que guarda el nombre y la oferta de cada participante
cliente = ["a", "b", "c", "d", "e"]  # La lista de participantes

async def precio(idx: str): 
    valor= random.randint(min_price, max_price)  # La oferta inicial del participante
    data[idx] = valor  # Guardamos el nombre y la oferta del participante en el diccionario
    print(f"{idx} ofrece ${valor}")  # Imprimimos la oferta del participante
    start = time.time()  # Guardamos el tiempo de inicio de la subasta
    while time.time() - start < 60:  # Mientras no se cumplan los 60 segundos de la subasta
        await asyncio.sleep(random.randint(0, 10))  # El participante se demora un tiempo aleatorio en decidir si reoferta o no
        max_offer = max(data.values())  # Buscamos la oferta más alta hasta el momento
        if max_offer > valor:  # Si la oferta más alta es mayor que la del participante actual
            reoffer = random.choice([True, False])  # El participante decide aleatoriamente si reoferta o no
            if reoffer:  # Si decide reofertar
                valor = max_offer + random.randint(500, 1000)  # Su nueva oferta es mayor que la oferta más alta en un incremento mínimo de $500
                data[idx] = valor  # Actualizamos el diccionario con la nueva oferta del participante
                print(f"{idx} ofrece ${valor}")  # Imprimimos la nueva oferta del participante

async def main(): 
    await asyncio.gather(*(precio(idx) for idx in cliente))  # Ejecutamos las funciones de los participantes de forma asíncrona y esperamos a que todas terminen

    lista = list(data.items())  # Convertimos el diccionario en una lista de tuplas

    resultado = ', '.join(f'{item[0]}: {item[1]}' for item in lista)  # Unimos los elementos de la lista en una sola cadena de texto

    print(f"Ofertas finales: {resultado}")  # Imprimimos las ofertas finales de cada participante

    ofertas= sorted(lista, key=lambda price: price[1],reverse=True)  # Ordenamos la lista por el segundo elemento de cada tupla en orden descendente
    print(f"El ganador es: {ofertas[0][0]}")  # Imprimimos el nombre del ganador

if __name__ == "__main__":
    asyncio.run(main())  # Ejecutamos la función asíncrona main usando asyncio.run