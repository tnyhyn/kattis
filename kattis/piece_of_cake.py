from sys import stdin


def cut(n, h, v):
    cuts = []
    cuts.append(h*v)
    cuts.append(h*(n-v))
    cuts.append(v*(n-h))
    cuts.append((n-h)*(n-v))
    print(max(cuts) * 4)

n, h, v = stdin.readline().split()
cut(int(n), int(h), int(v))