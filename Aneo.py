import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
speed = int(input())
#print('a', speed * 3.6)
#print('a', speed)
light_count = int(input())
inputs = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    #print((distance, duration))
    inputs.append((distance, duration))



def get_speed_range(distance, duration, i):
    if i > 0:
        max_speed = (distance / (2 * i * duration)) * 3.6
    else:
        max_speed = speed
    min_speed = (distance / ((2 * i + 1) * duration)) * 3.6
    if max_speed > speed:
        max_speed = speed
    if min_speed >= speed:
        min_speed = None
        max_speed = None
    return min_speed, max_speed
    
def merge_ranges(min_speed1, max_speed1, min_speed2, max_speed2):
    min_speed = max(min_speed1, min_speed2)
    max_speed = min(max_speed1, max_speed2)
    if min_speed > max_speed or int(max_speed) < min_speed:
        min_speed, max_speed = None, None
    return min_speed, max_speed


def solve():
    light = 0
    max_speeds = [speed] * light_count
    min_speeds = [0] * light_count
    
    iterations = [0] * light_count
    passed_all = False
    while not passed_all:
        passed = False
        while not passed:
            #print("light", light)
            #print('iterations', iterations)
            #print('inputs', inputs[light][0], inputs[light][1])
            this_min, this_max = get_speed_range(
                inputs[light][0], 
                inputs[light][1], 
                iterations[light]
            )
            #print("this min max", this_min, this_max)
            #print('before')
            #print("min", min_speeds)
            #print("max", max_speeds)
            if this_min == None:
                iterations[light] += 1
                continue
            if light > 0:
                if this_max <= min_speeds[light - 1]:
                    iterations[light] = 0
                    iterations[light - 1] += 1
                    light -= 1
                    #print('returning')
                    continue
            if light == 0:
                max_speeds[light] = this_max
                min_speeds[light] = this_min
                passed = True
            else:
                new_min, new_max = merge_ranges(
                    min_speeds[light - 1],
                    max_speeds[light - 1],
                    this_min,
                    this_max
                )
                #print(this_min, this_max)
                #print(new_max, new_min)
                if new_min == None:
                    iterations[light] += 1
                else:
                    max_speeds[light] = new_max
                    min_speeds[light] = new_min
                    passed = True   
            #print('after')
            #print("min", min_speeds)
            #print("max", max_speeds)
        light += 1
        if light == light_count:
            passed_all = True
    return max_speeds[light - 1]

print(int(solve()))