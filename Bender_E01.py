import sys
import math

global BREAKER, STATE, PRIORITIES, MOVES, MOVING, CHANGE_D, pos, CHANGE_P, Matrix
BREAKER = False
CHANGE_D = ''
CHANGE_P = [-1,-1]
STATE = 'R'
PRIORITIES = {'R': ['SOUTH', 'EAST', 'NORTH', 'WEST'],
              'I': ['WEST', 'NORTH', 'EAST', 'SOUTH']}
MOVES = {'SOUTH':(1,0), 'EAST':(0,1), 'NORTH':(-1,0), 'WEST':(0,-1)}
MOVING = 'SOUTH'


l, c = [int(i) for i in input().split()]
Matrix = [['0' for x in range(c)] for y in range(l)] 
for i in range(l):
    row = input()
    for j in range(c):
        Matrix[i][j] = row[j]

for i in range(l):
    print(Matrix[i], file=sys.stderr)

def where(element):
    answer = []
    for i in range(l):
        for j in range(c):
            if Matrix[i][j] == element:
                answer.append([i, j])
    return answer

def is_possible(move):
    global BREAKER, STATE, PRIORITIES, MOVES, MOVING, CHANGE_D, pos, CHANGE_P, Matrix
    block = Matrix[pos[0] + move[0]][pos[1] + move[1]]
    sub_dict = {'S': 'SOUTH','W': 'WEST','E': 'EAST','N': 'NORTH'}
    if block == 'B':
        BREAKER = not BREAKER
        return True
    elif block in [' ', '$', '@']:
        return True
    elif block == 'I':
        if STATE == 'I': 
            STATE = 'R'
            return True
        else: 
            STATE = 'I'
            return True
    elif block in list(sub_dict.keys()):
        CHANGE_D = sub_dict[block]
        return True
    elif block == 'X' and BREAKER:
        Matrix[pos[0] + move[0]][pos[1] + move[1]] = ' '
        return True    
    elif block == 'T':
    	pos_ts = where('T')
    	#print([pos[0] + move[0], pos[1] + move[1]], file=sys.stderr)
    	#print(pos_ts[0], file=sys.stderr)
    	if [pos[0] + move[0], pos[1] + move[1]] == pos_ts[0]:
    		CHANGE_P = pos_ts[1]
    	else:
    		CHANGE_P = pos_ts[0]
    	return True
    else: 
        MOVING = ''
        return False


print(where('@'), file=sys.stderr)
pos = where('@')[0]
print(f'Initial Position: {pos}', file=sys.stderr)
posf = where('$')[0]
print(f'Suicide Position: {posf}', file=sys.stderr)
backtrack = set()
loop_check = []

print(len(MOVING), file=sys.stderr)
print(STATE, file=sys.stderr)
print(PRIORITIES[STATE], file=sys.stderr)
while pos != posf:
    while is_possible(MOVES[MOVING]):
        #print(f'Moving: {MOVING}, Change_D: {CHANGE_D}, Change_P: {CHANGE_P}', file=sys.stderr)
        m = MOVES[MOVING]
        if (pos[0], pos[1], STATE, BREAKER, MOVING) in backtrack:
            print('LOOP')
        backtrack.add((pos[0], pos[1], MOVING, STATE, BREAKER))
        #print(backtrack, file=sys.stderr)
        pos[0] += m[0]
        pos[1] += m[1]
        if CHANGE_D != '':
        	MOVING = CHANGE_D
        	CHANGE_D = ''
        if CHANGE_P != [-1,-1]:
        	pos = CHANGE_P
        	CHANGE_P = [-1,-1]
        #print(pos, file=sys.stderr)
        if pos == posf:
            for i in backtrack:
                print(i[2])
            sys.exit()
        #print(backtrack, file=sys.stderr)

    for p in PRIORITIES[STATE]:
        m = MOVES[p]
        #print(m, file=sys.stderr)
        if is_possible(m):
            if (pos[0], pos[1], STATE, BREAKER, MOVING) in backtrack:
                print('LOOP')
                sys.exit()
            MOVING = p
            backtrack.add((pos[0], pos[1], MOVING, STATE, BREAKER))
            #print(backtrack[-1][2])
            pos[0] += m[0]
            pos[1] += m[1]
            #print(pos, file=sys.stderr)
            if pos == posf:
                for i in backtrack:
                    print(i[2])
                    sys.exit()
            #print(backtrack, file=sys.stderr)
            break
   
for i in backtrack:
    print(i[2])