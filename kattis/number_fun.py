# 6
# 1 2 3
# 2 24 12
# 5 3 1
# 9 16 7
# 7 2 14
# 12 4 2

from sys import stdin


def nf(i, j, k):
    if i+j == k: return 'Possible'
    if i*j == k: return 'Possible'
    if i-j == k  or j-i == k: return 'Possible'
    if i/j == k or j/i == k: return 'Possible'
    return 'Impossible'

n = int(input())
for i in range(n):
    i, j, k = stdin.readline().split()
    print(nf(int(i), int(j), int(k)))