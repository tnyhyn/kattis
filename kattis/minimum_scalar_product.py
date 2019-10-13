def minscalar(x, y, n):
    min_product = 0
    x.sort(), y.sort()
    for i in range(n):
        min_product += (x[i] * y[n - i - 1])
    return (min_product)

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    x = [int(i) for i in input().split(" ")]
    y = [int(i) for i in input().split(" ")]
    print("Case #{}: {}".format(i, minscalar(x, y, n)))