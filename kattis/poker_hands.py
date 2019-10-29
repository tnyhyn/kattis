from sys import stdin

hand = [i[0] for i in stdin.readline().split()]
rank = 'A23456789TJQK'
count = 0
print(hand)
for i in rank:
    if hand.count(i) > count:
        count = hand.count(i)
print(count)

