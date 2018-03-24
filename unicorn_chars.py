import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (225, 0, 235)
YELLOW = (246, 255, 0)
ORANGE = (255, 165, 0)

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

def print_0(shift, color):
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 0, 2, *color)
    uh.set_pixel(shift + 1, 0, *color)
    uh.set_pixel(shift + 1, 3, *color)
    uh.set_pixel(shift + 2, 1, *color)
    uh.set_pixel(shift + 2, 2, *color)

def print_1(shift, color):
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 0, 2, *color)
    uh.set_pixel(shift + 0, 3, *color)

def print_2(shift, color):
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 1, 0, *color)
    uh.set_pixel(shift + 1, 1, *color)
    uh.set_pixel(shift + 0, 2, *color)
    uh.set_pixel(shift + 0, 3, *color)
    uh.set_pixel(shift + 1, 3, *color)

def print_3(shift, color):
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 1, 0, *color)
    uh.set_pixel(shift + 1, 1, *color)
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 1, 2, *color)
    uh.set_pixel(shift + 1, 3, *color)
    uh.set_pixel(shift + 0, 3, *color)

def print_4(shift, color):
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 1, 1, *color)
    uh.set_pixel(shift + 2, 0, *color)
    uh.set_pixel(shift + 2, 1, *color)
    uh.set_pixel(shift + 2, 2, *color)
    uh.set_pixel(shift + 2, 3, *color)

def print_5(shift, color):
    uh.set_pixel(shift + 1, 0, *color)
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 1, 2, *color)
    uh.set_pixel(shift + 1, 3, *color)
    uh.set_pixel(shift + 0, 3, *color)

def print_6(shift, color):
    print_1(shift, color)
    uh.set_pixel(shift + 1, 0, *color)
    uh.set_pixel(shift + 1, 2, *color)
    uh.set_pixel(shift + 1, 3, *color)
    
def print_7(shift, color):
    uh.set_pixel(shift + 0, 0, *color)
    print_1(shift + 1, color)

def print_8(shift, color):
    print_1(shift, color)
    print_1(shift + 1, color)

def print_9(shift, color):
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 1, 0, *color)
    uh.set_pixel(shift + 1, 1, *color)
    uh.set_pixel(shift + 1, 2, *color)
    uh.set_pixel(shift + 1, 3, *color)

def print_10(shift, color):
    print_1(shift, color)
    print_0(shift + 2, color)

def print_11(shift, color):
    print_1(shift, color)
    print_1(shift+2, color)

def print_smiley(shift, color):
    uh.set_pixel(shift + 0, 2, *color)
    uh.set_pixel(shift + 1, 0, *color)
    uh.set_pixel(shift + 1, 3, *color)
    uh.set_pixel(shift + 2, 3, *color)
    uh.set_pixel(shift + 3, 0, *color)
    uh.set_pixel(shift + 3, 3, *color)
    uh.set_pixel(shift + 4, 2, *color)

def print_O(shift, color):
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 0, 2, *color)
    uh.set_pixel(shift + 1, 0, *color)
    uh.set_pixel(shift + 1, 3, *color)
    uh.set_pixel(shift + 2, 1, *color)
    uh.set_pixel(shift + 2, 2, *color)

def print_M(shift, color):
    uh.set_pixel(shift + 0, 0, *color)
    uh.set_pixel(shift + 0, 1, *color)
    uh.set_pixel(shift + 0, 2, *color)
    uh.set_pixel(shift + 0, 3, *color)
    uh.set_pixel(shift + 1, 1, *color)
    uh.set_pixel(shift + 2, 0, *color)
    uh.set_pixel(shift + 2, 1, *color)
    uh.set_pixel(shift + 2, 2, *color)
    uh.set_pixel(shift + 2, 3, *color)

def light_all(color):
    for i in range(8):
        for j in range(4):
            uh.set_pixel(i, j, *color)
