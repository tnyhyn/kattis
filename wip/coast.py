from sys import stdin, setrecursionlimit
setrecursionlimit(2000)


def coast(grid):
    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if grid[i][j] == 0:
            s = set()
            if is_sea(grid,i,j,s) and grid[i][j] == 0:
                p += dfs(grid, i, j)
    #             print(grid)
    #             print("i: {} | j: {} | p: {}".format(i,j,p))
    # print("p: {} | edges: {}".format(p, edges(grid)))
    print(p + edges(grid))

def is_sea(grid, i, j, v):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1:
        return False
    if (i,j) in v: return False
    v.add((i,j))
    if grid[i][j] == 1:
        return False
    if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
        return True
    if is_sea(grid,i+1,j,v) or is_sea(grid,i-1,j,v) or is_sea(grid,i,j+1,v) or is_sea(grid,i,j-1,v):
        return True

def edges(grid):
    tb, lr = 0, 0
    for j in range(len(grid[0])):
        if grid[0][j] == 1: tb += 1
        if grid[len(grid) - 1][j] == 1: tb += 1
    for i in range(len(grid)):
        if grid[i][0] == 1: lr += 1
        if grid[i][len(grid[0]) - 1] == 1: lr += 1
    return tb + lr

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
