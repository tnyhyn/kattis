def rail(x, y):
    connections = 4*x + 3*y
    if connections % 2 == 0: print('possible')
    else: print('impossible')

t = [int(i) for i in input().split(' ')]
rail(t[0], t[1])