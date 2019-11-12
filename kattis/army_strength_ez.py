from sys import stdin


def war(g, m):
    g.sort(reverse=True)
    m.sort(reverse=True)
    while True:
        if len(g) == 0: return 'MechaGodzilla'
        if len(m) == 0: return 'Godzilla'
        if g[-1] == m[-1]: m.pop()
        elif g[-1] > m[-1]: m.pop()
        else: g.pop()

n = int(input())
for i in range(n):
    blank_line = input()
    size_gdz, size_mgdz = stdin.readline().split()
    gdz = [int(i) for i in stdin.readline().split()]
    mgdz = [int(i) for i in stdin.readline().split()]
    print(war(gdz, mgdz))
