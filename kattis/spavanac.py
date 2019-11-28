from sys import stdin


h, m = stdin.readline().split()
if int(m) - 45 < 0:
    h = (int(h) - 1)%24
m = (int(m) - 45)%60
print(h, m)



