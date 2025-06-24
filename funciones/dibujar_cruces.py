from pygame import draw, Surface, SRCALPHA


def dibujar_cruces():
    cruz = Surface((32, 32), SRCALPHA)
    draw.line(cruz, 'red', [0, 0], [32, 32],4)
    draw.line(cruz, 'red', [0, 32], [32, 0],4)

    return cruz
