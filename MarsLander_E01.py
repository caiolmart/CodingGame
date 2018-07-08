import sys
import math

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append((land_x, land_y))
    
#print(surface)
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    
    i = 0
    while x > surface[i][0]:
        i += 1
    #floor height
    floor_h = (surface[i][1] + surface[i+1][1])/2
    
    #maximum accelaration
    a_max = 4 - 3.711
    
    #time to floor
    if v_speed < 0:
        floor_t = -floor_h/v_speed
    else:
        floor_t = 9999
    
    if (v_speed-0.4) + a_max*(floor_t - 0.1) < -30:
        power = '4'
    else:
        power = '0'
    
    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    print(f"0 {power}")