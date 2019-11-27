from sys import stdin

n = int(input())
seen, count = set(), 0
for i in range(n):
    school, team = stdin.readline().split()
    if school not in seen and count != 12:
        count += 1 
        seen.add(school)
        print(school, team)    
