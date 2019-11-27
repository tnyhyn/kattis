from sys import stdin

at_bats = int(input())
bats = [int(i) for i in stdin.readline().split()]
at_bats, sp = int(at_bats), 0
for i in bats:
    if i == -1: at_bats -= 1
    else: sp += i
print(sp/at_bats)