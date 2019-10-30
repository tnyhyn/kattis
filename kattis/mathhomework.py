from sys import stdin


def ans(b,d,c,l):
    found = False
    for i in range(l//b + 1):
        for j in range(l//d + 1):
            k = (l - b*i - d*j)//c
            # print("i: {} | j: {} | k: {}".format(i,j,k))
            if b*i + d*j + c*k == l and k >= 0:
                found = True
                print(i, j, k)
    if not found: print('impossible')

b,d,c,l = stdin.readline().split()
ans(int(b), int(d), int(c), int(l))