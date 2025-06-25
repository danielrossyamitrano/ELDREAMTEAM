from pygame import font
import pygame

def mostrar_texto(texto, color):
    """
    Muestra un texto en la pantalla con un color y una posion especificos
    Texto: texto a mostrar
    Color: color del texto (tupla RGB)
    Posicion: posicion del texto (tupla x, y)
    """
    fuente = pygame.font.SysFont("Verdana", 48)
    texto_impreso = fuente.render(texto, True, color)
    return texto_impreso

# from funciones.dibujar_objeto import dibujar_objeto_colision

# dibujar_objeto_colision(fondo, COLOR_ROSA, 650, 550, 70, 50)

# display.set_caption("Adivina el numero") # Establece el nombre de la ventana.


