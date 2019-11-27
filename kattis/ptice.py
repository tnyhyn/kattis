from itertools import cycle

n = int(input())
letters = str(input())
a = cycle(['A', 'B', "C"])
b = cycle(['B', 'A', 'B', 'C'])
c = cycle(['C', 'C', 'A', 'A', 'B', 'B'])
a_s, b_s, c_s = 0, 0, 0
for i in letters:
    at, bt, ct = next(a), next(b), next(c)
    if at == i: a_s += 1
    if bt == i: b_s += 1
    if ct == i: c_s += 1
high_score = max(a_s, b_s, c_s)
print(high_score)
if high_score == a_s: print('Adrian')
if high_score == b_s: print('Bruno')
if high_score == c_s: print('Goran')





