from sys import stdin

def np(stn):
    stn_s = set(stn)
    for i in stn_s:
        if stn.count(i) > 1: return 'no'
    return 'yes'
    
stn = stdin.readline().split()
print(np(stn))


