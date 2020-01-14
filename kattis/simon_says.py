from sys import stdin

n = int(input())
for i in range(n):
    l = stdin.readline().split()
    if l[0] == 'Simon' and l[1] == 'says':
        print(' '.join(l[2:]))
        