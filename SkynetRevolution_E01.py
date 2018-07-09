import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

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

#function to find all paths
def find_all_paths(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
	    return [path]
	paths = []
	for node in graph[start]:
	    if node not in path:
	        newpaths = find_all_paths(graph, node, end, path)
	        for newpath in newpaths:
	            paths.append(newpath)
	return paths
# game loop
while True:
	si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

	#find shortest path from Skynet Agent to every gateway
	path_list = []
	for g in gateways:
		path = min(find_all_paths(graph, si, g),key=len)
		path_list.append(path)

	#take shortest path from shortest paths
	path = min(path_list,key=len)

	s0 = path[0]
	s1 = path[1]

	# Example: 0 1 are the indices of the nodes you wish to sever the link between
	print(f"{s0} {s1}")