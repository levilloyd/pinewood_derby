
import unicornhat as uh
from unicorn_chars import *
import time
import colorsys

colors = [RED, YELLOW, BLUE, GREEN, PURPLE, ORANGE]

def main():
    uh.clear()
    for x in range(0, len(colors) - 1):
        light_all(colors[x])
        uh.show()
        time.sleep(1)
        uh.clear()

if __name__ == '__main__':
    main()


