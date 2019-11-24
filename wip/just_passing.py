from sys import stdin


def jp(A, passes):
    mark_passes(A)
    for j in range(1,len(A[0])):
        for i in range(len(A)):
            if A[i][j][0] == -1: continue
            elif i == 0: 
                A[i][j][0], A[i][j][1] = other_row(A, i, j, 'top')
            elif i == len(A)-1: 
                A[i][j][0], A[i][j][1] = other_row(A, i, j, 'bot')
            else: A[i][j][0], A[i][j][1] = mid_row(A, i, j)
    ans = float('inf')
    for i in range(len(A)):
        # print("1st: {} | 2nd: {}".format(A[i][len(A[0])-1][0], A[i][len(A[0])-1][1]))
        if A[i][len(A[0])-1][0] < ans and A[i][len(A[0])-1][1] == passes:
            ans = A[i][len(A[0])-1][0]
    print('impossible') if type(ans) == float else print(ans)


def mark_passes(A):
    for j in range(1, len(A[0])-1):
        for i in range(1, len(A)-1):
            if is_pass(A, i, j):
                A[i][j][1] += 1


def is_pass(A, i, j):
    if A[i+1][j][0] == -1 or A[i-1][j][0] == -1 or A[i][j-1][0] == -1 or A[i][j+1][0] == -1: return False
    elif A[i][j][0] < A[i-1][j][0] and A[i][j][0] < A[i+1][j][0] and A[i][j][0] > A[i][j+1][0] and A[i][j][0] > A[i][j-1][0]:
        return True
    return False


def mid_row(A, i, j):
    ml, dl, tl = A[i][j-1], A[i+1][j-1], A[i-1][j-1]
    if ml[0] == -1 and dl[0] == -1 and tl[0] == -1: return A[i][j][0], A[i][j][1]
    if ml[0] == -1: ml[0] = float('inf')
    if dl[0] == -1: dl[0] = float('inf')
    if tl[0] == -1: tl[0] = float('inf')
    smallest_neighbour = min(ml, dl, tl)
    # print("ml: {} | dl: {} | tl: {}".format(ml,dl,tl))
    # print("smallest_n: {} | i,j: {}, {}".format(smallest_neighbour, i, j))
    return A[i][j][0] + smallest_neighbour[0], A[i][j][1] + smallest_neighbour[1]


def other_row(A, i, j, row):
    if row == 'top': ml, ol = A[i][j-1], A[i+1][j-1]
    elif row == 'bot': ml, ol = A[i][j-1], A[i-1][j-1]
    if ml[0] == -1 and ol[0] == -1: return A[i][j][0], A[i][j][1]
    if ml[0] == -1: return A[i][j][0] + ol[0], A[i][j][1] + ml[1]
    if ol[0] == -1: return A[i][j][0] + ml[0], A[i][j][1] + ml[0]
    smallest_neighbour = min(ml ,ol)
    return A[i][j][0] + smallest_neighbour[0], A[i][j][1] + smallest_neighbour[1]


r, c, p = stdin.readline().split()
A = []
for i in range(int(r)):
    row = [[int(i),0] for i in stdin.readline().split()]
    A.append(row)
jp(A, int(p))
