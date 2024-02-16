# proyecto_integrador
Este es un proyecto de fundamentos de programación, el cual, con propósitos educativos tiene el objetivo de crear un videojuego de texto. Un videojuego de texto, también se le puede referir como videojuego ASCII, es un videojuedo donde se utilizan caracteres en la pantalla en vez de gráficos elaborados. Estos juegos necesitan menos recursos que los que son más gráficos.

Ahora bien, el videojuego específico de este proyecto consiste en crear un laberinto de texto, en donde el usuario logrará recorrer laberintos utilizando las teclas de dirección. Enseguida encontrarás una guía de los carácteres ASCII que serán utilizados para construir este laberinto y su significado: 

'#' - representa una pared
'.' - representa un pasillo
'P' - representa el personaje

Este proyecto es mantenido y realizado por Andrea Juliana Hernández.

------------------------------------------------------------------------------------------------
En seguida encontrarás el proceso de desarrollo de este juego que fue realizado por partes. En cada entrega se desarrollo una parte de este laberinto y serán explicados a continuación: 

# Archivo Main & README
La primera parte de este proyecto fue dividida en dos ítems:
1. Crear archivo README con la descripción del proyecto
2. Crear el archivo main del proyecto, donde se pide el nombre de jugador por teclado y se imprime un mensaje de bienvenida con el nombre del jugador.

# Proyectointegrador_2
Acá se realiza un bucle infinito que se detuviera al presionar la tecla de arriba del eclado. Esto, con el fin de aprender a utilizar la librería readchar y entender como leer un carácter del teclado.

# Proyectointegrador_3
Este avance se trató de manipular la terminal. Para esto, se crea una función que debe borrar la terminar e imprimir numeros desde 0 a 50 cada vez que se oprima la tecla "n" del teclado. 
Se importa libreria os.
Se utiliza la siguiente instrucción para limpiar la terminal: os.system('cls' if os.name=='nt' else 'clear')

# Proyectointegrador_4
En esta entrega se desarrolla el juego en si con funciones. 
1. Se crea matriz_carac --> la función diseñada para convertir una cadena de texto con el mapa a una matriz. Con el objetivo de utilizar esta estructura de datos para recorrerla.
2. Se crea la función: limpiar --> encargada de limpiar la terminal e imprimir la matriz que retorna la función matriz_carac
3. Se crea la función: main_loop --> encargada del juego del laberinto especificamente. Datos de entrada: mapa_lab, p_i, p_f. Consiste de un ciclo con while que funciona a partir de una posicion inicial en el mapa y se acaba cuando se llega a la posición final. De esta forma se imprime que se ganó el juego. 
En esta función se utiliza la libreria readchar, para identificar las flechas del teclado, y también un condicional if para comparar la posición actual del jugador con el mapa y arroja un mensaje cuando se choca con una pared.

# Proyectointegrador_5
En esta entrega se toma todo lo de proyectointegrador_4 y se crean dos clases: Juego y JuegoArchivo. 
La primera clase, Juego, contiene todo lo que se realizó en proyecto integrador 4, y es basicamente todo el código que necesita el juego para funcionar. 
La segunda clase, JuegoArchivo es la encargada de leer un archivo .txt de una ruta que da a la carpeta donde se tienen los archivos de los mapas. De estos archivos se elige uno aleatorio y se retorna una cadena de carácteres con el mapa y puntos inicial y final.
- Se utiliza os.listdir para tener una lista de los archivos en un directorio.
- Se utiliza random.choice para elegir un archivo aleatorio.
- Se utiliza .strip para eliminar espacios en blanco antes o después cuando se va a sacar la matriz de caracteres para el laberinto.

* Finalmente, con este avance se importan estas clases al main del juego (from protectointegrador_5 import Juego, JuegoArchivo) y desde allí se ingresa la ruta y se crea una instancia del juego para activarlo desde el main. 
