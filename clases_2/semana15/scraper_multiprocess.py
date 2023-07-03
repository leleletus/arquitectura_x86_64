import requests
from multiprocessing import Pool, cpu_count
import time

session = None

def set_global_session():
    global session
    if session is None:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        pass
        # print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with Pool(processes=cpu_count(), initializer=set_global_session) as pool:
        pool.map(download_site, sites)



if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ]  * 80

    inicio = time.perf_counter()
    download_all_sites(sites)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion multiproceso: {fin - inicio} segundos")

#pip install memory_profiler
#sin -M para los demas, si o si el multiprocess necesita -M
# python -m mprof run -M scraper_multiprocess.py
# python -m mprof plot