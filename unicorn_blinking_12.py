import unicornhat as uh
from unicorn_chars import *
import time
import colorsys


def main():
    colors = [GREEN, RED, BLUE, ORANGE, PURPLE, YELLOW]
    uh.clear()
    uh.show()
    for i in range(12):
        print_1(2, colors[i%6])
        print_2(4, colors[i%6])
        uh.show()
        time.sleep(1)
        uh.show()

if __name__ == '__main__':
    main()
