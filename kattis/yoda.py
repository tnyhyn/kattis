def yoda(n, k):
    if len(n) > len(k):
        k = k.zfill(len(n))
    else: n = n.zfill(len(k))
    n, k = list(n), list(k)
    for i in range(len(n)):
        if int(n[i]) > int(k[i]): k[i] = ''
        elif int(n[i]) < int(k[i]): n[i] = ''
    n = [str(i) for i in n if i != '']
    k = [str(i) for i in k if i != '']
    if len(n) == 0: 
        print('YODA')
        print(int(''.join(k)))
    elif len(k) == 0:
        print(int(''.join(n)))
        print('YODA')
    else:
        print(int(''.join(n)))
        print(int(''.join(k)))

n1, n2 = str(input()), str(input())
yoda(n1, n2)