plan_max = int(input())
sum = 0
for i in range(int(input())):
    sum += plan_max - int(input())
print(sum + plan_max)