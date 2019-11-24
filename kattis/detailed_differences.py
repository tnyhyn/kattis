# 3
# ATCCGCTTAGAGGGATT
# GTCCGTTTAGAAGGTTT
# abcdefghijklmnopqrstuvwxyz
# bcdefghijklmnopqrstuvwxyza
# abcdefghijklmnopqrstuvwxyz0123456789
# abcdefghijklmnopqrstuvwxyz0123456789


n = int(input())
for i in range(n):
    w1, w2 = input(), input()
    print(w1)
    print(w2)
    for i in range(len(w1)):
        if w1[i] == w2[i]: print('.', end='')
        else: print('*', end='')
    print('\n')
    
