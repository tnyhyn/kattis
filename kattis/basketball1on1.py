n = list(str(input()))
A, B = 0, 0
for i in range(1, len(n), 2):
    points, player = n[i], n[i-1]
    if player == 'A': A += int(points)
    else: B += int(points)
if A > B: print('A')
else: print('B')

