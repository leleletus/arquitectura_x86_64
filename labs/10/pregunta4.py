import asyncio
import time
import random
import numpy as np

# Crear un diccionario con los precios base de cada bloque
precios_base = {"Bloque 0": 15_000_000, "Bloque 1": 15_000_000, "Bloque 2": 15_000_000}

# Crear un diccionario con los precios actuales de cada bloque
precios_actuales = precios_base.copy()

# Crear un diccionario con los ganadores de cada bloque
ganadores = {}

# Crear una lista con los participantes
participantes = ["Telefónica", "Claro", "Entel"]

# Crear una variable para el número de rondas
rondas = 3

# Crear una variable para la duración de cada ronda en segundos
duracion_ronda = 30

async def reofertar(idx: str):
    global precios_base
    global precios_actuales

    # Elegir un bloque al azar para ofertar
    bloque = random.choice(list(precios_base.keys()))

    # Elegir un valor al azar entre el precio actual del bloque y el 20% más
    valor = random.randint(precios_actuales[bloque], int(precios_actuales[bloque] * 1.2))

    # Actualizar el precio actual del bloque y el ganador del bloque
    precios_actuales[bloque] = valor
    ganadores[bloque] = idx

    print(f"Participante {idx} hizo oferta de {valor} para el {bloque}")
    await asyncio.sleep(random.randint(0, 10))

async def ronda(n: int):
    global precios_base
    global precios_actuales

    # Imprimir el inicio de la ronda y los precios base de cada bloque
    print(f"\nRonda {n}:")
    print("Precios actuales:")
    for bloque, precio in precios_actuales.items():
        print(f"{bloque}: ${precio}")

    # Ejecutar las funciones reofertar concurrentemente para cada participante durante la duración de la ronda
    inicio = time.perf_counter()
    while time.perf_counter() - inicio <= duracion_ronda:
        await asyncio.gather(reofertar("Telefónica"), reofertar("Claro"), reofertar("Entel"))

    # Imprimir el fin de la ronda y los precios actuales de cada bloque
    print(f"\nSe cumplió el tiempo de {duracion_ronda} segundos. Ronda {n} finaliza.")

    # Actualizar los precios base para la siguiente ronda
    precios_base = precios_actuales.copy()

async def main():
    
    # Imprimir los bloques a subastar y los precios base de cada bloque
    print("Bloques a subastar:")
    print("Bloque 0: 50 MHz")
    print("Bloque 1: 60 MHz")
    print("Bloque 2: 70 MHz")
    
    print("\nPrecio base de cada bloque: $15 millones")
    
    # Ejecutar las funciones ronda secuencialmente para cada número de ronda
    for i in range(1, rondas + 1):
        await ronda(i)

    # Imprimir los ganadores de cada bloque al finalizar las rondas
    print("\nLos ganadores son:")
    for bloque, ganador in ganadores.items():
        print(f"{bloque}: {ganador} con ${precios_actuales[bloque]}")

if __name__ == "__main__":
    asyncio.run(main())