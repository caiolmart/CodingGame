import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
if n == 0:
    print('0')
    quit()
closest = 5526
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if abs(t) < abs(closest):
        closest = t
    if abs(t) == abs(closest):
        if t > 0 or closest > 0:
            closest = abs(closest)        
print(closest)