import asyncio
import time
import random
import numpy as np
import socket
import pickle

#implementando con diccionario

min_price = 20_000
max_price = 999_000
mi_diccionario = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0}
mi_diccionario["sniper"] = 0 #para agregar el nuevo al diccionario


tsubasta = 60
inicio =0

async def reofertar(idx: str):
    global min_price
    global max_price

    if random.randint(0, 1):
        if mi_diccionario[idx]:
            max_oferta = max(mi_diccionario.values())
            min_price = max_oferta + 500
            max_price = min_price * 1.2

        valor = random.randint(min_price, int(max_price))
        mi_diccionario[idx]=valor
        print(f"Participante {idx} hizo reoferta de: {valor}")
        await asyncio.sleep(random.randint(0, 10))

async def sniper():
    with open("oferta_del_sniper.txt", "r") as f:
        valor = int(f.read())
    mi_diccionario["sniper"] = valor
    print(f"Participante Sniper hizo reoferta de: {valor}")


# Programa servidor
async def handle_client(reader, writer):
    data = await reader.read(1024)
    number = pickle.loads(data)
    with open("oferta_del_sniper.txt", "w") as f:
        f.write(number)
    writer.close()

async def server():
    server = await asyncio.start_server(handle_client, 'localhost', 12345)
    async with server:
        await server.serve_forever()

# Programa cliente
async def client():
    reader, writer = await asyncio.open_connection('localhost', 12345)
    number = input("Ingresa el numero: ")
    serialized_data = pickle.dumps(number)
    writer.write(serialized_data)
    await writer.drain()
    writer.close()
    await writer.wait_closed()



async def main():
    global inicio 
    inicio = time.perf_counter()
    
    # Iniciar el servidor y el cliente antes de ejecutar las funciones reofertar
    await asyncio.gather(server(), client())
    
    while time.perf_counter() - inicio <= tsubasta - 3:
        await asyncio.gather(reofertar("a"), reofertar("b"), reofertar("c"), reofertar("d"), reofertar("e"))
    
    await sniper()

    print(f"Ofertas finales: {mi_diccionario}") 
    print(f"El ganador es: {max(mi_diccionario.items(), key=lambda x: x[1])[0]}")

if __name__ == "__main__":
    asyncio.run(main())