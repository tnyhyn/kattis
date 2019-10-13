def trik(s):
    ans = [1, 0, 0]
    for i in s:
        if i == 'A': ans[0], ans[1] = ans[1], ans[0]
        elif i == 'B': ans[1], ans[2] = ans[2], ans[1]
        else: ans[0], ans[2] = ans[2], ans[0]
    print(ans.index(1) + 1)

trik(str(input()))