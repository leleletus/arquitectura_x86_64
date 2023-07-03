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
async def server():
    SOCK_BUFFER =1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost',5000)
    sock.bind(server_address)
    sock.listen(5)
    client_socket, client_address = sock.accept()
    data= client_socket.recv(SOCK_BUFFER) #espera que le llegue
    deserialized_data = pickle.loads(data)
    with open("oferta_del_sniper.txt", "w") as f:
        f.write(deserialized_data)

    sock.close()


# Programa cliente
async def client():
    SOCK_BUFFER =1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost',5000)
    sock.connect(server_address)
    number = input("Ingresa el numero: ")
    serialized_data = pickle.dumps(number)
    sock.sendall(serialized_data)

    sock.close()



async def main():
    global inicio 
    inicio = time.perf_counter()
    while time.perf_counter() - inicio <= tsubasta - 3:
        await asyncio.gather(reofertar("a"), reofertar("b"), reofertar("c"), reofertar("d"), reofertar("e"))
    
    await asyncio.gather(server(), client())
    await sniper()

    print(f"Ofertas finales: {mi_diccionario}") 
    print(f"El ganador es: {max(mi_diccionario.items(), key=lambda x: x[1])[0]}")

if __name__ == "__main__":
    asyncio.run(main())