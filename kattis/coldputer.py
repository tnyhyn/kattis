# 5
# -14 -5 -39 -5 -7
from sys import stdin

n = int(input())
temps = [int(i) for i in stdin.readline().split()]
cold = 0
for i in temps: 
    if i < 0: cold +=1 
print(cold)
