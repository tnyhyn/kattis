L = int(input())
D = int(input())
X = int(input())
N, M = float('inf'), float('-inf')
for i in range(L, D+1):
    tsum = 0
    for j in str(i):
        tsum += int(j)
    if tsum == X and i <= N: N = i
    if tsum == X and i >= M: M = i
print(N)
print(M)
