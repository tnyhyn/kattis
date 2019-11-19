from sys import stdin
from collections import deque


def printer(A):
    for i in A:
        print(i)

def sheba(A):
    amoebas = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == '#':
                amoebas += 1
                bfs(A, i, j)
    # printer(A)
    print(amoebas)


def bfs(A, i, j):
    q = deque()
    q.append([i,j])
    seen = set()
    directions = [(-1,0), (0,1), (1,0), (0,-1), (-1,-1), (-1,1), (1,1), (1,-1)]
    while q:
        i, j = q.popleft()
        for d in directions:
            ni, nj = 0, 0
            # print(d[0], d[1])
            ni, nj= i+d[0], j+d[1]
            # print(ni, nj)
            if ni < 0 or ni >= len(A) or nj < 0 or nj >= len(A[0]) or A[ni][nj] == '.':
                continue
            if (ni,nj) in seen: continue
            else: seen.add((ni,nj))
            A[ni][nj] = 'X'
            q.append([ni,nj])
    # print(seen)


i, j = stdin.readline().split()
A = []
for i in range(int(i)):
    row = list(stdin.readline().rstrip())
    A.append(row)
sheba(A)