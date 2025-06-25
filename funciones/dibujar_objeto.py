from pygame import draw

def dibujar_objeto_colision(fondo, color, x, y, ancho, alto):
    """
    Dibuja un rectangulo para usar de colision en el juego.
    Parametros:
    fondo: Superficie donde se dibuja el objeto (siempre fondo).
    color: Color del rectangulo (tupla RGB).
    x: Posicion x del rectangulo.
    y: Posicion y del rectangulo.
    ancho: Ancho del rectangulo.
    alto: Alto del rectangulo.
    """
    rectangulo = draw.rect(fondo, color, (x, y, ancho, alto))
    return rectangulo