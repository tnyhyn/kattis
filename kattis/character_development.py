def chardev(n):
    if n == 0  or n == 1: 
        print(0)
        return
    relationships = 0
    for k in range(2, n + 1):
        relationships += f(n) / (f(k) * f(n-k))
    print(int(relationships))


def f(n):
    if n == 0 or n == 1: return 1
    return n * f(n - 1)

chardev(int(input()))