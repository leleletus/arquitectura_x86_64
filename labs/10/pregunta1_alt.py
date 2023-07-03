#alternativa by chatgpt

import asyncio  # Importamos el módulo asyncio para usar funciones asíncronas
import random  # Importamos el módulo random para generar números aleatorios

async def participant(name: str, min_price: int) -> None:
    # Esta es una función asíncrona que representa a un participante en la subasta
    await asyncio.sleep(random.randint(0, 10))  # El participante se demora un tiempo aleatorio entre 0 y 10 segundos en decidir su oferta
    bid = random.randint(min_price, min_price * 2)  # La oferta del participante es un número aleatorio entre el precio mínimo y el doble del precio mínimo
    print(f"{name} bids ${bid}")  # Imprimimos la oferta del participante
    return (name, bid)  # Retornamos el nombre del participante y su oferta

async def auction():
    # Esta es una función asíncrona que simula la subasta
    min_price = 20000  # El vendedor ha establecido un precio mínimo de $20000 para el item
    participants = ["Alice", "Bob", "Charlie", "Dave", "Eve"]  # Hay 5 participantes en la subasta
    bids = await asyncio.gather(*(participant(name, min_price) for name in participants))  # Usamos asyncio.gather para ejecutar las funciones de los participantes de forma asíncrona y esperamos a que todas terminen
    winner = max(bids, key=lambda x: x[1])  # Buscamos la oferta más alta para determinar al ganador
    print(f"The winner is {winner[0]} with a bid of ${winner[1]}")  # Imprimimos el nombre del ganador y su oferta

asyncio.run(auction())  # Ejecutamos la función asíncrona auction usando asyncio.run