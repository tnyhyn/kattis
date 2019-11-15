from sys import stdin
from collections import deque


def bash(target, buttons):
    print("target: {} | buttons: {}".format(target, buttons))
    q = deque()
    q.append((0,0))
    while q:
        dist, current = q.popleft()
        dist += 1
        for i in buttons:
            pressed = current
            if dist > 10: return ('break' , 'break')
            pressed += i
            if pressed < 0: pressed = 0
            elif pressed > 3600: pressed = 3600
            elif pressed == target:
                return (dist, pressed - pressed)
            # print(dist, pressed)
            q.append((dist, pressed))


n = int(input())
for i in range(n):
    amt, target = stdin.readline().split()
    buttons = {int(i) for i in stdin.readline().split()}
    dist, remainder = (bash(int(target), buttons))
    print(dist, remainder)
