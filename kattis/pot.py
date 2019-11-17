from sys import stdin


def pot(eqn):
    total = 0
    for i in eqn:
        t = ''
        for j in i[:len(i)-1]:
            t += j
        total += int(t) ** int(i[-1])
    return total

n = int(input())
eqn = []
for i in range(n):
    nums = list(stdin.readline().rstrip())
    eqn.append(nums)
print(pot(eqn))