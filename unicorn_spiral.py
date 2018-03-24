import unicornhat as uh
from unicorn_chars import *
import time
import colorsys

snake = [(0,0), (1,0), (2,0), (3,0), 
         (4,0), (5,0), (6,0), (7,0),
         (7,1), (7,2), (7,3), (6,3),
         (5,3), (4,3), (3,3), (2,3),
         (1,3), (0,3), (0,2), (0,1),
         (1,1), (2,1), (3,1), (4,1),
         (5,1), (6,1), (6,2), (5,2),
         (4,2), (3,2), (2,2), (1,2)]

def main():
    reverse_snake = []
    uh.clear()
    while snake:
        x, y = snake.pop(0)
        uh.set_pixel(x, y, PURPLE)
        reverse_snake.append((x,y))
        uh.show()
        time.sleep(0.4)
    while reverse_snake:
        x, y = reverse_snake.pop()
        uh.set_pixel(x, y, GREEN)
        uh.show()
        time.sleep(0.1)
    time.sleep(3)
        

if __name__ == '__main__':
    main()
