from sys import stdin
from collections import deque


def path(A):
    q = deque()
    q.append([[0,0], 0])
    seen = set((0,0))
    while q:
        loc, dist = q.popleft()
        moves = A[loc[0]][loc[1]]
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        dist += 1
        # print("seen: {}".format(seen))
        for d in directions:
            d[0], d[1] = d[0]*moves, d[1]*moves
            # print('d[0]: {} | d[1]: {}'.format(d[0], d[1]))
            loci = d[0] + loc[0]
            locj = d[1] + loc[1]
            # print("loc: {},{} | dist: {}".format(loci, locj, dist))
            if (loci, locj) in seen: 
                # print("seen")
                continue
            else: seen.add((loci, locj))
            if loci == len(A) - 1 and locj == len(A[0]) - 1:
                return dist
            if loci < 0 or loci >= len(A) or locj < 0 or locj >= len(A[0]):
                # print("pass")
                continue
            # print("added")
            q.append([(loci, locj), dist])
    return -1

i, j = stdin.readline().split()
grid = []
for i in range(int(i)):
    row = [int(i) for i in list(stdin.readline().rstrip())]
    grid.append(row)

print(path(grid))
