import unicornhat as uh
from unicorn_chars import *
import time
import colorsys


def main():
    uh.clear()
    light_all(YELLOW)
    uh.show()
    time.sleep(5)

if __name__ == '__main__':
    main()
