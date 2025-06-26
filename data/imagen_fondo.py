from pygame import image
from os import path, getcwd

_ruta = path.join(getcwd(), 'data', 'Fondo.png')
imagen_fondo = image.load(_ruta)

eraser = imagen_fondo.subsurface((385, 271, 31, 59))
eraser_rect = eraser.get_rect(topleft=[385,271])