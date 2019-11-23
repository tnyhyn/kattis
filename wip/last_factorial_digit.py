def fact(n):
    if n == 0 or n == 1: print(n)
    last = 1
    for i in range(2, n+1):
        last *= i
    print(str(last)[-1])

n = int(input())
for i in range(n):
    num = int(input())
    fact(num)