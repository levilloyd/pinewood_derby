import unicornhat as uh
import time
import colorsys

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

def print_H(shift, color):
    print shift
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
    print shift
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 0, 2, *color)
    uh.set_pixel(shift + 0, 3, *color)

def main():
    scroll = 7
    while True:
        uh.clear()
        #print_H(scroll + 0, GREEN)
        print_I(scroll + 0, RED)
        uh.show()
        scroll -= 1
        time.sleep(2)

if __name__ == '__main__':
    main()
