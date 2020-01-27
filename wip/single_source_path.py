from sys import stdin
from collections import defaultdict


def dfs(d, start, visited):
    visited.add(start)
    for node, _ in d[start]:
        if node not in visited:
            dfs(d, node, visited)
    return len(visited)


def djikstras(graph, start, reachable, nodes):
    final = {}
    dist = [float('inf') for i in range(nodes)]
    dist[start] = 0
    visited = 0
    if visited >= reachable: print("asdf")
    while visited < reachable:
        index, min_node = 0, float('inf')
        for i, num in enumerate(dist):
            if num < min_node and i not in final:
                min_node = num
                index = i
        final[index] = min_node
        for node, weight in graph[index]:
            dist[node] = min(dist[node], weight + min_node)
        visited += 1
    return final


while True:
    ini = [int(i) for i in stdin.readline().split()]
    if sum(ini) == 0: break
    if ini[1] == 0:
        for _ in range(ini[2]):
            q = int(input())
            if q == ini[3]: print(0)
            else: print("Impossible")
    else:
        d = defaultdict(list)
        for _ in range(ini[1]):
            k, v, w = stdin.readline().split()
            d[int(k)].append([int(v), int(w)])
        # print("d:",d)
        reachable = dfs(d, ini[3], set())
        # print("reachable:",reachable)
        shortest_path = djikstras(d, int(ini[3]), reachable, ini[0])
        # print("s:",shortest_path)
        for _ in range(ini[2]):
            q = int(input())
            if q in shortest_path: print(shortest_path[q])
            else: print("Impossible")
        print('\n')