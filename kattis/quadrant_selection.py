def quad(p1, p2):
    if p1 > 0 and p2 > 0: print(1)
    elif p1 < 0 and p2 > 0: print(2)
    elif p1 < 0 and p2 < 0: print(3)
    else: print(4)

p1 = int(input())
p2 = int(input())

quad(p1,p2)