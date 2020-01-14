from sys import stdin

n = input()
temp = [int(i) for i in stdin.readline().split()]

#  5
# 23 27 31 28 30
dt = [float('inf'), float('inf')]
for i in range(2, len(temp)):
    t = max(temp[i], temp[i-2])
    if t < dt[1]: 
        dt[0], dt[1] = i-1, t
print(dt[0], dt[1])

