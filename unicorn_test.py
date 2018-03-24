import unicornhat as uh
import time
import colorsys

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

def print_H(shift, color):
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 0, 2, *color)
    uh.set_pixel(shift + 0, 3, *color)

    uh.set_pixel(shift + 1, 2, *color)

    uh.set_pixel(shift + 2, 0, *color)
    uh.set_pixel(shift + 2, 1, *color)
    uh.set_pixel(shift + 2, 2, *color)
    uh.set_pixel(shift + 2, 3, *color)

def print_I(shift, color):
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 0, 2, *color)
    uh.set_pixel(shift + 0, 3, *color)

def main():
    uh.set_pixel(-4, 0, *RED)
    uh.show()
    while True:
        pass

if __name__ == '__main__':
    main()
