from sys import stdin

n1, n2 = stdin.readline().split()
n1, n2 = int(n1[::-1]), int(n2[::-1])
print(n1) if n1 > n2 else print(n2)