n = int(input())
rolls = [int(i) for i in input().split(" ")]
roll_set = set(rolls)
d_roll = {}
for i in roll_set:
    d_roll[i] = 0
for j in rolls:
    d_roll[j] += 1

unique_max = 0
for k,v in d_roll.items():
    if k > unique_max and v == 1: unique_max = k
if unique_max == 0: print('none')
else:
    print(rolls.index(unique_max) + 1)