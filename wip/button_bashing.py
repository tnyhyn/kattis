from sys import stdin
from collections import deque


def bash(target, buttons):
    # print("target: {} | buttons: {}".format(target, buttons))
    min_possible = (0, float('inf'))
    q = deque()
    seen = set()
    q.append((0,0))
    while q:
        dist, current = q.popleft()
        dist += 1
        for i in buttons:
            pressed = current
            pressed += i
            if pressed >= target and min_possible[1] >= pressed:
                min_possible = ((dist, pressed-target))
            if pressed in seen: continue
            else: seen.add(pressed)
            if pressed <= 0: continue
            elif pressed > 3600: 
                pressed = 3600
                q.append((dist, pressed))
            elif pressed == target:
                return (dist, pressed - pressed)
            else: q.append((dist, pressed))
    return min_possible


n = int(input())
for i in range(n):
    amt, target = stdin.readline().split()
    buttons = {int(i) for i in stdin.readline().split()}
    dist, remainder = (bash(int(target), buttons))
    print(dist, remainder)
