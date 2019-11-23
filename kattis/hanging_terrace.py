# 4 5
# enter 3
# enter 2
# leave 1
# enter 1
# enter 2

from sys import stdin

limit, n = stdin.readline().split()
limit, rejected = int(limit), 0
curr = 0
for i in range(int(n)):
    event, num = stdin.readline().split()
    if event == 'enter':
        if curr + int(num) > limit: rejected += 1
        else: curr += int(num)
    else:
        curr -= int(num)
print(rejected)
