from sys import stdin


def buy(m):
    if m >= 8: return 'Province or Gold'
    if m >= 6: return 'Duchy or Gold'
    if m >= 5: return 'Duchy or Silver'
    if m >= 3: return 'Estate or Silver'
    if m >= 2: return 'Estate or Copper'
    if m < 2: return 'Copper'

g, s, c = stdin.readline().split()
money = 3*int(g) + 2*int(s) + int(c)
print(buy(money))