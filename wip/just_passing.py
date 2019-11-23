# 5 7 2
# -1 -1 2 5 4 3 1
# 3 4 1 4 1 2 1
# 3 4 5 5 3 4 5
# 2 3 2 1 2 3 2
# -1 5 4 1 4 4 2

from sys import stdin


def jp(A, passes):





r, c, p = stdin.readline().split()
A = []
for i in range(int(r)):
    row = [int(i) for i in stdin.readline().split()]
    A.append(row)
jp(A, int(p))
