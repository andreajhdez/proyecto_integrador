from readchar import readkey, key
import os

num = 0

while num < 50:
    num += 1
    tecla = readkey()
    if tecla == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
    print(num)
