from sys import stdin
from collections import defaultdict, deque


def bfs(d, start):
    reachable = 0
    q = deque([start])
    seen = set([start])
    while q:
        node = q.popleft()
        if node in d:
            for i,_ in d[node]:
                if i not in seen:
                    seen.add(i)
                    q.append(i)
                    reachable += 1
    return reachable + 1


def djikstras(graph, start, nodes, seen_nodes, r):
    final = {}
    if not graph: return final
    dist = [float('inf') for i in range(nodes)]
    dist[start] = 0
    visited = 0
    while r > visited:
        index, min_node = 0, float('inf')
        for i in seen_nodes:
            if dist[i] < min_node and i not in final:
                min_node = dist[i]
                index = i
        if min_node == float('inf'): return final        
        final[index] = min_node
        for node, weight in graph[index]:
            dist[node] = min(dist[node], weight + min_node)
        visited += 1
    return final


while True:
    ini = [int(i) for i in stdin.readline().split()]
    if sum(ini) == 0: break
    d = defaultdict(list)
    seen_nodes = set()
    for _ in range(ini[1]):
        k, v, w = stdin.readline().split()
        d[int(k)].append([int(v), int(w)])
        seen_nodes.add(int(k))
        seen_nodes.add(int(v))
    reachable = bfs(d, ini[3])
    shortest_path = djikstras(d, int(ini[3]), int(ini[0]), list(seen_nodes), reachable)
    for _ in range(ini[2]):
        q = int(input())
        if q in shortest_path: print(shortest_path[q])
        else: print("Impossible")

