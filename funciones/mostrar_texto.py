from main import *

def mostrar_texto(texto, color, posicion):
    """
    Muestra un texto en la pantalla con un color y una posion especificos
    Texto: texto a mostrar
    Color: color del texto (tupla RGB)
    Posicion: posicion del texto (tupla x, y)
    """
    fuente = pygame.font.SysFont("Arial", 36)
    texto_impreso = fuente.render(texto, True, color)
    fondo.blit(texto_impreso, posicion)
    

