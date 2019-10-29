n = int(input())
sum = 0
for i in range(n):
    life = [float(i) for i in input().split(" ")]
    sum += (life[0]*life[1])
print(round(sum, 3))