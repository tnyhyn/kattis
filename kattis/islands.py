from sys import stdin


def ans(grid):
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':
                dfs(grid, i, j)
                islands += 1
    print(islands)

def dfs(grid, i, j):
    if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0: return None
    if grid[i][j] == 'W' or grid[i][j] == 'X': return None
    grid[i][j] = 'X'
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)


row, col = stdin.readline().split()
planet = []
for i in range(int(row)):
    l = list(stdin.readline().rstrip())
    planet.append(l)
ans(planet)