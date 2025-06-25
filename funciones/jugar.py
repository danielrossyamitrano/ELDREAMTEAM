from pygame import KEYDOWN
from data import *
from funciones import *
from funciones.mostrar_texto import mostrar_texto

def jugar(numero, number, guesses, event, fondo, fondo_rect):
    message_img, message_rect = None, None
    if event.type == KEYDOWN:
        if event.key in key_numbers:
            number = event.unicode
            render = mostrar_texto(number, COLOR_NEGRO)
            render_rect = render.get_rect(center=fondo_rect.center)
            fondo.fill(COLOR_BLANCO, render_rect)
            fondo.blit(render, render_rect)

    if number is not None and guesses < 4:
        if number != numero:
            fondo.blit(dibujar_cruces(), [3 + guesses * 40, 0])
            guesses += 1

        if guesses > 3:
            message_img = mostrar_texto('Perdiste', COLOR_ROJO)
            message_rect = message_img.get_rect(center=fondo_rect.center)
        elif number == numero:
            message_img = mostrar_texto('¡Ganaste!', COLOR_VERDE)
            message_rect = message_img.get_rect(center=fondo_rect.center)

    return guesses, message_img, message_rect