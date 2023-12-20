# se importan las librerías reachar y os para poder realizar el ejercicio de leer teclas y limpiar la consola
from readchar import readkey, key
import os

# Se inicia el contador numero en 0
num = 0

# Recorrido que terminará hastá que num se vuelva 50, se aymentará numero en paso de 1.
while num < 50:
    num += 1
    tecla = readkey()
    # si se presiona la tecla n se limpia la consola y continúa el ciclo hasta que lleguemos a 50.
    if tecla == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
    print(num)
