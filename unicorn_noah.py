import unicornhat as uh
from unicorn_chars import *
import time

columns = [
            {'offset': 0, 'pixels': [(0,0), (0,1), (0,2), (0,3)]},
            {'offset': 1, 'pixels': [(0,1)]},
            {'offset': 2, 'pixels': [(0,2)]},
            {'offset': 3, 'pixels': [(0,0), (0,1), (0,2), (0,3)]},
            {'offset': 4, 'pixels': []},
            {'offset': 5, 'pixels': [(0,1), (0,2)]},
            {'offset': 6, 'pixels': [(0,0), (0,3)]},
            {'offset': 7, 'pixels': [(0,1), (0,2)]},
            {'offset': 8, 'pixels': []},
            {'offset': 9, 'pixels': [(0,1), (0,2), (0,3)]},
            {'offset': 10, 'pixels': [(0,0), (0,2)]},
            {'offset': 11, 'pixels': [(0,1), (0,2), (0,3)]},
            {'offset': 12, 'pixels': []},
            {'offset': 13, 'pixels': [(0,0), (0,1), (0,2), (0,3)]},
            {'offset': 14, 'pixels': [(0,2)]},
            {'offset': 15, 'pixels': [(0,0), (0,1), (0,2), (0,3)]},
            {'offset': 16, 'pixels': []},
            {'offset': 17, 'pixels': []},
            {'offset': 18, 'pixels': []},
            {'offset': 19, 'pixels': []},
            {'offset': 20, 'pixels': []},
            {'offset': 21, 'pixels': []},
            {'offset': 22, 'pixels': []},
            {'offset': 23, 'pixels': []},
          ]

def main():
    shift = 8
    while shift > -30:
        uh.clear()
        for column in columns:
            pos = column['offset'] + shift
            if pos >= 0 and pos < 8:
                for x,y in column['pixels']:
                    uh.set_pixel(x + pos, y, YELLOW)
        shift -= 1
        uh.show()
        time.sleep(0.2)

if __name__ == '__main__':
    main()
