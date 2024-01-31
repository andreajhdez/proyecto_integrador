from typing import List, Tuple
import readchar
from readchar import readkey, key
import os
# Laberinto proporcionado como una cadena
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Definición de función para pasar la cadena de texto a una matriz.


def matriz_carac(laberinto: str):
    # Se separan las filas de la cadena de texto utilizando la funcion .split
    filas = laberinto.split("\n")

    # Se agregan los carácteres a la matriz utilizando list para separar los carácteres individualmente
    # indi es el indicador de cada fila dentro de filas
    matriz_map = [list(indi) for indi in filas]

    return (matriz_map)

# Definimos función para limpiar terminal e imprimir la matriz que arroja la función matriz_carac


def limpiar(matriz_map: list):
    # condicional para limpiar la consola en windows y linux
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    # recorrido para imprimir la matriz por fila, si no hago esto se imprimen todas pegadas y el laberinto no se logra visualizar.
    for fil in matriz_map:
        print(" ".join(fil))

# Funcion del main loop del juego del laberinto


def main_loop(mapa_lab: List[List[str]], p_i: Tuple[int, int], p_f: Tuple[int, int]):
    # Coordenadas del jugador
    px, py = p_i
    # Se le asigna un carácter para que represente graficamente la posición en la que se encuentra.
    personaje = "P"
    mapa_lab[px][py] = personaje
    limpiar(mapa_lab)
    # Ciclo que se procesa mientras el jugador encuentra la posicion final del laberinto.
    while (px, py) != p_f:
        mapa_lab[px][py] = personaje
        # Leer del teclado las teclas
        posicion = readchar.readkey()
        px_new, py_new = px, py
        # Condicional para almacenar que hace cada tecla en nuevas variables de posición.
        if posicion == key.UP:
            px_new -= 1
        elif posicion == key.DOWN:
            px_new += 1
        elif posicion == key.LEFT:
            py_new -= 1
        elif posicion == key.RIGHT:
            py_new += 1
        else:
            print("Solo puedes usar las flechas :/")

        # Se calcula el numero de filas y de columnas del laberinto
        # se resta uno porque las matrices se recorren desde el 0 y el condicional de abajo sera utilizando desde la posición 0,0
        num_filas = len(mapa_lab)-1
        num_columnas = len(mapa_lab[0])-1

        # condicional para verificar si la nueva posición esta en el mapa y no es una pared
        if 0 <= px_new and num_filas >= px_new and 0 <= py_new and num_columnas >= py_new and mapa_lab[px_new][py_new] != "#":
            # Se restaura la posición vieja
            mapa_lab[px][py] = "."
            px, py = px_new, py_new
        else:
            print("Haz chocado con una pared o estas en el límite del laberinto :(")

        # Se agrega la representación del usuario a la posición a la que se movio despues de darle al teclado
        mapa_lab[px][py] = personaje
        limpiar(mapa_lab)
    print("Lo lograste! Encontraste la salida :)")


matriz_mapa = matriz_carac(laberinto)
pi = (0, 0)
pf = (len(matriz_mapa)-1, len(matriz_mapa[0])-1)

main_loop(matriz_mapa, pi, pf)
