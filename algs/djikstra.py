d = {
    0: [[1,4], [7,8]],
    1: [[0,4], [7,11], [2,8]],
    2: [[1,8], [3,7], [8,2], [5,4]],
    3: [[2,7], [5,14], [4,9]],
    4: [[3,9], [5,10]],
    5: [[4,10], [3,14], [2,4], [6,2]],
    6: [[5,2], [8,6], [7,1]],
    7: [[6,1], [8,7], [1,11], [0,8]],
    8: [[2,8], [6,6], [7,7]]
}


def djikstras(graph: dict, start: int):
    final = {}
    dist = [float('inf') for i in range(len(graph))]
    dist[start] = 0
    visited = 0
    while visited < len(graph):
        index, min_node = 0, float('inf')
        for i, num in enumerate(dist):
            if num < min_node and i not in final:
                min_node = num
                index = i
        final[index] = min_node
        for node, weight in graph[index]:
            dist[node] = min(dist[node], weight + min_node)
        visited += 1
    for i,j in final.items():
        print(i, j)

djikstras(d, 0)