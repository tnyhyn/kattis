from sys import stdin, setrecursionlimit
setrecursionlimit(2000)


def coast(grid):
    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i > 0 and i < len(grid)-1 and j > 0 and j < len(grid[0])-1 and surround(grid, i, j):
                grid[i][j] = -1
            if grid[i][j] == 0:
                p += dfs(grid, i, j)
    print(p + edges(grid))

def surround(grid, i, j):
    if grid[i+1][j] == 1 and grid[i-1][j] == 1 and grid[i][j+1] == 1 and grid[i][j-1] == 1:
        return True

def edges(grid):
    counter = 0
    for j in range(len(grid[0])):
        if grid[0][j] == 1: counter += 1
        if grid[len(grid) - 1][j] == 1: counter += 1
    for i in range(len(grid)):
        if grid[i][0] == 1: counter += 1
        if grid[i][len(grid[0]) - 1] == 1: counter += 1
    return counter

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1:
        return 0
    if grid[i][j] == 1:
        return 1
    grid[i][j] = -1
    return dfs(grid, i-1, j) + dfs(grid, i+1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1)


l,w = stdin.readline().split()
grid = []
for i in range(int(l)):
    r = [int(i) for i in list(stdin.readline().rstrip())]
    grid.append(r)
coast(grid)
