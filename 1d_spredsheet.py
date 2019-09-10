import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def solve(operation, arg_1, arg_2):
    if operation == 'VALUE':
        return int(arg_1)
    elif operation == 'ADD':
        return int(arg_1) + int(arg_2)
    elif operation == 'SUB':
        return int(arg_1) - int(arg_2)
    elif operation == 'MULT':
        return int(arg_1) * int(arg_2)

n = int(input())
inputs = []
dependencies = {}
for i in range(n):
    dependencies[i] = []
    operation, arg_1, arg_2 = input().split()
    inputs.append([operation, arg_1, arg_2])
    if arg_1[0] == '$':
        dependencies[i].append(int(arg_1[1:]))
    else:
        dependencies[i].append(None)
    if arg_2[0] == '$':
        dependencies[i].append(int(arg_2[1:]))
    else:
        dependencies[i].append(None)

output = [None] * n
def solve_all(idx):
    if output[idx] != None:
        return output[idx]

    operation = inputs[idx][0]
    if dependencies[idx] == [None, None]:
        arg_1 = inputs[idx][1]
        arg_2 = inputs[idx][2]
        return solve(operation, arg_1, arg_2)

    if dependencies[idx][0] != None:
        arg_1 = solve_all(dependencies[idx][0])
        inputs[idx][1] = arg_1
        dependencies[idx][0] = None
    else:
        arg_1 = inputs[idx][1]

    if dependencies[idx][1] != None:
        arg_2 = solve_all(dependencies[idx][1])
        inputs[idx][2] = arg_2
        dependencies[idx][1] = None
    else:
        arg_2 = inputs[idx][2]
    
    return solve(operation, arg_1, arg_2)

for i in range(n):
    output[i] = solve_all(i)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(output[i])