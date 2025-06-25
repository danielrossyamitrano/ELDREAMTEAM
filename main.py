from pygame import KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT, K_ESCAPE
from pygame import init, event, quit, display, mixer, font
from funciones.dibujar_cruces import dibujar_cruces
from random import randint
from time import sleep
from sys import exit
from data import *

init()
mixer.init()
fondo = display.set_mode((800, 600))  # Inicializar Pygame y crear la ventana principal con tamaño 800x600.
fondo_rect = fondo.fill(COLOR_BLANCO)


numero = str(randint(1, 9))


fuente = font.SysFont('Verdana', 48)

guesses = 0
while True:
    message_img, message_rect = None, None
    number = None
    for e in event.get([KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT]):
        if (e.type == KEYDOWN and (e.key == K_ESCAPE)) or e.type == QUIT:
            quit()
            exit('Normal')

        elif e.type == KEYDOWN:
            if e.key in key_numbers:
                number = e.unicode
                render = fuente.render(number, True, COLOR_NEGRO)
                render_rect = render.get_rect(center=fondo_rect.center)
                fondo.fill(COLOR_BLANCO, render_rect)
                fondo.blit(render, render_rect)

    if number is not None and guesses < 4:
        if number != numero:
            fondo.blit(dibujar_cruces(), [3 + guesses * 40, 0])
            guesses += 1

        if guesses > 3:
            message_img = fuente.render('Perdiste', True, COLOR_ROJO)
            message_rect = message_img.get_rect(center=fondo_rect.center)
        elif number == numero:
            message_img = fuente.render('¡Ganaste!', True, COLOR_VERDE)
            message_rect = message_img.get_rect(center=fondo_rect.center)

    if message_img is not None:
        fondo.fill(COLOR_BLANCO)
        fondo.blit(message_img, message_rect)
        display.update()
        sleep(3)
        quit()
        exit()

    display.update()


