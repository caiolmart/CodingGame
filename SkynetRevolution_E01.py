import sys
import math
import collections

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
graph = {}
for i in range(n):
    graph[i] = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph[n1].append(n2)
    graph[n2].append(n1)
gateways = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)

# root connected to all gateways
# graph[-1] = gateways


# BFS Search -> returns tuple with (agent position, node on path to gateway)
def block_agent(graph, root, goal):
    visited, queue = set(), collections.deque(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if neighbour == goal:
                    return (vertex, goal)
                visited.add(neighbour)
                queue.append(neighbour)


#  game loop
while True:
    # The index of the node on which the Skynet agent is positioned this turn
    si = int(input())
    s0, s1 = block_agent(graph, gateways, si)
    # Example: 0 1 are the indices of the nodes you wish to sever the link
    # between
    print(f"{s0} {s1}")
