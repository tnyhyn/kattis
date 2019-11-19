from sys import stdin

n = int(input())
for i in range(n):
    r, e, c = stdin.readline().split()
    if int(e) - int(c) > int(r): print('advertise')
    elif int(e) - int(c) < int(r): print('do not advertise')
    else: print('does not matter')