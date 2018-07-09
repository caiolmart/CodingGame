import sys
import math
import collections

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
graph = {}
for i in range(n):
    graph[i] = set()
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph[n1].add(n2)
    graph[n2].add(n1)
gateways = set()
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.add(ei)


# Dijkstra's Algorithm for unweighted graph: returns paths to gateways
def dij_paths(graph, agent_pos, goals):
    distances = {}
    for i in graph.keys():
        distances[i] = math.inf
    distances[agent_pos] = 0
    unvisited = set(graph.keys())
    paths = {agent_pos: [agent_pos]}
    
    current = agent_pos
    
    while unvisited:
        print(f'current: {current}', file=sys.stderr)
        #print(graph[current], file=sys.stderr)
        neighbours = graph[current]
        print(f'neighbours: {neighbours}', file=sys.stderr)
        for node in neighbours:
            if node not in distances or distances[node] > distances[current] + 1:
                paths[node] = paths[current] + [node]
                distances[node] = distances[current] + 1
        unvisited.remove(current)
        #set current as the closest non visited node
        #print(f'distances: {distances}', file=sys.stderr)
        if unvisited:
            current = sorted(unvisited, key=lambda x: distances[x])[0]

    return paths, distances

# Select path to block
def select_path(graph, paths, distances, gateways):
    for i in gateways:
        if distances[i] == 1:
            return paths[i][0], paths[i][1]

    double_nodes = set()
    for i in gateways:
        neighbours = graph[i]
        for j in neighbours:
            danger = graph[j] & gateways
            if len(danger) >=2: double_nodes.add(j) 
    print(f'double nodes: {double_nodes}', file=sys.stderr)

    danger_nodes = set()
    for i in gateways:
    	danger_nodes.update(graph[i])
    print(f'danger nodes: {danger_nodes}', file=sys.stderr)
    if double_nodes:
        # Clear path: the nodes on the shortest path that are node danger nodes
        clear_path = {}
        for i in double_nodes:
            clear_path[i] = []
            for j in paths[i]:
                if j not in danger_nodes:
                    clear_path[i].append(j) 

        #candidates = {x:distances[x] for x in double_nodes}
        print(f'clear_path: {clear_path}', file=sys.stderr)
        node = min(clear_path,key=lambda x: len(clear_path[x]))
        print(f'node:{node}', file=sys.stderr)
        s0 = node
        s1 = list(graph[node] & gateways)[0]

    else:
        candidates = {x:distances[x] for x in gateways}
        node = min(candidates,key=candidates.get)
        path = paths[node]
        s0 = path[-2]
        s1 = path[-1]

    return s0, s1

#  game loop
while True: 

    # The index of the node on which the Skynet agent is positioned this turn
    si = int(input())
    paths, distances = dij_paths(graph, si, gateways)
    print('end dij_paths. answer:', file=sys.stderr)
    print(paths, file=sys.stderr)
    # Order by shortest path and most frequent last node to gateway
    s0, s1 = select_path(graph, paths, distances, gateways)
    print(f"{s0} {s1}")
    graph[s0].remove(s1)
    graph[s1].remove(s0)
