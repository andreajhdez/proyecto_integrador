# Se importan las funciones del readchar.
from readchar import readkey, key
# inicializamos el bucle infinito, poniendo el while siempre verdadero.
while True:
    k = readkey()
    # Si se oprime la tecla hacia arriba se sale del bucle infinito y si se oprime cualquier tecla del teclado imprime las teclas en consola.
    if k != key.UP:
        print(k)
    if k == key.UP:
        break

