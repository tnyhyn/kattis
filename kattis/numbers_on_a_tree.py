from sys import stdin

def ans():
    n = stdin.readline().split()
    if len(n) == 1: return 2**(int(n[0]) + 1) - 1
    k = 0
    for i in n[1]:
        if i == 'R':
            k = 2*k + 2
        else:
            k = 2*k + 1
    return (2**(int(n[0]) + 1) - 1) - k
print(ans())

