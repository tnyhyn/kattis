from sys import stdin
from math import sqrt

n, w, h = stdin.readline().split()
n, w, h = int(n), int(w), int(h)
for i in range(n):
    c = sqrt(w**2 + h**2)
    match = int(input())
    if c >= match: print('DA')
    else: print('NE')