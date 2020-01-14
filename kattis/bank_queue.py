# 4 4
# 1000 1
# 2000 2
# 500 2
# 1200 0

from sys import stdin

n = [int(i) for i in stdin.readline().split()]
q = []
for i in range(n[0]):
    k = [int(i) for i in stdin.readline().split()]
    q.append(k)
print(q)

