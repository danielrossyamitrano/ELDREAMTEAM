from pygame import KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT
from pygame import K_ESCAPE
from pygame import event, quit, display
from sys import exit

fondo = display.set_mode((800, 600))


while True:
    for e in event.get([KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT]):
        if (e.type == KEYDOWN and (e.key == K_ESCAPE)) or e.type == QUIT:
            quit()
            exit('Normal')

    display.update()


