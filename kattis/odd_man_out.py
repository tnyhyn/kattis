from sys import stdin


def ans(guests):
    paired = set(guests)
    for i in paired:
        c = guests.count(i)
        if c == 1: return i
    else: return i

n = int(input())
for i in range(n):
    guests = int(input())
    code = [int(i) for i in stdin.readline().split()]
    print("Case #{}: {}".format(i + 1, ans(code)))
