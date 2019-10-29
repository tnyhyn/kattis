from sys import stdin

n = int(input())
while n != -1:
    distance, prev = 0, 0
    for i in range(n):
        d, h = stdin.readline().split()
        distance += int(d) * (int(h) - prev)
        prev = int(h)
    print(distance, "miles")
    n = int(input())