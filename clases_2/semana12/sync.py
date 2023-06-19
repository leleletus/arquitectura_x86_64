
import time

def count(idx: int):
    print(f"[{idx}]","Uno")
    time.sleep(1)
    print(f"[{idx}]","Dos")

def main():
    for i in range(3):
        count(i)

if __name__ == "__main__":
    tic = time. perf_counter()
    main()
    toc = time. perf_counter()
    print(f"{__file__} executed in {toc-tic:0.4f} seconds.")