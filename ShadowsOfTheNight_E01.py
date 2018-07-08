import sys
import math
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
d_bound = h - 1
u_bound = 0
r_bound = w - 1
l_bound = 0  
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)    
    x = x0
    y = y0
    if 'L' in bomb_dir: 
        x = x0 - (x0 - l_bound) // 2 - 1
        r_bound = x0 - 1
    if 'R' in bomb_dir:
        x = x0 + (r_bound - x0) // 2 + 1
        l_bound = x0 + 1
    if 'D' in bomb_dir: 
        y = y0 + (d_bound - y0) // 2 + 1
        u_bound = y0 + 1
    if 'U' in bomb_dir:
        y = y0 - (y0 - u_bound) // 2 - 1
        d_bound = y0 - 1

    x0 = x
    y0 = y
    # the location of the next window Batman should jump to.
    print(f"{x} {y}")
