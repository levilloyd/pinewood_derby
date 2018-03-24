import unicornhat as uh
from unicorn_chars import *
import time
import colorsys

def main():
    for scroll in range(7, -2, -1):
        uh.clear()
        print_2(scroll + 0, RED)
        print_O(scroll + 3, RED)
        uh.show()
        time.sleep(0.5)

    for scroll in range(7, -2, -1):
	uh.clear()
        print_O(scroll + 0, RED)
        print_M(scroll + 4, RED)
        uh.show()
        time.sleep(0.5)

if __name__ == '__main__':
    main()
