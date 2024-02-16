from protectointegrador_5 import Juego, JuegoArchivo

# Se pide el nombre del jugador por teclado. Se declara variable nom_jugador, para almacenar esta información.
nom_jugador = input('Ingresa tu nombre: ')

# Se imprime el mensaje de bienvenido con el nombre del jugador (nom_jugador)
print(f'Hola {nom_jugador}, bienvenidx al Laberinto mas oscuro y retador que podrás encontrar... ¿Estás listx para iniciar este reto?')

esta_listo = input('¿Empezar? (si/no):')
if esta_listo == 'si':
    ruta = r'C:\Users\andre\OneDrive\Escritorio\ProyectoIntegrador\Mapas'

    # Se crea una instancia juego archivo, donde ingreso la ruta donde se encuentran los mapas.
    juego_archivo = JuegoArchivo(ruta)
    # Obtengo la cadena del mapa y puntos inicial y final del método para leer archivos.
    mapa, p_i, p_f = juego_archivo.leer_archivos(ruta)

    # Se crea una instancia del juego donde se ingresa el mapa y los puntos obtenidos anteriormente.
    juego = Juego(mapa, p_i, p_f)
    # Se llama a la función que crea la matriz para el jugar
    matriz_map = juego.matriz_carac(mapa)
    # Se activa el main loop donde ingresa la matris del laberinto y los puntos de inicio y fin.
    juego.main_loop(matriz_map, p_i, p_f)
else:
    pass
