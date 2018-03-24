import unicornhat as uh
from unicorn_chars import *
import time
import colorsys

def main():
    for scroll in range(7,-12,-1):
        uh.clear()
        print_H(scroll + 0, RED)
        print_I(scroll + 4, RED)
        uh.show()
        time.sleep(0.5)

if __name__ == '__main__':
    main()
