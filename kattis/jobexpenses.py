from sys import stdin

n = input()
nums = [int(i) for i in stdin.readline().split()]
expenses = 0
for i in nums:
    if i < 0: expenses += i
print(expenses*-1)