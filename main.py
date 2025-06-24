from pygame import KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT
from pygame import K_ESCAPE, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9
from pygame import K_KP1, K_KP2, K_KP3, K_KP4, K_KP5, K_KP6, K_KP7, K_KP8, K_KP9
# from pygame import K_DOWN, K_UP, K_RIGHT, K_LEFT
from pygame import init, event, quit, display, mixer, font
from sys import exit
from random import randint
from funciones.dibujar_cruces import dibujar_cruces


init()
mixer.init()
fondo = display.set_mode((800, 600))  # Inicializar Pygame y crear la ventana principal con tamaño 800x600.
fondo_rect = fondo.fill('white')


numero = randint(1, 9)

key_numbers = [K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
key_numbers += [K_KP1, K_KP2, K_KP3, K_KP4, K_KP5, K_KP6, K_KP7, K_KP8, K_KP9]

fuente = font.SysFont('Verdana', 48)

guesses = 0
while True:
    for e in event.get([KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT]):
        if (e.type == KEYDOWN and (e.key == K_ESCAPE)) or e.type == QUIT:
            quit()
            exit('Normal')

        elif e.type == KEYDOWN:
            if e.key in key_numbers:
                number = e.unicode
                render = fuente.render(number, True, 'black')
                render_rect = render.get_rect(center=fondo_rect.center)
                fondo.fill('white', render_rect)
                fondo.blit(render, render_rect)
                if number != numero and guesses < 4:
                    fondo.blit(dibujar_cruces(), [3 + guesses *40, 0])
                    guesses += 1
                else:
                    quit()
                    exit('Perdiste')

    display.update()


