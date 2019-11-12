from math import ceil
from sys import stdin


def ans(candy, bill):
    base = 10
    candy = ceil(candy // base ** bill) * base
    print(candy)

c, k = stdin.readline().split()
ans(int(c), int(k))