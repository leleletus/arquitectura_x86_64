import asyncio
import time

async def count(idx: int):
    print(f"[{idx}]", "Uno")
    await asyncio.sleep(1)
    print(f"[{idx}]", "DOS")

async def main():
    await asyncio.gather (count(0) , count(1), count(2))

if __name__ == "__main__":
    tic = time. perf_counter()
    asyncio.run(main())
    toc = time. perf_counter()
    print(f"{__file__} executed in {toc-tic:0.4f} seconds.")