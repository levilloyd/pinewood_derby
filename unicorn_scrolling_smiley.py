import unicornhat as uh
from unicorn_chars import *
import time
import colorsys

def main():
    for scroll in range(7,-12,-1):
        uh.clear()
        print_smiley(scroll + 0, BLUE)
        uh.show()
        time.sleep(0.5)

if __name__ == '__main__':
    main()
