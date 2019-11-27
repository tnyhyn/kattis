from sys import stdin

d = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'T': 10,
    '8': 0,
    '7': 0
}
hand, dom = stdin.readline().split()
total = 0
for i in range(int(hand)*4):
    h = str(input())
    if h[0] in d:
        total += d[h[0]]
    elif h[0] == 'J':
        if h[1] == dom: total += 20
        else: total += 2
    elif h[0] == '9':
        if h[1] == dom: total += 14
print(total)
