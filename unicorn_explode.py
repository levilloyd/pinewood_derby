import unicornhat as uh
from unicorn_chars import *
import time
import colorsys


def main():
    uh.clear()
for i in range(20):
    light_all(RED)
    uh.show()
    time.sleep(0.1)
    light_all(ORANGE)
    uh.show()
    time.sleep(0.1)
    light_all(YELLOW)
    uh.show()
    time.sleep(0.1)

if __name__ == '__main__':
    main()
