import sys

def flex(width, par):
    room_splits = [0] + width + par
    room_splits.sort()
    ans = []
    for i in range(len(room_splits)):
        for j in range(i+1, len(room_splits)):
            if room_splits[j] - room_splits[i] not in ans:
                ans.append(room_splits[j] - room_splits[i])
    return sorted(ans)

lines = [line.rstrip('\n') for line in sys.stdin.readlines()]
for i in range(0, len(lines), 2):
    width = [int(lines[i].split(' ')[0])]
    p = [int(i) for i in lines[i+1].split()]
    ans = flex(width, p)
    for i in ans:
        print(i)