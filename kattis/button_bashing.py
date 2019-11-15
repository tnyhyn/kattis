from sys import stdin
from collections import deque


def bash(target, buttons):
    q = deque()
    q.append(0,0)
    while q:
        current, dist = q.popleft()
        dist += 1
        for i in buttons:
            current += i
            if current < 0: current = 0
            elif current > 3600: current = 3600
            elif current == target: print()















n = int(input())
for i in range(n):
    amt, target = stdin.readline().split()
    buttons = {int(i) for i in stdin.readline().split()}
    bash(int(target), buttons)
