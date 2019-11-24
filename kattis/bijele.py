# One king
# One queen
# Two rooks
# Two bishops
# Two knights
# Eight pawns

# 0 1 2 2 2 7
from sys import stdin

req = [1, 1, 2, 2, 2, 8]
found = [int(i) for i in stdin.readline().split()]
for i in range(len(req)):
    print(req[i] - found[i], end='')
    print(' ', end='')

