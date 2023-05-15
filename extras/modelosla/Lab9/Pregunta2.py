import cv2
import os
import urllib.request
from threading import Thread
import time

#Pregunta a:
def img_serie (url):
    for i in range(len(url)):
       urllib.request.urlretrieve(url[i],f"foto_serie_{i+1}.png")

#Pregunta b:
def img_paralelo(url,nombre):
    urllib.request.urlretrieve(url,nombre)

#pip install opencv-contrib-python
#pip install pillow

if __name__=="__main__":

   urls = ['https://media.istockphoto.com/photos/peruvian-dancers-at-the-parade-in-cusco-picture-id612718846',
           'https://media.istockphoto.com/photos/caporales-dance-group-picture-id509802736',
           'https://media.istockphoto.com/photos/native-peruvian-group-of-young-girls-dancing-the-wayna-raimi-picture-id1149386588',
           'https://media.istockphoto.com/photos/peruvian-poor-woman-smiling-with-traditional-inca-clothing-picture-id1149686551',
           'https://media.istockphoto.com/photos/dancing-with-horses-picture-id516727199',
           'https://media.istockphoto.com/photos/peruvian-dancers-picture-id458405427'] 

   os.chdir("/home/antonio/DanzasyTrajesDelPeru/") #Ruta de acceso del archivo "DanzasyTrajesDelPeru"

   print(os.getcwd()) #Imprime la ruta que estoy usando
   print("         ")

   a1 = time.perf_counter()
   img_serie(urls)
   a2 = time.perf_counter()

   t_serie = a2 - a1 


   a3 = time.perf_counter()
   t1 = Thread(target=img_paralelo, args=(urls[0],"foto_paralelo_1.png"))
   t2 = Thread(target=img_paralelo, args=(urls[1],"foto_paralelo_2.png"))
   t3 = Thread(target=img_paralelo, args=(urls[2],"foto_paralelo_3.png"))
   t4 = Thread(target=img_paralelo, args=(urls[3],"foto_paralelo_4.png"))
   t5 = Thread(target=img_paralelo, args=(urls[4],"foto_paralelo_5.png"))
   t6 = Thread(target=img_paralelo, args=(urls[5],"foto_paralelo_6.png"))

   t1.start()
   t2.start()
   t3.start()
   t4.start()
   t5.start() 
   t6.start()

   t1.join()
   t2.join()
   t3.join()
   t4.join()
   t5.join()
   t6.join()
   a4 = time.perf_counter()

   t_paralelo = a4 - a3

   print(f"Tiempo de ejecucion en serie : {t_serie:0.2f} segundos ")
   print("     ")
   print(f"Tiempo de ejecucion en paralelo : {t_paralelo:0.2f} segundos ")
   print("     ")
   print(f"Speedup (factor de aceleración) : {t_serie/t_paralelo}")

