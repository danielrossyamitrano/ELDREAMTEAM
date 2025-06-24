from pygame import KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT
from pygame import K_ESCAPE
from pygame import init, event, quit, display, mixer
from sys import exit


init()
mixer.init()
fondo = display.set_mode((800, 600))


while True:
    for e in event.get([KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT]):
        if (e.type == KEYDOWN and (e.key == K_ESCAPE)) or e.type == QUIT:
            quit()
            exit('Normal')

    display.update()


