from pygame import KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT, K_ESCAPE  # importamos constantes de pygame
from pygame import init, event, display, mixer, image  # importamos funciones fundamentales.
from random import randint  # importamos el método randint de random para el numero aleatorio.
from time import sleep  # importamos la función sleep para que se muestre el mensaje durante un tiempito
from data import *  # data tiene los colores y las constantes
from funciones import *  # funciones tiene todas las funciones relativas al juego y las utilitarias.

init()  # inicalizamos pygame
mixer.init()  # y también el módulo mixer.
pantalla = display.set_mode((800, 600))  # Inicializar Pygame y crear la ventana principal con tamaño 800x600.
pantalla.blit(imagen_fondo, (0, 0))
numero = str(randint(1, 9))  # inicializamos el número aleatorio y lo convertimos en str porque el input del
# usuario es también un string.

guesses = 0  # acumulador de intentos
while True:  # main loop.
    message_img, message_rect = None, None  # inicializa las varibales como None porque no se crean hasta llegar al
    # resultado del juego.
    number = None  # similarmente, el number empieza como None porque espera input del usuario.
    for e in event.get([KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT]):  # captuamos los eventos de teclado
        if (e.type == KEYDOWN and (e.key == K_ESCAPE)) or e.type == QUIT:
            # si el usuario toca la tecla escape o clickea la cruz, se cierra el juego.
            salir()  # la función salir() unifica las llamadas a pygame.quit() y sys.exit()

        guesses, message_img, message_rect = jugar(numero, number, guesses, e)
        # jugar() toma el input del usuario y lo procesa siguiendo los requerimientos del juego.

    if message_img is not None:  # si el usuario ganó o perdió, se imprime el siguiente mensaje
        pantalla.blit(imagen_fondo,(0, 0))
        pantalla.blit(message_img, message_rect)  # imprime el mensaje contra el fondo.
        display.update()  # actualiza la pantalla para que se muestre el mensaje.
        sleep(3)  # invocamos a la función sleep antes de salir para darle tiempo al user de leer el mensaje
        salir()  # y salimos del juego porque está cumplida la condición de victoria o derrota.

    display.update()
