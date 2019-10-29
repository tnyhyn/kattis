import collections


def topo(graph):
    visited = {}
    stack = []
    for k in graph:
        visited[k] = False 
    for k in graph:
        if visited[k] == False:
            dfs(k, graph, visited, stack)
    return stack[::-1]


def dfs(key, graph, visited, stack):
    visited[key] = True
    for edge in graph[key]:
        if edge not in visited: continue
        elif visited[edge] == False:
            dfs(edge, graph, visited, stack)
    stack.append(key)


t = int(input())
map = {}
for i in range(1,t+1):
    line = input().split()
    map[line[0][:len(line[0])-1]] = line[1:]

run_file = input()
filtered_map = [run_file]
deps = collections.deque([run_file])
while deps:
    dep = deps.popleft()
    for k in map:
        if dep in map[k]: 
            deps.append(k)
            filtered_map.append(k)

filtered_map = {k: map[k] for k in set(filtered_map)}

for file in topo(filtered_map)[::-1]:
    print(file)