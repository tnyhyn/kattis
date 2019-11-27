n = str(input())

while True:
    s = 0
    for i in n:
        s += int(i)
    if int(n) % s == 0: 
        print(n)
        break
    n = str(int(n) + 1)
